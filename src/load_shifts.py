from src.load_data import load_shifts as load_shift_table


def prepare_shifts():
    """Загружает смены и преобразует время начала и окончания."""

    shifts = load_shift_table()
    # Переименуем столбцы для удобства
    shifts.columns = ["Type", "Shift"]
    # Разделяем строку 07:00-19:00
    shifts[["Start", "End"]] = shifts["Shift"].str.split("-", expand=True)
    # Оставляем только часы
    shifts["Start"] = shifts["Start"].str[:2].astype(int)
    shifts["End"] = shifts["End"].str[:2].astype(int)
    # Длительность смены
    shifts["Duration"] = 12
    return shifts


if __name__ == "__main__":
    shifts = prepare_shifts()

    print(shifts)
