import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

win_counter = 0
lose_counter = 0
while True:
    player_move = input("Choose [r] for rock, [p] for paper, [s] for scissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid input. Try again!")
        continue

    computer_random_number = random.randint(1, 3)
    computer_move = ""
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or (player_move == scissors and computer_move == paper) \
        or (player_move == paper and computer_move == rock):
        print("You win!")
        win_counter += 1
    elif player_move == computer_move:
        print("Draw")
    else:
        print("You lose!")
        lose_counter += 1
    if (win_counter == 2 and lose_counter == 0) or (win_counter == 2 and lose_counter == 1):
        print("You are the winner!")
        break
    elif lose_counter == 2:
        print("You lost the game!")
        break