import pandas as pd

from src.load_shifts import prepare_shifts


def is_working(hour, start, end):
    """Проверяет,
    работает ли смена
    в указанный час.
    """

    # обычная дневная смена

    if start < end:
        return start <= hour < end

    # ночная смена

    else:
        return hour >= start or hour < end


def create_shift_matrix():
    shifts = prepare_shifts()

    matrix = []

    # перебираем смены

    for _, row in shifts.iterrows():

        line = []

        # проверяем каждый час

        for hour in range(24):
            line.append(int(is_working(hour, row["Start"], row["End"])))

        matrix.append(line)

    # превращаем список в DataFrame

    matrix = pd.DataFrame(matrix, columns=range(24))

    # добавляем информацию о смене

    matrix.insert(0, "Shift", shifts["Shift"])

    matrix.insert(0, "Type", shifts["Type"])

    return matrix


if __name__ == "__main__":
    df = create_shift_matrix()

    print(df)
