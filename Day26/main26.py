import pandas
data = pandas.read_csv("nato_phonetic.csv")
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("enter a word: ").upper()
out_list = [phonetic_dic[letter] for letter in word]
print(out_list)