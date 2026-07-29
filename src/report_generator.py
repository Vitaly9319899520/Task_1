from pathlib import Path

import pandas as pd

from src.build_schedule import build_schedule
from src.coverage_check import coverage_check
from src.optimize_schedule import optimize_schedule
from src.plot_load import plot_load


def create_report():
    project = Path(__file__).resolve().parent.parent

    schedule = build_schedule()

    coverage = coverage_check()

    optimized = optimize_schedule()

    plot_load()

    report = project / "reports" / "Final_Report.xlsx"

    with pd.ExcelWriter(report) as writer:
        optimized.to_excel(writer, sheet_name="Оптимальные смены", index=False)

        schedule.to_excel(writer, sheet_name="График", index=False)

        coverage.to_excel(writer, sheet_name="Проверка покрытия", index=False)

    print("Отчет сформирован.")


if __name__ == "__main__":
    create_report()
