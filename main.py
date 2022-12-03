import pandas

alpha_data = pandas.read_csv(
    "/Users/wanice/Documents/GitHub/NATO-alphabet/nato_phonetic_alphabet.csv")


alpha_dict = {row.letter: row.code for (index, row) in alpha_data.iterrows()}


print(alpha_dict)
print(alpha_dict.keys())

guess = input("Kindly input a letter: ").upper()
newt = []
for char in guess:
    if char in alpha_dict.keys():
        newt.append(alpha_dict.get(char))
print(newt)