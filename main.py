import random
import sys
from datetime import datetime

MAX_COUNT = 5
COUNT = 0
TODAY = datetime.now().strftime("%d-%m-%Y")


def get_random_word() -> list:
    with open("words_db.txt", "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            word_list = line.split(",")
        random_letter_list = list(random.sample(word_list, 1)[0].upper())
        hidden = ['*'] * len(random_letter_list)
        print("-" * 84)
        print(f"|У вас є 5 спроб, щоб відгадати слово, яке складаєтся з 5 літер.                   |\n|Якщо вгадана літера знаходиться на своєму місці, то вона буде у верхньому регістрі|\n|Якщо літера вгадана, але вона не на своєму місці - вона буде в нижньому регістрі. |")
        print(f"|>>>> {hidden}                                                    |")
        # print(f"|>>>> {random_letter_list}                                                    |")
        print("-" * 84)
        quess_word(random_letter_list, is_word_of_the_day=False)
        
        
def get_word_of_the_day():
    # Проверяем нет ли записи с сегодняшней датой в списке со словом дня. 
    with open("word_of_the_day.txt", "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            word_of_the_day_list = line.split("!")
            if word_of_the_day_list[0] == TODAY:
                print("-" * 51)
                print(f"|Вітаю, слово дня уже відгадано, повертайся завтра:|")    
                print("-" * 51)
                start_game()
            else:
                # Если слово не отгадывали сегодня - запускаем выбор рандомного слова из списка.         
                with open("words_db.txt", "r", encoding="utf-8") as f:
                    while True:
                        line = f.readline()
                        if not line:
                            break
                        word_list = line.split(",")
                        word_day_list = list(random.sample(word_list, 1)[0].upper())
                        hidden = ['*'] * len(word_day_list)
                        print("-" * 84)
                        print(f"|У вас є 5 спроб, щоб відгадати слово, яке складаєтся з 5 літер.                   |\n|Якщо вгадана літера знаходиться на своєму місці, то вона буде у верхньому регістрі|\n|Якщо літера вгадана, але вона не на своєму місці - вона буде в нижньому регістрі. |")
                        print(f"|>>>> {hidden}                                                    |")
                        # print(f"|>>>> {word_day_list}                                                    |")
                        print("-" * 84)
                        quess_word(word_day_list, is_word_of_the_day=True)
                        
 
def game_mode() -> int:
    print("-" * 35)
    print(f"|Будь ласка оберіть ігровий режим:|\n|1. Відгадувати рандомне слово    |\n|2. Відгадувати слово дня         |\n|0. Вийти з гри                   |")
    print("-" * 35)
    player_input = input(">>>> ")
    return player_input


def quess_word(random_letter_list, is_word_of_the_day):
    global COUNT
    hidden = ['*'] * len(random_letter_list)
    input_word = input("|>>>> ")
    input_letter_list = list(input_word.replace("|>>>> ", "").upper())
    if len(random_letter_list) != len(input_letter_list):
        print("-" * 66)
        print("|Введіть будь ласка слово, довжина якого рівна 5 символів.|")
        print("-" * 66)
        print(random_letter_list)
        quess_word(random_letter_list, is_word_of_the_day)
    else:
        COUNT += 1
        if COUNT < 5:
            for index in range(len(random_letter_list)):
                if input_letter_list[index] == random_letter_list[index]:
                    hidden[index] = input_letter_list[index]
                elif input_letter_list[index] in random_letter_list:
                    hidden[index] = input_letter_list[index].lower()
                if input_letter_list == random_letter_list:
                    print("-" * 36)
                    print(f"|Вітаю з перемогою, загадане слово:|")    
                    print(f"|{random_letter_list}         |")
                    print(f"|Ти відгадав його з {COUNT} спроби       |")
                    print("-" * 36)
                    COUNT = 0
                    if is_word_of_the_day == True:
                        with open("word_of_the_day.txt", "w", encoding="utf-8") as f:
                            f.write(TODAY)
                    start_game()
            print(hidden)
            print(f"Кількість спроб що залишилась: {MAX_COUNT - COUNT}")
            quess_word(random_letter_list, is_word_of_the_day)
        else:
            print("-" * 36)
            print(f"|Спроби скінчились, загадане слово:|")    
            print(f"|{random_letter_list}         |")
            print("-" * 36)
            start_game()
            
            
def start_game():
    gm = int(game_mode())
    if gm == 0:
        print("-" * 37)
        print("|Успіхів тобі гравець, ще побачимось|")
        print("-" * 37)
        sys.exit(0)
    elif gm == 1:
        get_random_word() 
    elif gm == 2:
        get_word_of_the_day() 


if __name__ == "__main__":
    start_game()
    