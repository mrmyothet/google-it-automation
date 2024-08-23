# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20.


# The function accepts a "given_number" variable through its parameters.
def addition_table(given_number):
    iterated_number = 1
    sum = 1
    while iterated_number <= 5:
        sum = given_number + iterated_number

        if sum > 20:
            break

        print(str(given_number), "+", str(iterated_number), "=", str(sum))
        iterated_number += 1


addition_table(5)
addition_table(17)
addition_table(21)
