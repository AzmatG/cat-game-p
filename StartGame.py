import questionary
from cprint import cprint
from art import text2art
cat_attributes = {
    'intelligence' : 5,
    'hunger' : 0,
    'happiness' : 5,
    'energy' : 5,
    }   
def StartGame(name):
    choice = questionary.select(
        f"What would you like to do with {name}?",
        choices=[f"Play with {name}!", f"Train {name}!", f"Feed {name}", f"Tuck {name} into bed!", f"View {name}'s stats"],
    ).ask()
    if choice == f"Play with {name}!":
        if cat_attributes["energy"] > 0 or cat_attributes["hunger"] < 5:
            cprint(f"You played with {name}", c = "m")
            cprint("Happiness +1", c = "g")
            cprint("Energy -1\nHunger +1", c = "r")
            cat_attributes["happiness"] += 1
            cat_attributes["energy"] -= 1
            cat_attributes["hunger"] += 1
            return StartGame(name)
        elif cat_attributes["energy"] > -5 or cat_attributes["hunger"] < 10:
            cprint(f"{name} doesnt feel like playing right now...\nI wonder whats wrong?\nEnergy -1\nHunger +1", c = "r")
            cat_attributes["energy"] -= 1
            cat_attributes["hunger"] += 1
            return StartGame(name) 
        else:
            cprint(f"{name} has died!, How could you do this!", c = "Br")
            print(text2art("GAME OVER!"))
    if choice == f"Train {name}!":
        if cat_attributes["energy"] > 0 and cat_attributes["hunger"] < 5:
            cprint(f"You trained {name}!", c = "m")
            cprint("Intelligence +1!", c = "g")
            cprint("Energy -=1\nHunger +1!", c = "r")
            cat_attributes["intelligence"] += 1
            cat_attributes["hunger"] += 1
            cat_attributes["energy"] -= 1
            return StartGame(name)
        elif cat_attributes["energy"] > -5 or cat_attributes["hunger"] < 10:
            cprint(f"{name} wasn't up for it...\nEnergy -1\nHunger +1", c = "r")
            cat_attributes["energy"] -= 1
            cat_attributes["hunger"] += 1
            return StartGame(name)
        else:
            cprint(f"{name} didn't want to see your abusive face anymore and spontaneously combusted! How heartless of you!", c = "Br")
            print(text2art("GAME OVER!"))
    if choice == f"Feed {name}":
        if cat_attributes["energy"] < 10 and cat_attributes["hunger"] >= 0:
            cprint(f"{name} feels great!", c = "m")
            cprint("Energy +1", c = "g")
            cprint("Hunger -1", c = "r")
            cat_attributes["energy"] += 1
            cat_attributes["hunger"] -= 1
            return StartGame(name)
        elif cat_attributes["energy"] > 10 or -5 < cat_attributes["hunger"] < 0 :
            cprint(f"{name} is feeling a bit full... She refused to eat it all!\nHunger-1", c = "r")
            cat_attributes["hunger"] -=1
            return StartGame(name)
        else:
            cprint(f"Oh no! {name} ate too much and created her own gravitational orbit!. She is no longer reachable!\nHow could you!", c = "Br")
            print(text2art("GAME OVER!"))
    if choice == f"Tuck {name} into bed!":
        cprint(f"{name} was peacefully put to sleep!", c="m")
        cprint("Energy +2", c = "g")
        cat_attributes["energy"] +=2
        return StartGame(name)
    if choice == f"View {name}'s stats":
        cprint(cat_attributes, c = "Bg")
        return StartGame(name)
