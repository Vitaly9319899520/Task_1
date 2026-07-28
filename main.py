from src.load_data import load_chat_history, load_staff, load_shifts


def main():
    chats = load_chat_history()
    staff = load_staff()
    shifts = load_shifts()
    print("История обращений")
    print(chats.head())
    print()
    print("Сотрудники")
    print(staff.head())
    print()
    print("Смены")
    print(shifts.head())


if __name__ == "__main__":
    main()
