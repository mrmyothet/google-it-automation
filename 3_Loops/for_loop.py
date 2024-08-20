for x in range(5):
    print(x)

print("")

friends = ["Taylor", "Alex", "Pat", "Eli"]
for friend in friends:
    print("Hi " + friend)

print("")

values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print(values)
print("Total :", sum)
print("Average :", str(sum / length))
