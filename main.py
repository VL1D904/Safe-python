# Импорт необходимых библиотек
import pygame
import sys
import time

# Импорт содержимого из миниигр
from rub import *
from virus import *
from arcade import *
from start import *

# создание экрана подключение шрифтов музыки и определение стартовой сцены
pygame.init()
pygame.display.set_caption('safe_python')
size = 900, 750
screen = pygame.display.set_mode(size)
name_font = pygame.font.Font('plot/font.otf', 20)
text_font = pygame.font.Font('plot/font.otf', 16)
font = pygame.font.Font('plot/font.otf', 30)
number_scene = 0
music = pygame.mixer_music.load('music/music.mp3')

# Функция добавления сцены в БД
def insert(number):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f'INSERT INTO Scenes VALUES ({number})')
    con.commit()
    con.close()

# Основной класс игры
class Game:
    def __init__(self):
        # Загрузка всех сцен из файла
        self.scenes = []

        arr = []
        for scene in open('plot/novels.txt', 'r', encoding='utf-8').readlines():
            if scene.strip() != '_':
                arr.append(scene.strip())
            else:
                self.scenes.append(arr)
                arr = []

    # Функция затемнения экрана
    def darkness(self, scene):
        for color in range(200, 50, -20):
            background = pygame.transform.scale(pygame.image.load(scene), (900, 750))
            background.fill((color, color, color), special_flags=pygame.BLEND_RGBA_MULT)
            background_rect = background.get_rect()
            screen.blit(background, background_rect)
            pygame.display.flip()
            time.sleep(.1)
        
    # Функция отрисовки элементов
    def draw(self, scene):
        # Отрисовка заднего фона
        background = pygame.transform.scale(pygame.image.load(scene[1]), (900, 750))
        background_rect = background.get_rect()
        screen.blit(background, background_rect)

        # Отрисовка персонажа при необходимости
        if scene[5] != 'False':
            hero_img = pygame.image.load(scene[5])
            hero_img = pygame.transform.scale(hero_img, tuple(map(int, scene[7].split())))
            hero_rect = hero_img.get_rect()
            hero_rect.x = int(scene[6].split()[0])
            hero_rect.y = int(scene[6].split()[1])
            screen.blit(hero_img, hero_rect)

        # Отрисовка поля для текста
        rect = pygame.Surface((900, 150))
        rect.set_alpha(220)
        rect.fill((32, 32, 32))
        screen.blit(rect, (0, 600))

        # Отрисовка текста (Имя героя и его реплика)
        name_hero = name_font.render(scene[2], True, tuple(map(int, scene[4].split())))
        text_hero = text_font.render(scene[3], True, tuple(map(int, scene[4].split())))
        screen.blit(text_hero, (30, 650))
        screen.blit(name_hero, (20, 610))

    # Опредение типа сцены
    def set_scene(self, scene):
        global guitar, number_scene
        match scene[0]:
            case 'novel':
                self.draw(scene)
            case 'darkness':
                self.darkness(scene[1])
                number_scene += 1
            case 'rub':
                insert(number_scene)
                rub.main()
                number_scene += 1
            case 'virus':
                insert(number_scene)
                virus.main()
                number_scene += 1
            case 'arcade':
                insert(number_scene)
                arcade.main()
                number_scene += 1
            case 'start':
                number_scene = start.main()
            case 'end':
                screen.fill((0, 0, 0))
                end_font = pygame.font.Font('plot/font.otf', 50)
                end_text = end_font.render('Конец', True, (255, 255, 255))
                avtors = name_font.render('Авторы:', True, (255, 255, 255))
                name_1 = name_font.render('Семенова Саша', True, (255, 255, 255))
                name_2 = name_font.render('Гусев Влад', True, (255, 255, 255))
                name_3 = name_font.render('ученики "IT-cube Великий Новгород"', True, (255, 255, 255))
                screen.blit(end_text, (size[0] // 2 - 90, size[1] // 2 - 50))
                screen.blit(avtors, (size[0] // 2 - 50, size[1] // 2 + 20))
                screen.blit(name_1, (size[0] // 2 - 90, size[1] // 2 + 50))
                screen.blit(name_2, (size[0] // 2 - 90, size[1] // 2 + 80))
                screen.blit(name_3, (size[0] // 2 - 250, size[1] // 2 + 110))


    # Основная функиция класса
    def main(self):
        global number_scene

        pygame.mixer_music.play(0)
        while True:
            # Выход из игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    insert(number_scene)
                    pygame.quit()
                    sys.exit()
                
                # Переключение сцены
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        number_scene += 1
                    elif event.key == pygame.K_RIGHT:
                        number_scene += 1
                    elif event.key == pygame.K_LEFT:
                        number_scene -= 1
            
            # Вызов функции с обработкой вида сцены
            if 0 <= number_scene <= len(self.scenes) - 1:
                self.set_scene(self.scenes[number_scene])
            elif number_scene > len(self.scenes) - 1:
                number_scene = 0
            pygame.display.flip()


# Запуск игры с созданием объектов всех основных классов
if __name__ == "__main__":
    game = Game()
    rub = Rub()
    virus = Viruses_minigame()
    arcade = Arcade()
    start = Start()
    game.main()