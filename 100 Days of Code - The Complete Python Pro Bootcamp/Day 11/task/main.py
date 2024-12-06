import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []

def start_game():
    player_hand.clear()
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))
    computer_hand.clear()
    computer_hand.append(random.choice(cards))
    computer_hand.append(random.choice(cards))
    print_state()

def blackjack_check(hand):
    if (11 in hand) and (10 in hand) and sum(hand) <= 21:
        return True
    else:
        return False

def print_state():
    print(f"Your Cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

def computer_play():
    while sum(computer_hand) < 16:
        if blackjack_check(player_hand) or blackjack_check(computer_hand):
            return
        computer_hand.append(random.choice(cards))
    if sum(computer_hand) > 21 and 11 in computer_hand:
        ace_index = computer_hand.index(11)
        computer_hand[ace_index] = 1
        computer_play()

def player_play():
    while sum(player_hand) < 21:
        if blackjack_check(player_hand) or blackjack_check(computer_hand):
            return
        player_hit = input("Type 'y' to get another card. type 'n' to pass: ")
        if player_hit == "y":
            player_hand.append(random.choice(cards))
        elif player_hit == "n":
            return
        print_state()
    if sum(player_hand) > 21 and 11 in player_hand:
        ace_index = player_hand.index(11)
        player_hand[ace_index] = 1
        player_play()

def final_game_check():
    if blackjack_check(player_hand) and blackjack_check(computer_hand):
        print("Double Black jack. Draw")
    elif blackjack_check(computer_hand):
        print("Dealer Got Black Jack. You lose nigga")
    elif blackjack_check(player_hand):
        print("You Got Black Jack. You Win!")
    elif sum(player_hand) > 21 and sum(computer_hand) > 21:
        print("You both suck, Draw!")
    elif sum(player_hand) > 21:
        print("You went over. You lose")
    elif sum(player_hand) > sum(computer_hand) and sum(player_hand) <= 21:
        print("You win!")
    elif sum(computer_hand) > sum(player_hand) and sum(computer_hand) <= 21:
        print("You lose")
    elif sum(computer_hand) > 21:
        print("Dealer went over. You win!")
    elif sum(player_hand) == sum(computer_hand):
        print("Draw.")
    return False

def blackjack():
    game_state = True
    ask_player = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask_player == "y":
        game_state = True
        print("\n" * 20)
    elif ask_player == "n":
        return
    start_game()
    while game_state:
        player_play()
        computer_play()
        print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
        print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
        game_state = final_game_check()
    blackjack()

blackjack()