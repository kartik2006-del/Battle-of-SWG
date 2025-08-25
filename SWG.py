import random

print('***** snake water game ***** '.center(120).title())
print('description : this is a three round game, every round you will get one point ,whoever has the point wins'.title())

weapon=['snake','water','gun']

count_user=0
count_comp=0



def game_py():
    global count_comp,count_user
    for round_no in range(1,4):
        print(f'-----Round {round_no}')

        x=input('enter your weapon (snake,water,gun) : '.lower())
        comp=random.choice(weapon)
        print(f'comp choose : {comp}')
        if x==comp:
            print('Result : TIE \n you : {count_user} \n comp : {count_comp}')
        elif x not in weapon:
            print('INVALID INPUT')
        elif x=='gun' and comp=='snake'or x=='water' and comp=='gun' or x=='snake' or comp=='water' :
            count_user+=1
            print(f'you WIN \n your score : {count_user} \n comp score : {count_comp}')
        else:
            count_comp+=1

            print(f'comp WIN \n your score : {count_user} \n comp score : {count_comp}')
    print('===== FINAL SCORE ====='.center(120))
    if count_comp>count_user:
        print(f' CONGRATULATIONS ! comp WIN the game \n comp final score :  {count_comp} \n your final score : {count_user}')
    elif count_user>count_comp:
        print(f'CONGRATULATIONS ! you WIN the game \n your final score : {count_user} \n comp final score : {count_comp} ')
    else :
        print(f"it is a tie Final score( you : {count_user} \n comp : {count_comp})")

game_py()

        
    