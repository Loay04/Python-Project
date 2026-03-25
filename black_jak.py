import os 
import random
def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")
def deal_card():
    card =[2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(card)
def calculate_card(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare_card(user_score, computer_score):
    result = {
      "draw":"Draw\n\n",
      "user_over": "you went over 21 Sorry\n\n",
      "computer_over":"Computer went over 21, you win\n\n",
      "user_21":"you won with a blackjack\n\n",
      "computer_21":"Sorry, computer had a blackjack\n\n",
      "user_win":"you win\n\n",
      "user_lose":"you lose\n\n"
     } 
    if user_score == computer_score:
        return result["draw"]
    elif user_score > 21:
        return result["user_over"]
    elif computer_score > 21:
        return result["computer_over"]
    elif user_score == 21:
        return result["user_21"]
    elif computer_score == 21:
        return result["computer_21"]
    elif user_score > computer_score:
        return result["user_win"]
    else:
        return result["user_lose"]
def game():
    computer_card = [deal_card() for _ in range(2)]
    user_card = [deal_card() for _ in range(2)]
    Game_on = True
    while Game_on:
        user_score = calculate_card(user_card)
        computer_score = calculate_card(computer_card)
        print(f"\n\nYour cards are {user_card}, current score {sum(user_card)}")
        print(f"Computer's first card is {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21  or computer_score > 21:
            Game_on = False
        else:
            user_needs_another_card = input("Get another card ? Y/N.......").upper()
            if user_needs_another_card == "Y":
              user_card.append(deal_card())
              user_score = calculate_card(user_card)
            else:
              Game_on= False
    while computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_card(computer_card)
    print(f"\nYour final hand: {user_card} with score {user_score}")
    print(f"\nComputer's final hand: {computer_card} with score {computer_score}")
    print(compare_card(user_score,computer_score))
  
clear()        
while input("1- Snake Game\n2- Twenty one\n3- Ping Pong\n________\n") .lower() == "twenty one":
    game()