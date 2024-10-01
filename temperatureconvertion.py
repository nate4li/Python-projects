import random
from colorama import Fore

red=Fore.RED
black=Fore.BLACK
green=Fore.GREEN
yellow=Fore.YELLOW
blue=Fore.BLUE

def temperatureconverter(user_input):
    FAHREHNEIT_TO_CELSIUS = (user_input - 32) * 5/9
    
    if(user_input>=90):
        print("fahrenheit: ",red, "{0:4.1f}".format(user_input),black)
        print("celsius", red, "{0:4.1f}".format(FAHREHNEIT_TO_CELSIUS),black)
    elif(user_input<=75) & (user_input>=89):
        print("fahrenheit: ",yellow, "{0:4.1f}".format(user_input),black)
        print("celsius", yellow, "{0:4.1f}".format(FAHREHNEIT_TO_CELSIUS),black)
    elif(user_input>=64) & (user_input<=74):
        print("fahrenheit: ",blue, "{0:4.1f}".format(user_input),black)
        print("celsius", blue, "{0:4.1f}".format(FAHREHNEIT_TO_CELSIUS),black)
    elif(user_input<=63):
        print("fahrenheit: ",green, "{0:4.1f}".format(user_input),black)
        print("celsius", green, "{0:4.1f}".format(FAHREHNEIT_TO_CELSIUS),black)

      

user=float(input("Enter a temperature in Fahrenheit to convert to Celsuis: "))

for x in range(5):
    temperatureconverter(user)
    user=float(input("Enter a temperature in Fahrenheit to convert to Celsuis: "))