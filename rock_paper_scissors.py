
import random

move_keys={
    "R":"rock",
    "P":"paper",
    "S":"scissors"
}
mark={
    "S":{"r":1,"s":0,"p":-1},
    "R":{"r":0,"p":1,"s":-1},
    "P":{"r":-1,"p":0,"s":1}
}

def status_message(move_1,move_2):
    messages=("Paper Wraps Rock","Scissors cuts paper", "Rock smashes scissors")
    moves=(move_1,move_2)
    print(moves)
    if (("paper" in moves) and ("rock" in moves)):
        print(messages[0])
    elif (("paper" in moves) and ("scissors" in moves)):
        print(messages[1])
    else:
        print(messages[2])

def print_instructions():

    print(
        """
        ROCK PAPER SCISSORS
        LETS PLAY TOGETHER
        PRESS R TO PLAY ROCK
              S TO PLAY SCISSORS
              P TO PLAY PAPER
        """
        )

print_instructions()

while True:

    

    print("Enter_move")
    player_move=input().upper()

    computer_move=random.choice(tuple(move_keys.keys()))

    try:
        player_mark=mark[player_move][player_move.lower()]
    except KeyError:
        print('please input an accepted move')
        continue

    computer_mark=mark[player_move][computer_move.lower()]

    if  player_mark > computer_mark  :
        print("I played {}".format(move_keys[computer_move]))
        status_message(move_keys[player_move],move_keys[computer_move])
        print("you win")
        

    elif player_mark < computer_mark:
        print("I played {}".format(move_keys[computer_move]))
        status_message(move_keys[player_move],move_keys[computer_move])
        print("you loose")

    else:
        print("I played {}".format(move_keys[computer_move]))
        print("it's a tie")
        continue


    print("press 'E' to exit or any other key to play again")
    again=input().upper()

    if again =="E":
        break
    else:
        continue


