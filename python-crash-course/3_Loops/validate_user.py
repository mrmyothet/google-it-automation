def get_username():
    username = input("enter user name : ")
    return username


def validate_user(name):
    return name == "myothet"


user_name = get_username()
while not validate_user(user_name):
    print("Invalid user name")
    user_name = get_username()
