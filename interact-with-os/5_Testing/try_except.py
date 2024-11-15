def character_frequency(filename):
    # First try to open the file
    try:
        f = open(filename)
    except OSError:
        return None

    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters


filename = "/home/myothet/repos/google-it-automation/interact-with-os/4_Manage_Data_Processes/fishy.log"
result = character_frequency(filename)
print(result)
