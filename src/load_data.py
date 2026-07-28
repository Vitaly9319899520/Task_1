from pathlib import Path
import pandas as pd


def load_chat_history():
    """Загружает историю обращений."""

    project_path = Path(__file__).resolve().parent.parent
    file_path = project_path / "data" / "query.csv"
    df = pd.read_csv(file_path, sep=";", encoding="utf-8")
    # print(df)
    return df


def load_staff():
    """Загружает список сотрудников."""

    project_path = Path(__file__).resolve().parent.parent
    file_path = project_path / "data" / "source.xlsx"
    df = pd.read_excel(file_path, sheet_name="Список экспертов")
    # print(df)
    return df


def load_shifts():
    """Загружает список смен."""

    project_path = Path(__file__).resolve().parent.parent
    file_path = project_path / "data" / "source.xlsx"
    df = pd.read_excel(file_path, sheet_name="Смены")
    # print(df)
    return df


# load_staff()
# load_shifts()
# load_chat_history()
