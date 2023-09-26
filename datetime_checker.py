import tkinter.messagebox as messagebox


def is_correct_format(day, month, year):
    try:
        day = int(day)
    except ValueError:
        messagebox.showerror("Error", "Input data for Day is incorrect format!")
        return {'message': f"Input data for Day is incorrect format!", 'status': False}

    try:
        month = int(month)
    except ValueError:
        messagebox.showerror("Error", "Input data for Month is incorrect format!")
        return {'message': f"Input data for Month is incorrect format!", 'status': False}

    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("Error", "Input data for Year is incorrect format!")
        return {'message': f"Input data for Year is incorrect format!", 'status': False}

    return {'message': f"Input data is correct format!", 'status': True}


def is_valid_range(day, month, year):
    day, month, year = int(day), int(month), int(year)
    if day < 1 or day > 31:
        return {'message': f"Input data for Day is out of range!", 'status': False}
    elif month < 1 or month > 12:
        return {'message': f"Input data for Month is out of range!", 'status': False}
    elif year < 1000 or year > 3000:
        return {'message': f"Input data for Year is out of range!", 'status': False}
    return {'message': f"Input data is in range!", 'status': True}


def day_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28


def is_valid_date(day, month, year):
    day, month, year = int(day), int(month), int(year)
    if 1 <= month <= 12 and 1 <= day <= day_in_month(year, month):
        return True
    return False


def check_date(day, month, year):
    date_format = is_correct_format(day, month, year)
    if not date_format['status']:
        return date_format

    date_range = is_valid_range(day, month, year)
    if not date_range['status']:
        return date_range

    if is_valid_date(day, month, year):
        return {'message': f"{day}/{month}/{year} is a correct date time!", 'status': True}
    else:
        return {'message': f"{day}/{month}/{year} is an incorrect date time!", 'status': False}