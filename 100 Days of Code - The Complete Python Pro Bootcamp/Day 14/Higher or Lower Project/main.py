import game_data
import art
import random

def random_person():
    random_selection = random.choice(game_data.data)
    return random_selection

def check_higher_follower_count(person_1, person_2):
    person_1_follower_count = int(person_1['follower_count'])
    person_2_follower_count = int(person_2['follower_count'])
    if person_1_follower_count > person_2_follower_count:
        return person_1
    else:
        return person_2

def print_state():
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {random_selection_A['name']}, a {random_selection_A['description']}, "
          f"from {random_selection_A['country']}")
    print(art.vs)
    print(f"Against B: {random_selection_B['name']}, a {random_selection_B['description']}, "
          f"from {random_selection_B['country']}")

random_selection_A = random_person()
random_selection_B = random_person()

game_state = True
score = 0
print_state()
while game_state:
    higher_follower_person = check_higher_follower_count(random_selection_A, random_selection_B)
    print(f"its {higher_follower_person['name']} btw")
    selection = input("Who has more followers? Type 'A' or 'B': ")
    if selection == "A":
        if random_selection_A is higher_follower_person:
            score += 1
            random_selection_A = random_selection_B
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_state = False
            break
    elif selection == "B":
        if random_selection_B is higher_follower_person:
            score += 1
            random_selection_A = random_selection_B
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_state = False
            break
    random_selection_B = random_person()
    print("\n"*20)
    while random_selection_A is random_selection_B:
        random_selection_B = random_person()
    if game_state:
        print_state()