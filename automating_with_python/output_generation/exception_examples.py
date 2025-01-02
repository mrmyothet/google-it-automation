# Using try/except

try:
    f = open("/etc/hosts", "w+")
    f.write("Success!")
except FileNotFoundError:
    print("Error: File not found")
except Exception as ex:
    print("Error appending to file: " + str(ex))
else:
    f.close()


# Using raise
def start_server(port):
    if not isinstance(port, int):
        raise TypeError("port must be an integer")
    elif port < 1024 or port > 65535:
        raise ValueError("port must be between 1024 and 65535")


# Using finally
try:
    f = open("/etc/hosts", "w+")
    f.write("Success!")
except:
    print("Error appending to file" + str(ex))
finally:
    f.close()
