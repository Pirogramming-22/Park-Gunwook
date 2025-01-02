from random import randint

number = 1
playerATurn = True

def get_valid_input():
    while True:
        try:
            playerNum = float(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : "))
            if playerNum in [1, 2, 3]:
                return int(playerNum)
            elif playerNum.is_integer():
                print("1, 2, 3 중 하나를 입력하세요.")
            else:
                print("정수를 입력하세요")
        except ValueError:
            print("정수를 입력하세요")

def play_turn(player_name, count):
    global number
    for _ in range(count):
        if number >= 31:
            print(f"{player_name} : {number}")
            return True
        print(f"{player_name} : {number}")
        number += 1
    return False

while True:

    if(playerATurn == False):
        playerNum = get_valid_input()
    else:
        playerNum = randint(1, 3)
        
    
    game_over = play_turn('computer' if playerATurn else 'player', playerNum)

    if game_over:
        print(f"{'player' if playerATurn else 'computer'} win!")
        break

    playerATurn = not playerATurn