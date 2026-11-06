def next_birthday(date, birthdays):
    birthday_dates = []

    for bday in birthdays:
        if bday > date:
            birthday_dates.append(bday)

    if birthday_dates:
        birthday = min(birthday_dates)
        list_of_names = birthdays[birthday]
    else:
        birthday = min(birthdays)
        list_of_names = birthdays[birthday]

    return birthday, list_of_names
