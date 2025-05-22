import datetime

# Электронное табло (7-сегментный стиль)
digit_display = {
    '0': [" *** ",
          "*   *",
          "*   *",
          "*   *",
          " *** "],
    '1': ["  *  ",
          " **  ",
          "  *  ",
          "  *  ",
          " *** "],
    '2': [" *** ",
          "*   *",
          "   * ",
          "  *  ",
          "*****"],
    '3': ["*****",
          "    *",
          " *** ",
          "    *",
          "*****"],
    '4': ["   * ",
          "  ** ",
          " * * ",
          "*****",
          "   * "],
    '5': ["*****",
          "*    ",
          "**** ",
          "    *",
          "**** "],
    '6': [" *** ",
          "*    ",
          "**** ",
          "*   *",
          " *** "],
    '7': ["*****",
          "    *",
          "   * ",
          "  *  ",
          " *   "],
    '8': [" *** ",
          "*   *",
          " *** ",
          "*   *",
          " *** "],
    '9': [" *** ",
          "*   *",
          " ****",
          "    *",
          " *** "],
    '.': ["     ",
          "     ",
          "     ",
          "     ",
          "  *  "],
    ' ': ["     ",
          "     ",
          "     ",
          "     ",
          "     "],
}

# Получение даты рождения от пользователя
def get_birth_date():
    day = int(input("Введите день рождения (1-31): "))
    month = int(input("Введите месяц рождения (1-12): "))
    year = int(input("Введите год рождения (напр., 2000): "))
    return datetime.date(year, month, day)

# Определение дня недели
def get_weekday(birth_date):
    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return weekdays[birth_date.weekday()]

# Проверка на високосный год
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Определение возраста
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year
    if (birth_date.month, birth_date.day) > (today.month, today.day):
        age -= 1
    return age

# Печать цифр в стиле электронного табло
def print_date_in_display_style(date):
    str_date = date.strftime("%d%m%Y")
    rows = ['' for _ in range(5)]
    for digit in str_date:
        for i in range(5):
            rows[i] += digit_display.get(digit, digit_display[' '])[i] + '  '
    print("Дата рождения в виде электронного табло:
")
    for row in rows:
        print(row)

# Основная функция
def main():
    birth_date = get_birth_date()
    weekday = get_weekday(birth_date)
    leap = is_leap_year(birth_date.year)
    age = calculate_age(birth_date)

    print(f"\nВы родились {birth_date.strftime('%d.%m.%Y')} ({weekday})")
    print(f"Год {birth_date.year} {'високосный' if leap else 'не високосный'}")
    print(f"Вам {age} лет")

    print_date_in_display_style(birth_date)

if __name__ == "__main__":
    main()
