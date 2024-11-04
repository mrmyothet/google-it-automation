import subprocess

result = subprocess.Popen(
    ["echo", "Hello from popen!"], stdout=subprocess.PIPE, text=True
)
output, _ = result.communicate()
print(output)
