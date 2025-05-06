import pygame

pygame.init()


class Node2D:
    def __init__(self, screen, x: int = 0, y: int = 0, size: int = 1) -> None:
        self.screen = screen
        self.prev = None
        self.next = None
        self.x: int = x
        self.y: int = y
        self.color: tuple = (0, 0, 0)
        self.size: float = size

    def draw(self) -> None:
        # Поле ввода
        pygame.draw.rect(self.screen, self.color, input_rect, 2)

    def _process(self) -> None:
        pass


# Настройки окна
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Ввод текста")
font = pygame.font.Font(None, 32)  # Шрифт для отображения текста

# Переменные для текста
input_text = ""
active = False  # Активно ли поле ввода
color_inactive = pygame.Color("lightskyblue3")
color_active = pygame.Color("dodgerblue2")
color = color_inactive

# Прямоугольник для поля ввода
input_rect = pygame.Rect(100, 50, 200, 32)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Активация поля ввода по клику
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
            color = color_active if active else color_inactive

        # Обработка ввода текста
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_RETURN:  # Enter - завершить ввод
                print("Введённый текст:", input_text)
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:  # Backspace - удалить символ
                input_text = input_text[:-1]
            else:
                input_text += event.unicode  # Добавляем символ

    # Отрисовка
    screen.fill((30, 30, 30))

    # Поле ввода
    pygame.draw.rect(screen, color, input_rect, 2)

    # Текст
    text_surface = font.render(input_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # Подпись
    label = font.render("Введите текст:", True, (255, 255, 255))
    screen.blit(label, (input_rect.x, input_rect.y - 30))

    pygame.display.flip()

pygame.quit()
