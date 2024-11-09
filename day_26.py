# NATO Alphabet Project

import pandas

data = pandas.read_csv("day_26_nato_phonetic_alphabet.csv")

data_dict={row.letter:row.code for (index,row) in data.iterrows()}

user_input=input("Enter a word : ").upper()
output=[data_dict[char] for char in user_input]

print(output)