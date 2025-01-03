def translate_error_code(error_code):
    if error_code == "401 Unauthorized":
        translation = "Server received an unauthorized request"
    elif error_code == "404 Not Found": 
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout": 
        translation = "Server request to close unused connection"
    else: 
        translation = "Unknown error code"
    return translation

def round_up(number):
    x = 10
    whole_number = number // x
    remainder = number % x
    if remainder >= 5:
        return x*(whole_number+1)
    return x*whole_number

print(translate_error_code("404 Not Found"))

number = 25

if number <= 5:
    print("The number is 5 or smaller.")
elif number == 33:
    print("The number is 33.")
elif number < 32 and number >= 6:
    print("The number is less than 32 and greater than 6.")
else:
    print("The number is " + str(number))

print(round_up(35))