import random

response=input("Do you want to roll the dice?")

while response == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        response=input("Do you want to roll the dice?")
    if no ==2:
        print("[-----]")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("[-----]")
        response=input("Do you want to roll the dice?")
    if no ==3:
        print("[-----]")
        print("[     ]")
        print("[0   0]")
        print("[  0  ]")
        print("[-----]")
        response=input("Do you want to roll the dice?")
    if no ==4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        response=input("Do you want to roll the dice?")
    if no ==5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        response=input("Do you want to roll the dice?")
    if no ==6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        response=input("Do you want to roll the dice?")
while response == "n":
    print("Thanks you for playing")