


def processing(date_str):
    day, month, year = map(int, date_str.split('-'))
    return (year, month, day)

def quick_sort(dates):
    if len(dates) <= 1:
        return dates
    else:
        pivot = dates.pop()
        pivot_tuple = processing(pivot)
        greater, lesser = [], []
        
        for date in dates:
            if processing(date) <= pivot_tuple:
                lesser.append(date)
            else:
                greater.append(date)
        
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


n = int(input())
dates = [input() for i in range(n)]

sorted_dates = quick_sort(dates)
for date in sorted_dates:
    print(date)


# s = '01-12-2000'
# s1 = '31-10-2000'
# print(processing(s) < processing(s1))
