# for satisfying the condition initialize choice as y
choice = 'y'

while choice == 'y' or choice == 'Y':

    # taking input from user
    print("Enter a string ::: ", end=" ")
    string = input()

    # initialize new_string as empty string for storing non unicode characters
    new_string = ""
    # initialize remove_char as empty string for storing unicode characters
    remove_char = ""
    print()

    # it will iterate every character in string
    for character in string:
        # it will check if characters are alphanumeric
        # for removing special characters
        if character.isalnum():
            new_string = new_string + character
        else:
            remove_char = remove_char + character

    # encode the string into ‘ASCII’ and error as ‘ignore’ to remove Unicode characters
    string_encode = new_string.encode(encoding='ascii', errors='ignore')
    #  decode the string back in its form
    string_decode = string_encode.decode(encoding='ascii', errors='ignore')

    # for printing output
    if new_string == "":
        print("The string is empty all characters are unicode characters")
        print("The removed unicode characters are : ", remove_char)

    elif remove_char == "":
        print("There are no unicode characters in a given {} string ".format(string))

    else:
        print("After removing unicode characters the string is : ", string_decode)
        print("The removed unicode characters are : ", remove_char)

    print()

    # taking input from user if they want to remove the unicode character again
    choice = input("Do you want to remove Unicode characters again press y else n : ")

    # if user entered wrong input
    while choice != 'y' and choice != 'Y' and choice != 'n' and choice != 'N':
        print("Invalid input try again !")
        choice = input("Do you want to remove Unicode characters again press y else n : ")

    print()
