from pathlib import Path
import math
import pandas as pd
from analyze_load import analyze_load

AHT = 690
MAX_CHATS = 2


def calculate_staff():
    # -----------------------------
    # Загружаем почасовую нагрузку
    # -----------------------------
    hourly_load = analyze_load()
    # -----------------------------
    # Производительность эксперта
    # -----------------------------
    chats_per_hour = (3600 / AHT) * MAX_CHATS
    # -----------------------------
    # Требуемое количество экспертов
    # -----------------------------
    hourly_load["Required_Experts"] = (hourly_load["Chats"] / chats_per_hour).apply(
        math.ceil
    )
    # -----------------------------
    # Сохраняем
    # -----------------------------
    project_path = Path(__file__).resolve().parent.parent
    output = project_path / "reports" / "required_staff.xlsx"
    hourly_load.to_excel(output, index=False)
    return hourly_load


if __name__ == "__main__":
    result = calculate_staff()
    print(result.head(30))
