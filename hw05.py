"""
Name: tfernsler
Peers: (add any collaborators)
References: w3schools.com
"""

"""
plan
1. get letter
2. get number
3. concatenate into new_var
4. check for new_var in list

"""


def get_letter():
    """ gets letter A, B, or C from user """
    lsti = ["A", "B", "C"]
    while True:
        letter = input("Give me an single uppercase letter: ")
        if len(letter) > 1:
            print("Error: it needs to be a single character.")
            continue
        elif not letter in lsti:
            print("Error: You provided the wrong character.")
            continue
        else:
            break
    return letter

def get_digit():
    """ Gets digit 1, 2, or 3 from user """
    losti = ["1", "2", "3"]
    while True:
        digit = input("Give an single number character: ")
        if not digit.isdigit() == True:
            print("Error: your input should be only digits.")
            continue
        elif not digit in losti:
            print("Error: a single digit needs to be in [1, 3].")
            continue
        else:
            break
    return digit


def check_pattern(letter, digit, lst):
    """ checks if input from users is in st_list """
    ligit = letter+digit
    print("Strings with the pattern:")
    for i in lst:
        if ligit in i:
            print(i)
        elif letter+"@"+digit in i:
            #for j in len(i):
            print(i)
        else:
            pass
    print("")
                 


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    while True:
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter, digit, st_list)
        i = input("Try Again? (y/n): ")
        if i == "y":
            continue
        else:
            break

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()