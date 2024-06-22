# Импортируем необходимые библиотеки
import pygame
import sys
import sqlite3

# импортируем наше игровое окно из главного (main) файла
from main import screen


# Функция для получения последней сцены из БД
def select():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    res = cur.execute('SELECT scene FROM Scenes').fetchall()[-1][0]
    con.close()
    return res


# Класс со стартовым окном
class Start:
    def __init__(self):
        # Задний фон и кнопки
        self.background = pygame.image.load('images/start.png')
        self.background_rect = self.background.get_rect()

        self.start_button = pygame.image.load('images/new_game.png')
        self.start_button = pygame.transform.scale(pygame.image.load('images/new_game.png'), (240, 180))
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.center = (330, 550)

        self.continue_button = pygame.image.load('images/continue.png')
        self.continue_button = pygame.transform.scale(pygame.image.load('images/continue.png'), (240, 180))
        self.continue_button_rect = self.continue_button.get_rect()
        self.continue_button_rect.center = (630, 550)

    # Отрисовка
    def draw(self):
        screen.blit(self.background, self.background_rect)
        screen.blit(self.start_button, self.start_button_rect)
        screen.blit(self.continue_button, self.continue_button_rect)

    def main(self):
        global number_scene
        while True:
            for event in pygame.event.get():
                # Выход
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Новая игра
                    if self.start_button_rect.collidepoint(event.pos):
                        # Установка 1 (начальной) сцены
                        number_scene = 1
                        return number_scene
                    # Продолжить игру
                    if self.continue_button_rect.collidepoint(event.pos):
                        # Получение последней сцены из БД
                        number_scene = select()
                        return number_scene
                    
            self.draw()
            pygame.display.flip()