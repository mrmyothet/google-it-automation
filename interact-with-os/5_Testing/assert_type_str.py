word_list = ["east", "after", "up", "over", "inside"]


def OrganizeList(myList):
    for item in myList:
        assert type(item) == str, "Word list must be as list of strings"
    myList.sort()
    return myList


print(OrganizeList(word_list))

my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))
