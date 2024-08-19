def hint_username(username):
    if len(username) < 3:
        print("Invalid user name. Must be at least 3 characters long")
    elif len(username) > 15: 
            print("Invalid user name. Must be at most 15 characters long")
    else: 
        print("Valid user name.")

def hint_username2(username):
    if len(username) < 3:
        return "Invalid user name. Must be at least 3 characters long"
    elif len(username) > 15:
        return "Invalid user name. Must be at most 15 characters long"
    else:
        return "Valid user name."


def is_positive(number):
    if(number > 0):
        return True
    else:
        return False
    
def is_even(number):
    if(number % 2 == 0): 
        return True
    return False

hint_username("mt")
hint_username("myothet")
hint_username("mr.myothet@gmail.com")

print(is_positive(-5))
print(is_positive(0))
print(is_positive(13))

print('is_even(19) => ', is_even(19))
print('is_even(20) => ', is_even(20))

print(hint_username2("mt"))