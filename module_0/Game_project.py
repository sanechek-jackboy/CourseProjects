import numpy as np

def game_core(number):
    '''Сначала устанавливаем предполагаемое число равным 50, и если оно не равно number, то изменяем его, 
    присваивая значение, равное сумме (разности)текущего значения и средним арифметическим между 
    предполагаемым числом и текущим максимальным (минимальным) значением этого числа'''
    count = 1
    inf = 1 #нижняя граница
    sup = 100 #верхняя граница
    
    while True:
        predict = 50
        while number != predict:
            count+=1
            if number > predict:
                inf = predict #нижняя граница теперь равна текущему значению предполагаемого числа
                predict += (sup-inf+1)//2 #делаем предполагаемое число центром отрезка [inf, sup]
            else:
                sup = predict #верхняя граница теперь равна текущему значению предполагаемого числа
                predict -= (sup-inf+1)//2 #делаем предполагаемое число центром отрезка [inf, sup]
        return count
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core)