import pygame
from random import randint

from config import *

# Импортируем объекты

from start_screen import *

# импортируем файл с картой
from Map import *
map_obj = Map(file_name='1.txt', room_x=1, room_y=1)

from Ghost import *
# from Menu import *

from Player import *
from Enemy import *
from number_of_steps import *
# from Screen import *

