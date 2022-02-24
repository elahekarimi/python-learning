import pandas

data = pandas.read_csv("nato_phonetic.csv")
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("enter a word: ").upper()
    try:
        out_list = [phonetic_dic[letter] for letter in word]
    except KeyError:
        print("just enter word")
        generate_phonetic()
    else:
        print(out_list)


generate_phonetic()
