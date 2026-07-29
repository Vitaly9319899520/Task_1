from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_load():

    project = Path(__file__).resolve().parent.parent

    df = pd.read_excel(project / "reports" / "required_staff.xlsx")

    # Максимальная нагрузка по каждому часу
    hourly = (
        df.groupby("Hour")
        .agg(Chats=("Chats", "max"), Experts=("Required_Experts", "max"))
        .reset_index()
    )

    # ---------- график нагрузки ----------

    plt.figure(figsize=(12, 6))

    plt.plot(hourly["Hour"], hourly["Chats"], marker="o", linewidth=2)

    plt.title("Количество обращений по часам")

    plt.xlabel("Час")

    plt.ylabel("Число чатов")

    plt.grid(True)

    plt.xticks(range(24))

    plt.tight_layout()

    plt.savefig(project / "reports" / "hourly_load.png")

    plt.close()

    # ---------- график экспертов ----------

    plt.figure(figsize=(12, 6))

    plt.plot(hourly["Hour"], hourly["Experts"], marker="o", linewidth=2)

    plt.title("Требуемое количество экспертов")

    plt.xlabel("Час")

    plt.ylabel("Эксперты")

    plt.grid(True)

    plt.xticks(range(24))

    plt.tight_layout()

    plt.savefig(project / "reports" / "required_experts.png")

    plt.close()

    print("Графики построены.")
