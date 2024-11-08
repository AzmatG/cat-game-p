import questionary
from art import text2art
from cprint import cprint
from StartGame import StartGame

cat_attributes = {
    'intelligence' : 5,
    'hunger' : 0,
    'happiness' : 5,
    'energy' : 5,
    }   
Art = text2art("Welcome!")
print(Art)
cprint("Welcome to The Cat Game! The best cat raising simulator in the world!\nPlease press start to get started!", c="r")
choice = questionary.select(
    "Please press start to get started!",
    choices = [
        "Start",
        "Maybe later..."
    ]
).ask()
if choice == "Start":
    cprint("Welcome to your own cat simulator! Before we begin, answer these short questions...", c = "m")
    name = questionary.text("What name would you like to give to your cat").ask().capitalize()
    Art = text2art("Have fun!")
    print(Art)
    StartGame(name)
    running = True
    while running:
        StartGame(name) 
else:
    cprint("I see... Hope to see you later!", c = "g")
        



