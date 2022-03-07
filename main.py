# rock paper scissor game python

import random
l=["rock","paper","scissor"]
games=0
c_won=0
p_won=0

print("The one with most wins in the 10 games Wins!")

while games!=10:
    computer=random.choice(l)
    player=input("Enter a choice:")
    print(f"Computer chose:{computer}")

    if computer=="rock":
        if player=="rock":
            print("Its a draw")
        elif player=="paper":
            print("player won")
            p_won+=1
        elif player=="scissor":
            print("Computer wins!")
            c_won+=1
    if computer=="paper":
        if player=="rock":
            print("Computer Wins!")
            c_won+=1
        elif player=="paper":
            print("Its a draw")
            
        elif player=="scissor":
            print("player wins!")
            p_won+=1
    if computer=="scissor":
        if player=="rock":
            print("Player wins!")
            p_won+=1
        elif player=="paper":
            print("Computer Wins!")
            c_won+=1
        elif player=="scissor":
            print("Its a draw")

    games+=1
    print("\n")
print("\n")
print(("\n"))
print(f"Computer Won {c_won} games!")
print(f"player Won {p_won} games!")
if (c_won<p_won):
    print("Player wins the game!")

elif(c_won>p_won):
    print("computer wins the game!")
else:
    print("The game is a draw!")
            

    
