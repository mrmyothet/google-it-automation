import subprocess

result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)
print(result.stdout.strip())

result = subprocess.call(["echo", "Hello from call!"])
print(result)

result = subprocess.check_call(["echo", "Hello from check_call!"])
print(result)

result = subprocess.check_output(["echo", "Hello from check_output!"])
print(result.strip())
