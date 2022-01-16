import random


class TossClass:
    def toss():
        choices = ['head', 'tail']
        user1 = input("Player1: Enter your choice\n")
        user2 = input("Player2: Enter your choice\n")

        winners = [user1, user2]
        result = random.choice(winners)

        if user1 == choices[1]:
            if user2 == 'tail':
                print("You have to choose head now\ntail is choosed by Player1")
        elif user1 == choices[0]:
            if user2 == 'head':
                print("You have to choose tail now\nhead is choosed by Player1")

        if result == user1:
            print("Player1 have Won the toss")
        elif result == user2:
            print("Player2 have Won the toss")
        else:
            pass


    toss()
