'''
1. создаём функцию, расчитывающую кратчайший путь (shortest_way)
функция выдаёт False/True и кратчайший путь до игрока по координатам
2. функции мы передаём 2 значения:
  координаты начальной клетки (start)
  координаты конечной клетки (finish)
3. создаём закрытый и открытый список
 закрытый (close) - для помещения в него пройденных клеток
 открытый (open) - клетки в которые можно пойти из текущих
4. в функции находится цикл "while running"
running имеет значение False:
  если мы достигли игрока
  если список open пустой (нам некуда ходить)
5. на первой итерации задаём значения первой клетки
  len_short_way = 0
  all_way = 0
  cell_value = 0
  coords - кортеж с координатами клетки
и добовляем их в словарь в списке close
* all_way, len_short_way и cell_value = 0, т.к их значения не нужны

5. проверим не стоим ли мы уже в клетке игрока
 если да - выдаём кортеж, в котором True и список координат пути до игрока
6. проверяем есть ли клетки в списке open. если нет - возращаем False и выходим
* на первой итерации мы не проверяем открытый список (мы ещё не выбрали клетку)
7. проверяем не является ли клетка в которую мы собираемся пойти препядствием
 если да - игнорируем её
8. проходимся по 4 соседним клеткам, вызывая метод cell, который принимает параметры
  start - координаты начальной клетки
  finish - координаты конечной клетки
  previous_cell - координаты предыдущей клетки
функция выдаёт следущие значения:
  длинна кратчайшего пути от этой, до конечной клетки методом "Манхэттен" (функция manhattan_len)
  длину уже пройденного пути от начальной клетки
  вес клетки (сумма первых двух зеачений)
9. далее, проходясь по клеткам, создаём в списках open и close словари и добовляем в него значения клетки
ключами словария будут
  len_short_way - длинна кратчайшего пути от этой, до конечной клетки методом "Манхэттен" (функция manhattan_len)
  all_way - длина уже пройденного пути от начальной клетки
  cell_value - вес клетки
  coords - кортеж с координатами предыдущей клетки
10. но, перед тем как добавить клетку в список, нужно проверить есть ли она уже там
 если есть, то сравниваем их значения по ключу cell_value, выбираем минималное и заменяем
'''
from pygame_init import map_obj
from  Map import Wall
from config import *

def get_cell_value(value):
    return value['cell_value']

class Shortest_way:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish
        # закрытый - для помещения в него пройденных клеток
        self.close = {}
        # открытый - клетки в которые можно пойти из текущих
        self.open = {}
        # если путь построен - True, иначе - False
        self.error = False
        # список с кортежами координат пути
        self.way = []
        # если мы в одной клетке с игроком - выходим
        if self.start == self.finish:
            return
        start_flag = True
        running = True
        kk = 0
        while running:
            kk += 1
            # проверяем первая ли итерация
            if start_flag:
                # задаём параметры начальной клетки
                cell_with_min_weight = {'len_short_way': 0, 'passed_way': 0, 'cell_value': 0, 'current_coords': self.start, 'previous_coords': self.start}
                self.close[self.start] = cell_with_min_weight
                start_flag = False
            else:
                # проверяем пустой ли список
                if len(self.open) == 0:
                    return
                # следущий ход делаем в клетку из списка self.open с минимальным значением
                cell_with_min_weight = min(self.open.values(), key=lambda k: k['cell_value'])
                # current_step_list - список из словаря (как next_step)
                self.close_append(cell_with_min_weight)

            x, y = cell_with_min_weight['current_coords']
            if self.check_cell((x, y), (x, y + 1), cell_with_min_weight['passed_way']):
                return

            if self.check_cell((x, y), (x + 1, y), cell_with_min_weight['passed_way']):
                return

            if self.check_cell((x, y), (x, y - 1), cell_with_min_weight['passed_way']):
                return

            if self.check_cell((x, y), (x - 1, y), cell_with_min_weight['passed_way']):
                return
            # input()


    def open_append(self, cell):
        if cell['current_coords'] in self.close:
            return
        if cell['current_coords'] in self.open:
            if cell['cell_value'] < self.open[cell['current_coords']][
                'cell_value']:
                # print(self.open[cell['current_coords']]['current_coords'])
                # exit()
                del self.open[cell['current_coords']]
                self.open[cell['current_coords']] = cell
        else:
            self.open[cell['current_coords']] = cell

    # добовляем в список close
    def close_append(self, cell):
        if cell['current_coords'] in self.close:
            if cell['cell_value'] < self.close[cell['current_coords']][
                'cell_value']:
                del self.close[cell['current_coords']]
                self.close[cell['current_coords']] = cell
                del self.open[cell['current_coords']]
        else:
            self.close[cell['current_coords']] = cell
            del self.open[cell['current_coords']]
        return

    # поиск кратчайшего расстояния по методу "Манхэттен"
    def manhattan_len(self, current_coords):
        x0, y0 = current_coords
        x1, y1 = self.finish
        return abs(x1 - x0) + abs(y1 - y0)




    # проверяем находится ли игрок в клетке -> вызываем функцию для возврата пути
    # прверяем находится ли в клетке стена/ящик -> выходим из функции
    # расчитываем пареметры клетки
    # проверяем есть ли она списке self.open
    # если нет -> добовляем
    # если есть -> добовляем клетку с наименьшим весом
    def check_cell(self, previous_coords, current_coords, passed_way):
        x, y = current_coords
        if self.finish == current_coords:
            # close_dict = {}
            # for i in self.close:
            #     close_dict[i['current_coords']] = i
            i = previous_coords
            # self.way.append(current_coords)
            while i != self.start:
                self.way.insert(0, i)
                i = self.close[i]['previous_coords']
                current_coords = i
            return True


        if map_obj.string[y][x] != '.':
            return False

        cell = {}
        cell['len_short_way'] = self.manhattan_len(current_coords)
        cell['passed_way'] = passed_way + 1
        cell['cell_value'] = cell['len_short_way'] + cell['passed_way']
        cell['previous_coords'] = previous_coords
        cell['current_coords'] = current_coords
        self.open_append(cell)
        return False

if __name__ == 'main':
    start = (5, 5)
    finish = (5, 7)
    # print(shortest_way(start, finish))