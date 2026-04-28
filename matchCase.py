number = int(input("enter number: 2"))
"""match-case is python version of switch case statements"""
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")