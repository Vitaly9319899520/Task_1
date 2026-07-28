from pathlib import Path

import pandas as pd
import pulp

from calculate_staff import calculate_staff
from create_shift_matrix import create_shift_matrix


def optimize_schedule():
    # -------------------------
    # Загружаем необходимые данные
    # -------------------------

    required = calculate_staff()

    matrix = create_shift_matrix()

    # -------------------------
    # Берем максимальную нагрузку
    # по каждому часу
    # -------------------------

    hourly_need = (
        required.groupby("Hour")["Required_Experts"]
        .max()
        .reindex(range(24), fill_value=0)
    )

    # -------------------------
    # Создаем модель
    # -------------------------

    model = pulp.LpProblem("ChatSupportScheduling", pulp.LpMinimize)

    # -------------------------
    # Переменные
    # -------------------------

    shifts = {}

    for i in matrix.index:
        shifts[i] = pulp.LpVariable(f"Shift_{i}", lowBound=0, cat="Integer")

    # -------------------------
    # Целевая функция
    # -------------------------

    model += pulp.lpSum(shifts[i] for i in matrix.index)

    # -------------------------
    # Ограничения
    # -------------------------

    for hour in range(24):
        model += (
            pulp.lpSum(shifts[i] * matrix.loc[i, hour] for i in matrix.index)
            >= hourly_need.loc[hour]
        )

    # -------------------------
    # Решение
    # -------------------------

    model.solve()

    # -------------------------
    # Результат
    # -------------------------

    result = matrix[["Type", "Shift"]].copy()

    result["Experts"] = [int(shifts[i].value()) for i in matrix.index]

    # -------------------------
    # Сохраняем
    # -------------------------

    project = Path(__file__).resolve().parent.parent

    output = project / "reports" / "optimized_shifts.xlsx"

    result.to_excel(output, index=False)

    return result


if __name__ == "__main__":
    df = optimize_schedule()

    print(df)
