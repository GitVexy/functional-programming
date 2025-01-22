def sort_dates(dates):
    return sorted(dates, key = sorter)

def sorter(date):
    month, day, year = date.split("-")
    return year, month, day