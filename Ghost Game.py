from random import randint

print('Ghost Game')
brave = True
score = 0

while brave == True:
    ghost_door = randint(1, 3)
    print('Перед тобой три двери...')
    print('За одной из них призрак.')
    print('Какую дверь ты откроешь?')
    door = input('1, 2 или 3? ')
    door_num = int(door)

    if door_num == ghost_door:
        print('ПРИЗРАК!')
        brave = False   
    else:
        print('Фух, никого')
        print('Ты заходишь в следующую комнату...')
        score = score + 1

print('О нет! ТИКАЙ ОТСЮДА, ГЛУПЕЦ!')
print('Ты проиграл! Твой счет:', score)
