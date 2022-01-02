import ascii_art as aa
import random


def deal_card():
    """Returns a random card from the deck of cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards as input and calculates the total score of the cards and returns it."""
    # Return 0 in case the initial cards received are ace and 10 as it represents a blackjack.
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # In case there's a ace in the cards received and the sum of the cards is already greater than 21 then remove
    # the ace from the cards and insert 1 in its's place.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # Return the sum of all the available cards
    return sum(cards)


def compare(user_score, computer_score):
    """Function to compare the scores of the user and the computer and check for the game status depending on it """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose!!"

    if user_score == computer_score:
        return "It's a Draw!!"
    elif computer_score == 0:
        return "You lose, opponent has a blackjack!!"
    elif user_score == 0:
        return "You win, You had a blackjack!!"
    elif user_score > 21:
        return "You went over. You lose!!"
    elif computer_score > 21:
        return "You win, computer went over!!"
    elif user_score > computer_score:
        return "You win !!!"
    else:
        return "You lose !!"


def play_game():
    """Function to start the game."""
    print(aa.logo)

    # Initial lists of both the user and the computer
    user_cards = []
    computer_cards = []

    # Flag to check for the game status
    is_game_over = False

    # Give both the computer and the user the initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Loop that will the run till the game is not over
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards : {user_cards}, current score : {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    if not is_game_over:    
        # The computer will get a random card till the user doesn't end the game and the score will keep updating
        while computer_score != 0 or computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(computer_score=computer_score, user_score=user_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n' : ") == 'y':
    aa.cls()
    play_game()
