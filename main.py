## Higher or Lower ##

from art import logo, vs
from data import clubs
import os
import random

def format_data(clubs):
    club_name = clubs['name']
    club_league = clubs['league']
    club_origin = clubs['origin']
    return f"{club_name}, a {club_league} club, based in {club_origin}."

def check_guess(guess, club_a, club_b):
    follower_count_a = club_a['follower_ig_millions']
    follower_count_b = club_b['follower_ig_millions']
    if follower_count_a > follower_count_b:
        return guess == 'a'
    elif follower_count_b > follower_count_a:
        return guess == 'b'
    
score = 0
run_game = True
print(logo)

while run_game:
    
    club_a = random.choice(clubs)
    club_b = random.choice(clubs)
    while club_a == club_b:
        club_b = random.choice(clubs)

    print(f"Compare A: {format_data(club_a)}")

    print(vs)

    print(f"Against B: {format_data(club_b)}")

    user_guess = input("\nWhich club has more followers on IG? Type 'A' or 'B': ").lower()
    
    os.system("cls" if os.name == "nt" else "clear")

    is_correct = check_guess(user_guess, club_a, club_b)
    if is_correct:
        score += 1
        print(logo)
        print(f"You are correct! Current score: {score}.\n")
    else:
        run_game = False
        print(f"Wrong answer. Final score: {score}.\n")