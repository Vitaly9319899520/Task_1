from pathlib import Path

import pandas as pd

from src.calculate_staff import calculate_staff
from src.create_shift_matrix import create_shift_matrix
from src.optimize_schedule import optimize_schedule


def coverage_check():
    required = calculate_staff()

    matrix = create_shift_matrix()

    shifts = optimize_schedule()

    # Максимальная потребность по каждому часу
    required = (
        required.groupby("Hour")["Required_Experts"]
        .max()
        .reindex(range(24), fill_value=0)
    )

    fact = []

    for hour in range(24):

        workers = 0

        for i in matrix.index:
            workers += matrix.loc[i, hour] * shifts.loc[i, "Experts"]

        fact.append(workers)

    result = pd.DataFrame(
        {"Hour": range(24), "Required": required.values, "Scheduled": fact}
    )

    result["Difference"] = result["Scheduled"] - result["Required"]

    project = Path(__file__).resolve().parent.parent

    result.to_excel(project / "reports" / "coverage_check.xlsx", index=False)

    return result


if __name__ == "__main__":
    print(coverage_check())
