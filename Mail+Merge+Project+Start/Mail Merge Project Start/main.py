#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()


for name in names:
    name = name.strip()
    with open("Input/Letters/starting_letter.txt") as file:
        new_letter = file.readlines()
    with open(f"Output/{name}.txt", mode="w") as file:
        new_letter[0] = new_letter[0].replace("[name]", name)
        for line in new_letter:
            file.write(line)
