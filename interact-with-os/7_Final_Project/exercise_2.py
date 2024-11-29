import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
sorted_fruit = sorted(fruit.items())
print(sorted_fruit)

sort_by_name = sorted(fruit.items(), key=operator.itemgetter(0))
print(sort_by_name)

sort_by_value = sorted(fruit.items(), key=operator.itemgetter(1))
print(sort_by_value)

reverse_sort_by_value = sorted(fruit.items(), key=operator.itemgetter(1), reverse=True)
print(reverse_sort_by_value)
