import random

import random

def rockpaperscissors(user_input, computer_input):
    if((user_input == "paper") & (computer_input == "paper")):
        print("The computer threw paper, Paper and paper in a draw.")
    elif((user_input == "rock") & (computer_input == "rock")):
        print("The computer threw rock, Rock and rock in a draw.")
    elif ((user_input == "scissors") & (computer_input == "scissors")):
        print ("The computer threw scissors, Scissors and scissors in a draw.")
        
    elif((user_input == "rock") & (computer_input == "scissors")) :
       print ("The compter threw scissors. Rock versus scissor, you win!")
    elif((user_input == "scisssors") & (computer_input == "paper")) : 
       print ("The computer threw paper. scissors versus paper, you win!") 
    elif((user_input == "paper") & (computer_input == "rock")) :
       print ("The computer threw rock. paper versus rock, you win!")
    elif((user_input == "scissors") & (computer_input == "rock")):
       print("The computer threw rock. scissors versus rock, computer wins!")
    elif( (user_input == "rock") & (computer_input== "paper")) :  
       print ("The computer threw paper. Rock versus paper, computer wins!") 
    elif((user_input == "paper") & (computer_input == "scissor")) :
       print ("The computer threw scissors. paper versus scissor, computer win")

rock = "rock"
paper = "paper"
scissor = "scissor"
list = [ rock, paper, scissor]

response = input("Would you like to play a game of Rock, Paper, Scissors?: 'Y' for yes, anything else for no:   ").upper()
while response == 'Y':
    computer = random.choice(list)
    user = input ("Rock. Paper. Scissor. Shoot:  ").lower()
    rockpaperscissors(user,computer)
    response = input("Would you like to play another round of Rock, Paper, Scissors?: 'Y' for yes, anything else for no:   ")



