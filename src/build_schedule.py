from pathlib import Path

import pandas as pd


def build_schedule():
    project = Path(__file__).resolve().parent.parent

    staff = pd.read_excel(
        project / "data" / "source.xlsx", sheet_name="Список экспертов"
    )

    optimized = pd.read_excel(project / "reports" / "optimized_shifts.xlsx")

    # -----------------------------
    # Назначаем смены сотрудникам
    # -----------------------------

    staff["Shift"] = ""

    index = 0

    for _, row in optimized.iterrows():

        shift = row["Shift"]

        workers = int(row["Experts"])

        for _ in range(workers):

            if index >= len(staff):
                break

            staff.loc[index, "Shift"] = shift

            index += 1

    # -----------------------------
    # Формируем календарь
    # -----------------------------

    schedule = pd.DataFrame()

    schedule["Group"] = staff["Группа"]

    schedule["Employee"] = staff["Эксперт"]

    schedule["Shift"] = staff["Shift"]

    # Смещения циклов по группам
    patterns = {}

    groups = schedule["Group"].unique()

    base_patterns = [[0, 1], [2, 3], [1, 2], [3, 0]]

    for i, group in enumerate(groups):
        patterns[group] = base_patterns[i % len(base_patterns)]

    for day in range(1, 32):

        schedule[str(day)] = ""

        for i in range(len(schedule)):

            shift = schedule.loc[i, "Shift"]

            if shift == "":
                schedule.loc[i, str(day)] = ""
                continue

            group = schedule.loc[i, "Group"]

            work_days = patterns[group]

            cycle = (day - 1) % 4

            if cycle in work_days:
                schedule.loc[i, str(day)] = shift
            else:
                schedule.loc[i, str(day)] = "Выходной"

    schedule.to_excel(project / "reports" / "schedule.xlsx", index=False)

    return schedule


if __name__ == "__main__":
    result = build_schedule()

    print(result.head())
