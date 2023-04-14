print("Welcome!!\nThis app is used to replace letters in a phrase with\na given set of rules")
print(".....................................................................................\nEnjoy yourself!!\n\n")


def translate(phrase, library, replacement):
    translation = ""
    for letter in phrase:
        if letter in library:
            translation = translation + str(replacement)
        else:
            translation = translation + letter
    return translation


while True:
    try:
        user_phrase = str(input("Enter your phrase: "))
        user_library = str(input("Compare it to: "))
        user_replacement = str(input("Replace them with: "))
        result = str(translate(user_phrase, user_library, user_replacement))
        print(".............................\nHere is your translation: " + result + "\n")

        choice = str(input("Make a new prompt:\ny or n: "))
        if choice.lower() == "y":
            print("\n")
        else:
            print("\nOkay, Thanks for using my Application!!")
            break

    except ValueError:
        print("Oops invalid input")
