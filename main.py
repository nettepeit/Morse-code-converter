import pandas as pd

data = pd.read_csv("morse.csv", names=["char", "code"], index_col=0)


def to_morse():
    all_chars = data.index.to_list()
    text = input("Write your text here: ")
    text_list = list(text.upper())
    morse_text = []
    for char in text_list:
        if char in all_chars:
            char_loc = data[data.index == char]
            char_val = char_loc.values[0].tolist()
            morse_text.append(char_val)
        elif char.isspace():
            morse_text.append(" ")

    morse_sentence = " ".join([" ".join([str(c) for c in lst]) for lst in morse_text])
    print(f"Your text in morse code: {morse_sentence}")


def to_text():
    all_codes = data.values.tolist()
    codes_list = []
    for code in all_codes:
        for c in code:
            codes_list.append(c)
    morse = input("Write your Morse code here, please put 2 spaces between words: ")
    morse_list = list(morse.split(" "))
    sentence = []
    for code in morse_list:
        if code in codes_list:
            code_loc = data[data.values == code]
            code_val = code_loc.index
            sentence.append(code_val)
        elif code == "":
            sentence.append(" ")

    text_sentence = "".join(["".join([str(c) for c in lst]) for lst in sentence])
    print(f"Your morse code in text: {text_sentence.lower()}")


is_on = True
while is_on:
    answer = input("For Text to Morse write TM: \nFor Morse to Text write MT: \nTo stop write EXIT: ")
    if answer == "TM":
        to_morse()
    elif answer == "MT":
        to_text()
    elif answer == "EXIT":
        is_on = False
    else:
        print("Please write a valid input.")
