# Mail Merge

with open("./day_24_Input/Names/invited_names.txt") as file:
    name=file.readlines()
    for i in range (0,len(name)):
        name[i]=name[i].strip()

with open("./day_24_Input/Letters/starting_letter.txt") as file:
    letter=file.readlines()
    change="[name]"
    for i in range (0,len(name)):
        letter[0]=letter[0].replace(change,name[i])
        with open(f"./day_24_Output/ReadyToSend/{name[i]}.txt", "w") as file:
            file.writelines(letter)
        change=name[i]
