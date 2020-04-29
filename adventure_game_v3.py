import time
import random
items = []

# Function for pausing text
def messagePause(message):
  print(message)
  #time.sleep(2)

enemy_list = ["pirate", "wicked fairie", "gorgon"]
enemy = random.choice(enemy_list)
print(message, enemy)


# GAME INTRO
def intro():
  messagePause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
  messagePause("Rumor has it that a is somewhere around here, and has been terrifying the nearby village.")
  messagePause("In front of you is a house.")
  messagePause("To your right is a dark cave.")
  messagePause("In your hand you hold your trusty (but not very effective) dagger.")

# HOUSE INTRO
def house_intro():
  messagePause("You approach the door of the house.")
  messagePause("You are about to knock when the door opens and out steps a gorgon")
  messagePause("Eep! This is the gorgon's house!")
  messagePause("The gorgon attacks you!")

# DOOR / HOUSE LOSE BATTLE
def house_lose():
  messagePause("You feel a bit under-prepared for this, what with only having a tiny dagger.")

# CAVE / GETS SWORD
def cave_gets_sword():
  messagePause("You peer cautiously into the cave.")
  messagePause("It turns out to be only a very small cave.")
  messagePause("Your eye catches a glint of metal behind a rock.")
  messagePause("You have found the magical Sword of Ogoroth!")
  messagePause("You discard your silly old dagger and take the sword with you.")
  messagePause("You walk back out to the field.")

# CAVE / ALREADY HAS SWORD
def cave_has_sword():
  messagePause("You peer cautiously into the cave.")
  messagePause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
  messagePause("You walk back out to the field.")

# DOOR / HOUSE LOSE FIGHT
def fight_lose():
  messagePause("You do your best...")
  messagePause("but your dagger is no match for the gorgon.")
  messagePause("You have been defeated!")

# DOOR / HOUSE WIN FIGHT
def fight_win():
  messagePause("As the gorgon moves to attack, you unsheath your new sword.")
  messagePause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
  messagePause("But the gorgon takes one look at your shiny new toy and runs away!")
  messagePause("You have rid the town of the gorgon. You are victorious!")

# RUNAWAY
def run_away():
  messagePause("You run back into the field. Luckily, you don't seem to have been followed.")


# PLAY AGAIN USER INPUT VALIDATION
def play_again_input(play_again_message,options):
  while True:
    options = ["y", "n"]
    response = input(play_again_message).lower()
    for option in options:
      if option in response:
        return response
    print("Please select a valid input")

#PLAY AGAIN
def play_again():
  answer = play_again_input("Would you like to play again? Y/N \n", "")
  if "y" in answer:
    print("Excellent! Restarting the game ..")
    intro()
    main_function()
    # call random.choice function for enemy -> for random.choide(enemy)
  elif "n" in answer:
    print("Thanks for playing! See you next time.")
    
# gets number input
def number_input(message, values):
  number = input(message)
  if values in number:
      return number

def house(): 
  house_intro()
  # que quieres hacer? pelear o huir?
  choice = number_input("Would you like to (1) fight or (2) run away?","")
  if choice == "1":
   if "sword" in items:
    fight_win()
    play_again()
   else: # el jugador pierde
    fight_lose()
    play_again()
  elif choice == "2":
    # SUB 2 huir - el usuario vuelve al campo
    run_away()
    main_function()


def cave():
  # recibe instruciones de 1 para casa 2 para cueva
  if "sword" in items:
    cave_has_sword()
    main_function()
  else:
    cave_gets_sword()
    items.append("sword")
    main_function()

def main_function():
  # recibe instruciones de 1 para casa 2 para cueva
  choice = number_input("Enter 1 to knock on the door of the house.\n" "Enter 2 to peer into the cave.\n" 
  "What would you like to do?\n" "(Please enter 1 or 2.)\n", "")
  if choice == "1":
    house()
  elif choice == "2":
    cave()
  else:
    messagePause("please enter valid input")
  
intro()
main_function()