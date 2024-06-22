# Импортируем необходимые библиотеки
import pygame
import sys

# импортируем наше игровое окно и его размеры из главного (main) файла
from main import screen, size

# Создаем группы спрайтов для монеток и троллей
troll_group = pygame.sprite.Group()
money_group = pygame.sprite.Group()


# Класс спрайта монетки
class Money(pygame.sprite.Sprite):
    # Передаем при инициализации объекта класса позицию по х, у, картинку и к каким размерам ее преобразовать
    def __init__(self, x, y, image, scale):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        money_group.add(self)


# Класс спрайта тролля
class Troll(pygame.sprite.Sprite):
    # Передаем при инициализации объекта класса позицию по х, у, картинку и к каким размерам ее преобразовать
    # Также скорость смещение по х, координату столкновения с монеткой и к какой монетке принадлежит объект
    def __init__(self, x, y, image, speed, scale, coord, money):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.money_x = coord
        self.money = money
        troll_group.add(self)


# Класс Героя
class Hero(pygame.sprite.Sprite):
    # Установка картинки с размерами и позицией по центру
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/hero.png'), (60, 100))
        self.rect = self.image.get_rect()
        self.rect.x = size[0] // 2 - 60
        self.rect.y = size[1] - 100


# Основной класс события
class Rub():
    def __init__(self):
        # Создание объектов классов
        self.hero = Hero()
        self.money_1 = Money(200, 120, 'images/money1.jpg', (70, 70))
        self.money_2 = Money(600, 350, 'images/money2.jpg', (50, 70))
        self.money_3 = Money(400, 220, 'images/money3.jpg', (70, 70))
        self.troll_1 = Troll(-100, 100, 'images/troll2.png', 5, (100, 100), 150, self.money_1)
        self.troll_2 = Troll(900, 200, 'images/troll1.png', -20, (70, 100), 400, self.money_3)
        self.troll_3 = Troll(-100, 350, 'images/troll2.png', 10, (100, 100), 550, self.money_2)
        self.clock = pygame.time.Clock()

    # Отрисовка экрана
    def draw(self):
        screen.fill('black')
        bg = pygame.transform.scale(pygame.image.load('images/bg_rub.gif'), (900, 750))
        bg_rect = bg.get_rect()
        screen.blit(bg, bg_rect)
        screen.blit(self.hero.image, self.hero.rect)
        money_group.draw(screen)
        troll_group.draw(screen)

        # Действия с троллями
        for sprite in troll_group:
                # обработка столкновения с монеткой
                if sprite.rect.x == sprite.money_x:
                    sprite.money.kill()
                # Перемещение с троллями
                sprite.rect.x += sprite.speed

    # Основная функция Класса
    def main(self):
        while True:
            for event in pygame.event.get():
                # Выход
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Передвижения по экрану героя
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_UP:
                            self.hero.rect.y -= 10
                        case pygame.K_DOWN:
                            self.hero.rect.y += 10
                        case pygame.K_RIGHT:
                            self.hero.rect.x += 10
                        case pygame.K_LEFT:
                            self.hero.rect.x -= 10

            # Завершение события
            if not money_group:
                return -1
            
            self.draw()

            self.clock.tick(30)
            pygame.display.flip()
