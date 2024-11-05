

cat_attributes = {
    "intelligence": 6,
    "energy": 10,
    "weight": 10,
    # change the inital values above
}

print("Welcome to my Cat Game!")

# Take the user inputs for name and colour:
name = input("\nEnter a name for the cat: ").capitalize()
# ...

# start the while loop
while True:
    # Finish the string below
    option = input(f"What would you like to do? \n1. Play with {name} \n2. Train {name} \n3. Feed {name} \n4. show stats\n")

    if option == '1':
        if cat_attributes["energy"] > 0:
            print(f"You played with {name}...\n...\n...\nThey seemed to be happy!\n")
            cat_attributes["energy"] -= 2
            cat_attributes["weight"] -= 1
        else:
            print(f"{name} spontaneously combusted!\n Oh no!")
            break
    elif option == '2':
        if cat_attributes["energy"] > 0:
            print(f"You trained {name}...\n...\n...\nIt seems they learned a trick!\n")
            cat_attributes["energy"] -= 2
            cat_attributes["intelligence"] += 2
        else:
            print(f"{name} hissed at you!...\n...\nThey doesnt want to do be your pet anymore!.")
            break
            
    elif option == "3":
        
        print(f"You fed {name}...\n...\n...\nThey feels great!\n")
        cat_attributes["weight"] += 1
        cat_attributes["energy"] += 4
    elif option == "4":
        print(f"Here is {name}'s current status:\nEnergy = {cat_attributes["energy"]}\nIntelligence = {cat_attributes["intelligence"]}\nWeight = {cat_attributes["weight"]}\n")
    
    else:
        pass        

    # finish off the if statements below
    if cat_attributes['energy'] <= 0:
        print(f"{name} is now tired.\nTry feeding her!\n")
    elif cat_attributes["weight"] == 15:
        print(f"{name} is feeling a bit full...\n...\n...\n")
    elif cat_attributes["weight"] == 25:
        print(f"{name} can no longer move. She is too heavy!\n...\n...\n")
        break
    elif cat_attributes["intelligence"] == 10:
        print(f"{name} can now perform many tricks!\n")
    elif cat_attributes["intelligence"] == 16:
        print(f"{name} can now converse with you in english! She is very smart!\n")