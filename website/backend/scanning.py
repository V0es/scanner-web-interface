#тестирую выборку моделей сканеров из вывода sane-find-scanner
import re
from typing import List
import subprocess


def parse_device_message(message : str) -> List[str]: 
    stripped_message = message.rstrip().split('\n') # удаляем пробельные символы и разделяем по символам '\n'
    available_scanners = list(filter(lambda x: x.count('found USB') != 0, stripped_message)) # отбираем строки, в которых есть информация о сканнерах и преобразуем в список

    for index, scanner in enumerate(available_scanners):
        available_scanners[index] = ''.join(re.findall(r'\[([^=,]*)\]\)', scanner)) # ищем regex по паттерну '[' (любое кол-во символов, кроме '=' и ',') '])'
    print(available_scanners)
    return available_scanners



def parse_message(message):
    pass

#message = subprocess.getoutput(f'sane-find-scanner')
#print(parse_device_message(message))