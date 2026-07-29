from pathlib import Path
import pandas as pd
from src.load_data import load_chat_history


def analyze_load():
    # ----------------------------
    # Загружаем историю обращений #
    # ----------------------------
    chats = load_chat_history()
    # ----------------------------
    #  Преобразуем дату-время
    #  ----------------------------
    chats["DateTimeStart"] = pd.to_datetime(
        chats["DateTimeStart"], format="%d%b%Y:%H:%M:%S.%f"
    )
    # ----------------------------
    #  Получаем дату
    # ----------------------------
    chats["Date"] = chats["DateTimeStart"].dt.date
    # ----------------------------
    # Получаем час
    # ----------------------------
    chats["Hour"] = chats["DateTimeStart"].dt.hour
    # ----------------------------
    # Считаем количество обращений
    # ----------------------------
    hourly_load = chats.groupby(["Date", "Hour"]).size().reset_index(name="Chats")
    # ----------------------------
    # Сохраняем результат
    # ----------------------------
    project_path = Path(__file__).resolve().parent.parent
    output = project_path / "reports" / "hourly_load.xlsx"
    hourly_load.to_excel(output, index=False)
    return hourly_load


if __name__ == "__main__":
    result = analyze_load()
    print(result.head(20))
