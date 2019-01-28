# this program is cursed, please leave while you still can
import random

def main():
    print_header()
    uwu_text = input("what text awe you putting in\n>>>").strip().lower()
    print(uwu(uwu_text))


def print_header():
    print("--------------------------")
    print("")
    print("     uwu genewatow")
    print("(please leave this program its so bad)")
    print("--------------------------")

# cursed begins after this line
def uwu(text):
    modifiers = ["uwu", "owo", "UWU", "OWO"]
    while text.find("l") != -1:
        spot = text.find("l")
        text_1 = text[:spot]
        text_2 = text[spot+1:]
        text = "{}w{}".format(text_1, text_2)
    while text.find("r") != -1:
        spot = text.find("r")
        text_1 = text[:spot]
        text_2 = text[spot+1:]
        text = "{}w{}".format(text_1, text_2)
    return "{} {}".format(text, random.choice(modifiers))


if __name__ == "__main__":
    main()
