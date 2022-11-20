import phase1
import articles
import authors
import venues


def main():
    print("To search for an article enter 'A'"
          "To search for an author enter 'U'"
          "To list venues within a range enter 'V' "
          "To add an article enter 'R'"
          "To quit enter 'Q'")
    done = False
    while not done:
        uI = input("> ").lower().strip()
        if uI == 'a':
            pass
        elif uI == 'u':
            pass
        elif uI == 'v':
            pass
        elif uI == 'r':
            pass
        elif uI == 'q':
            print("Exiting program...")
            print("Goodbye")
            done = True
        else:
            print("Invalid input, try again.")
            uI = input("> ").lower().strip()

    return


main()
