def record_profit_years(recent_first, recent_last):
    recent_first.reverse()

    recent_last.extend(recent_first)

    return recent_last


recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

print(record_profit_years(recent_first, recent_last))
# Should print [1989, 1992, 1997, 2001, 2006, 2011, 2018, 2022]


def list_years(start, end):
    return [year for year in range(start, end + 1)]


print(list_years(1972, 1975))
# Should print [1972, 1973, 1974, 1975]


def odd_numbers(x, y):
    return [n for n in range(x, y) if n % 2 != 0]


print(odd_numbers(5, 15))
# Should print [5, 7, 9, 11, 13]
