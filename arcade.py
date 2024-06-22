# Импортируем необходимые библиотеки
import pygame
import sys


# Создаем экран для лабиринта
pygame.init()
pygame.display.set_caption('safe_python')
size = 900, 750
screen = pygame.display.set_mode(size)
text_font = pygame.font.Font('plot/font.otf', 16)
game = True

# Таблица с клеточками поля
TABLE_ZONE = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 4, 0, 0, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Словарь вопросов
QUESTION = {
    1: 'Можно ли доверять незнакомцам, которые просят личную информацию в интернете?',
    2: 'Нужно ли использовать разные пароли для разных учетных записей?',
    3: 'Можно ли удалить вирус, просто удалив зараженный файл?',
    4: 'Нужно ли регулярно обновлять антивирусное программное обеспечение?'
}

# Установка лабиринта
scene = pygame.image.load('images/bg_arcade.png')
scene_rect = scene.get_rect()
scene_rect.y = -3000
scene_rect.x = -250

# Класс главного героя
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('images/hero.png'), (80, 120))
        self.rect = self.image.get_rect()
        self.rect.x = size[0] // 2
        self.rect.y = size[1] - 120
        # Опредление позиции относительно клеточек
        self.pos = [32, 9]

    # Функция его передвижения
    def move(self, coord, score, size_screen, step):
        # Изменение координаты положения в клетке
        self.pos[coord] += score 

        # Проверка не является ли клетка стеной
        if TABLE_ZONE[self.pos[0]][self.pos[1]] == 1 or not 0 <= self.pos[0] <= 32 or not 0 <= self.pos[1] <= 17:
            self.pos[coord] -= score
            return
        
        # Вызов функции отображения вопрос
        if 2 <= TABLE_ZONE[self.pos[0]][self.pos[1]] <= 5:
            arcade.question(TABLE_ZONE[self.pos[0]][self.pos[1]])

        # Выход с лабиринта
        if TABLE_ZONE[self.pos[0]][self.pos[1]] == 6:
            global game
            game = False

        # Перемещение героя или лабиринта относительно экрана
        if step < self.rect[not coord] + step * score <= size_screen - step:
            self.rect[not coord] += step * score
        else:
            scene_rect[not coord] -= step * score

# Класс миниигры
class Arcade():
    def __init__(self) -> None:
        self.hero = Hero()

    # Отрисовка
    def draw(self):
        screen.fill('black')
        screen.blit(scene, scene_rect,)
        screen.blit(self.hero.image, self.hero.rect)

    # Отображение вопросов
    def question(self, num):
            # Основная отрисовка
            self.draw()

            # Отрисовка вопросв
            rect = pygame.Surface((900, 150))
            rect.set_alpha(220)
            rect.fill((32, 32, 32))
            screen.blit(rect, (0, 600))

            text_hero = text_font.render(QUESTION[num - 1], True, (255, 255, 255))
            screen.blit(text_hero, (30, 650))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # выход из игры
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                        # Закрытие вопроса
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            return
                        elif event.key == pygame.K_RIGHT:
                            return

                pygame.display.flip()
            
    def main(self):
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Выход
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Передвижение героя
                    match event.key:
                        case pygame.K_UP:
                            self.hero.move(0, -1, 750, 120)
                        case pygame.K_DOWN:
                            self.hero.move(0, 1, 750, 120)
                        case pygame.K_RIGHT:
                            self.hero.move(1, 1, 900, 80)
                        case pygame.K_LEFT:
                            self.hero.move(1, -1, 900, 80)
            # Отрисовка и обновление экрана
            self.draw()
            pygame.display.flip()

# Создание объекта основного класса
arcade = Arcade()