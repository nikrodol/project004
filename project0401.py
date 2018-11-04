#Игра "Отгадай слово".
import random

def guessing(answer, count=0, badcount=0):#Процесс игры.
    print('Попытка № {}:'.format(k + 1), end='')
    guessword = list(input())
    for j in range(len(answer)):
        if answer[j] == guessword[j]:#Определяем буквы на "своем месте".
            count += 1
        else:
            for x in range(len(answer)):#Определяем буквы на "чужом месте".
                if guessword[x] == answer[j]:
                    badcount += 1
                    break
    print('На "своем месте": {}'.format(count))
    print('На "чужом месте": {}'.format(badcount))
    print()
    return count

letters = random.sample(list('АЕНОСТ'), 4)#Генерация слова.
yes_no='Да'

while yes_no=='Да':#Согласие на игру.
    print('Загадано четырехбуквенное слово из букв А, Е, Н, О, С, Т.\nОтгадай!')
    k=0
    for k in range(10):#Перебор попыток.
        if guessing(letters)==4:#Победа.
            print('Вы выиграли! Поздравляем! Если хотите сыграть еще раз, то введите "Да"')
            yes_no=input().capitalize()
            break
        if k==10:#Проигрыш.
            print('Печально, но вы проиграли. Хотите еще раз сыграть? Если')
            yes_no=input().capitalize()
print('До следущего сеанса игры!')