"""
Name: Rouan Chen
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ get a single uppercase letter, A, B,or C from the user with input validation. """
    while True:
        text = input("Give an single uppercase letter: ")
        if len(text) != 1:
            print("Error: it needs to be s single character.")
            continue
        if text not in ["A", "B", "C"]:
            print("Error: You proovided the wrong character.")
            continue
        return text

def get_digit():
    """ get a single digit 1, 2, or 3 from the user with input validation """
    while True:
        text = input("Give an single number character: ")
        if not text.isdigit():
            print("Error: your input should be only digits.")
            continue
        if text not in ["1", "2", "3"]:
            print("Error: a single digit needs to be i [1,3].")
            continue
        return text


def check_pattern(letter, digit, lst):
    """ Check the list of strings for words containing letter followed by digit, and print them. """
    print("Strings with the pattern:")
    matched_words = []
    
    for word in lst:
        found_letter_first = False
        match_found = False
        
        for ch in word:
            if not found_letter_first and ch == letter:
                found_letter_first = True
            elif found_letter_first and ch ==digit:
                match_found = True
                break
        if match_found:
            if word not in matched_words:
                matched_words.append(word)
                
    for word in matched_words:
        print(word, end=" ")
    print()


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
        
        choice = input("Try Again? (y/n): ")
        if choice != 'y':
            break

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()