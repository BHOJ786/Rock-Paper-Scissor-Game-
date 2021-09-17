import random # for computer's choice

def game(comp, player):
    if comp == player:
        print("<    TIED   >")
    elif comp=='r':
        if player =='p':
            print ("<    WIN   >")
        elif player =='s':
            print ("<    LOSE  >")
    elif comp=='p':
        if player =='s':
            print ("<   WIN  >")
        elif player =='r':
            print ("<   LOSE   >")
    elif comp=='s':
        if player =='p':
            print ("<   WON   >")
        elif player =='r':
            print ("<    LOSE   >")

# computer choosing from choices randomly

print("computer turn : Rock(r) Paper(p) Scissor(s) ??")
randomno=random.randint(1,3)
if randomno == 1:
    comp = 'r'
elif randomno == 2:
    comp = 'p'
elif randomno == 3:
    comp = 's'

# Player input

player=input("Player's turn : Rock(r) Paper(p) Scissor(s) ??")


a=game(comp, player)
print (f"< THE COMPUTER CHOOSE  < {comp} > >")
print (f"< AND THE PLAYER CHOOSE  < {player} > >")

