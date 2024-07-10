import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def convert_nato():
    word = input("Enter a word: ").upper()
    try:
        word_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the alphabet please:")
        convert_nato()
    else:
        print(word_list)


convert_nato()
