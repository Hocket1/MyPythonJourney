print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print('Welcome to Treasure Island')
print('Your mission is find the Treasure') 
passage = input('You are at a crossroad. Do You want to turn right or left: \n').lower()
if passage == 'left':
    swim_or_wait=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.: \n').lower()
    if swim_or_wait == 'wait':
        Door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose: \n').lower()
        if Door == 'yellow':
            print('Yay! You won youself a scholarship to MIT')
        elif Door == 'red':
            print('Ooch!. Sorry you got burned by fire')
        elif Door == 'blue':
            print("brrr!. Eaten by a beast")
        else:
            print('Game Over')
    else:
        print('Oooch!. Swallowed by a chrocodile')
        
else:
    print('Game over. You fell into a hole')

