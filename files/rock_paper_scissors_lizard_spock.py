# -*- coding: utf-8 -*-
from __future__ import print_function # must be first in file
import random
import time
import sys

#1 is rock
#2 is paper
#3 is scissors
#4 is lizard
#5 is spock

blah = "Wiseass\n"

def wiseass():
    for l in blah:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)


def rpsls():
    cpu = random.randint(1,5)
    p1 = raw_input('Rock, Paper, Scissors, Lizard, or Spock:\n\n')
    if p1 != "Rock" or "rock" or "Paper" or "paper" or "Scissors" or "scissors" or "Lizard" or "lizard" or "Spock" or "spock":
        wiseass()
    
    if cpu == 1:
        if p1 == "Rock" or "rock":
            print('Tie!')
    elif p1 == "Paper" or "paper":
        print ('Paper beats Rock. You win!')
    elif p1 == "Scissors" or "scissors":
        print ('Rock beats Scissors. You lose!')
    elif p1 == "Lizard" or "lizard":
        print ('Rock beats Lizard. You lose!')
    elif p1 == "Spock" or "spock":
        print ('Spock beats Rock. You win!')

    if cpu == 2:
        if p1 == "Rock" or "rock":
            print('Paper beats Rock. You lose!')
    elif p1 == "Paper" or "paper":
        print ('Tie!')
    elif p1 == "Scissors" or "scissors":
        print ('Scissors beats Paper. You win!')
    elif p1 == "Lizard" or "lizard":
        print ('Lizard beats Paper. You win!')
    elif p1 == "Spock" or "spock":
        print ('Paper beats Spock. You lose!')

    if cpu == 3:
        if p1 == "Rock" or "rock":
            print ('Rock beats Scissors. You win!')
    elif p1 == "Paper" or "paper":
        print ('Scissors beats Paper. You lose!')
    elif p1 == "Scissors" or "scissors":
        print ('Tie!')
    elif p1 == "Lizard" or "lizard":
        print ('Scissors beats Lizard. You lose!')
    elif p1 == "Spock" or "spock":
        print ('Spock beats Scissors. You win!')
        
    if cpu == 4:
        if p1 == "Rock" or "rock":
            print ('Rock beats Lizard. You win!')
    elif p1 == "Paper" or "paper":
        print ('Lizard beats Paper. You lose!')
    elif p1 == "Scissors" or "scissors":
        print ('Scissors beats Lizard. You win!')
    elif p1 == "Lizard" or "lizard":
        print ('Tie!')
    elif p1 == "Spock" or "spock":
        print ('Lizard beats Spock. You lose!')
        
    if cpu == 5:
        if p1 == "Rock" or "rock":
            print ('Spock beats Rock. You lose!')
    elif p1 == "Paper" or "paper":
        print ('Paper beats Spock. You win!')
    elif p1 == "Scissors" or "scissors":
        print ('Spock beats Scissors. You lose!')
    elif p1 == "Lizard" or "lizard":
        print ('Lizard beats Spock. You win!')
    elif p1 == "Spock" or "spock":
        print ('Tie!')
    

def bot():
    p = [1, 2, 3, 4, 5,]
    cpu = random.choice(p)
    p1 = random.choice(p)
    print(p1)
    print(cpu)

    if cpu == 1:
        if p1 == "Rock" or "rock":
            print('Tie!')
    elif p1 == "Paper" or "paper":
        print ('Paper beats Rock. You win!')
    elif p1 == "Scissors" or "scissors":
        print ('Rock beats Scissors. You lose!')
    elif p1 == "Lizard" or "lizard":
        print ('Rock beats Lizard. You lose!')
    elif p1 == "Spock" or "spock":
        print ('Spock beats Rock. You win!')

    if cpu == 2:
        if p1 == "Rock" or "rock":
            print('Paper beats Rock. You lose!')
    elif p1 == "Paper" or "paper":
        print ('Tie!')
    elif p1 == "Scissors" or "scissors":
        print ('Scissors beats Paper. You win!')
    elif p1 == "Lizard" or "lizard":
        print ('Lizard beats Paper. You win!')
    elif p1 == "Spock" or "spock":
        print ('Paper beats Spock. You lose!')

    if cpu == 3:
        if p1 == "Rock" or "rock":
            print ('Rock beats Scissors. You win!')
    elif p1 == "Paper" or "paper":
        print ('Scissors beats Paper. You lose!')
    elif p1 == "Scissors" or "scissors":
        print ('Tie!')
    elif p1 == "Lizard" or "lizard":
        print ('Scissors beats Lizard. You lose!')
    elif p1 == "Spock" or "spock":
        print ('Spock beats Scissors. You win!')
        
    if cpu == 4:
        if p1 == "Rock" or "rock":
            print ('Rock beats Lizard. You win!')
    elif p1 == "Paper" or "paper":
        print ('Lizard beats Paper. You lose!')
    elif p1 == "Scissors" or "scissors":
        print ('Scissors beats Lizard. You win!')
    elif p1 == "Lizard" or "lizard":
        print ('Tie!')
    elif p1 == "Spock" or "spock":
        print ('Lizard beats Spock. You lose!')
        
    if cpu == 5:
        if p1 == "Rock" or "rock":
            print ('Spock beats Rock. You lose!')
    elif p1 == "Paper" or "paper":
        print ('Paper beats Spock. You win!')
    elif p1 == "Scissors" or "scissors":
        print ('Spock beats Scissors. You lose!')
    elif p1 == "Lizard" or "lizard":
        print ('Lizard beats Spock. You win!')
    elif p1 == "Spock" or "spock":
        print ('Tie!')

def bot_repeat():
    a = 0

    if a < 20:
        time.sleep(2)
        bot()
        a += 1
    else:
        time.sleep(0.2)

