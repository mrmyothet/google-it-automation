# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(4))


def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result


factorial(4)

# The function should return the sum of all positive numbers between the number n received and 1.
# For example, when n is 3 it should return 1+2+3=6,
# and when n is 5 it should return 1+2+3+4+5=15.


def sum_positive_numbers(n):
    # The base case if n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)


print(sum_positive_numbers(3))
print(sum_positive_numbers(5))

# factorial(1000)
# RecursionError: maximum recursion depth exceeded

# these activities are good use cases for recursive programs
# - Going through a file system collecting information related to directories and files.
# - Managing permissions assigned to groups inside a company,
#   when each group can contain both subgroups and users.


def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        print(number)
        return number == 1

    # Recursive case: keep dividing number by base.
    print("Calling again with " + str(number))
    return is_power_of(number / base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False


# Recursion is a process where a function calls itself one or more times with modified values to accomplish a task.
# This technique can be particularly effective
# when solving complex problems that can be broken down into smaller, simpler problems of the same type.
# the count_users function uses recursion to count the number of users that belong to a group within a company's system.
# It does this by iterating through each member of a group, and if a member is another group,
# it recursively calls count_users to count the users within that subgroup.

# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     count += 1
#     if is_group(member):
#       count += count_users(member)
#   return count

# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18

# def count_users(group):
#   count = 0
#   for member in get_members(group):
#     if is_group(member):
#       count += count_users(member)
#     else: count += 1
#   return count


# print(count_users("sales")) # Should be 3
# print(count_users("engineering")) # Should be 8
# print(count_users("everyone")) # Should be 18
