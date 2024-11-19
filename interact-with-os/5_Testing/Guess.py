import random


def Guess(participants):
    try:
        my_participant_dict = {}
        for participant in participants:
            my_participant_dict[participant] = random.randint(1, 9)

        if my_participant_dict["Larry"] == 9:
            return True
        else:
            return False
    except KeyError:
        return None


participants = ["Jack", "Jill", "Larry", "Tom"]
print(Guess(participants))

participants = ["Cathy", "Fred", "Jack", "Tom"]
print(Guess(participants))
