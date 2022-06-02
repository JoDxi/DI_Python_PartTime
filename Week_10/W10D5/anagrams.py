import anagram_checker


def main_menu():
    ask_input = True
    while ask_input:
        print("""
            --CHECK YOUR ANAGRAM--
                 Choose the following:
                 (1) Input a word
                 (2) Cancel
            """)
        user_input = input("Enter your choice: ")
        if user_input == "1":
            event = anagram_checker.AnagramChecker()
            check_valid = event.is_valid_word()
            if check_valid:
                event.get_anagrams()
                break
        elif user_input == "2":
            print("Bye bye")
            break


main_menu()
