## Higher or Lower ##

from art import logo, vs
from data import clubs
from os import system
import random

def format_data(clubs):
    club_name = clubs['name']
    club_league = clubs['league']
    club_origin = clubs['origin']
    return f"{club_name}, a {club_league} club, based in {club_origin}."

club_a = random.choice(clubs)
club_b = random.choice(clubs)
while club_a == club_b:
    club_b = random.choice(clubs)

print(logo)

print(f"Compare A: {format_data(club_a)}")

print(vs)

print(f"Against B: {format_data(club_b)}")