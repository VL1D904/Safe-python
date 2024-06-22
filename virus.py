# Импортируем необходимые библиотеки
import pygame
import threading
import sys
from random import randint, uniform
import time

# импортируем содержимое из главного (main) файла
import main

# Создание группы спрайтов вирусов
virus_sprites = pygame.sprite.Group()

# Переменная ответственная за состояние второго потока
thread = True


# Функция для создания второго потока
def run_in_thread(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


# Класс кнопки перезапуска
class Restart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/restart.png')
        self.image = pygame.transform.scale(self.image, (200, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (main.size[0] // 2, main.main.size[1] // 2)


# Класс спрайта вируса
class Viruses(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Рандомные размеры картинки и рандомная картинка
        self.size = randint(150, 250)
        self.image = pygame.transform.scale(pygame.image.load(f'images/virus{randint(0, 2)}.png'), (self.size, self.size))
        self.rect = self.image.get_rect()

        # Алгоритм для избежания накладок спрайтов
        while True:
            self.rect.topleft = (
                randint(0, 900 - self.size),
                randint(0, 750 - self.size))
            if not pygame.sprite.spritecollideany(self, virus_sprites):
                virus_sprites.add(self)
                break
        
        # Добавление спрайта в группу
        virus_sprites.add(self)


# Класс миниигры
class Viruses_minigame():
    def __init__(self):
        # Установка счета
        self.score = 0

        # Рандомная установка кол-ва вирусов и с какой задержкой каждый появится
        self.list_viruses = [uniform(0.1, 1.5) for _ in range(randint(50, 100))]

        # Установка заднего фона
        self.bg = pygame.transform.scale(pygame.image.load('images/bg_virus.jpeg'), (900, 750))
        self.bg_rect = self.bg.get_rect()

        # Переменные отвечающие за победу/проигрыш
        self.restart = None
        self.win = True
        self.stop = False
        self.button_restart = False

    # Функция второго потока появления вирусов
    @run_in_thread
    def draw_virus(self):
        # Создание нового спрайта вируса и задержка перед следующем при активном состоянии игры
        for virus in self.list_viruses:
            if not thread:
                return
            time.sleep(virus)
            Viruses()
        
        # Остановка потока пока не исчезли оставшиеся спрайты
        while virus_sprites:
            time.sleep(0.1)

        # Определение победы/поражения
        self.win = self.stop = self.score >= len(self.list_viruses) * 60

    # Функция отрисовки
    def draw(self):
        # Отрисовка заднего фона
        main.screen.fill('black')
        main.screen.blit(self.bg, self.bg_rect)

        # Отрисовка счета
        text = main.font.render(str(self.score), True, (255, 255, 255))
        main.screen.blit(text, (10, 10, 200, 200))

        # Отрисовка спрайтов
        virus_sprites.draw(main.screen)

        # Определение объекта переигрывания при необходимости
        if not self.win:
            self.restart = Restart()
            self.button_restart = True
            self.win = True

        # Отображение кнопки restart'а если таковая имеется
        try:
            main.screen.blit(self.restart.image, self.restart.rect)
        except:
            pass

    # Основная функция миниигры
    def main(self):
        # Обнуление переменных
        self.score = 0
        self.restart = None
        self.win = True
        self.stop = False
        self.button_restart = False

        # вызов функции добавления вирусов
        self.draw_virus()

        # Основной цикл
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Выход и остановка второго потока
                    global thread
                    thread = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Попадание по вирусы
                    for sprite in virus_sprites:
                        if sprite.rect.collidepoint(event.pos):
                            self.score += 100
                            sprite.kill()
                if event.type == pygame.MOUSEBUTTONDOWN and self.button_restart:
                    # Перезапуск миниигры
                    if self.restart.rect.collidepoint(event.pos):
                        self.score = 0
                        self.draw_virus()
                        self.restart.kill()
                        self.restart = None

            # Завершение миниигры
            if self.stop:
                return
            
            # Вызов функции отрисовки
            self.draw()

            # Исчезновение вирусов
            for virus in virus_sprites:
                virus.size -= .15
                if virus.size <= 0:
                    virus.kill()

            pygame.display.flip()
