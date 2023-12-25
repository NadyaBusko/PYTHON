import random
import pygame

pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определение размеров окна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Создание окна
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Быки и коровы")

# Определение шрифта
font = pygame.font.SysFont(None, 20)

def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    window.blit(text_surface, text_rect)

def generate_number():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    while (a == b):
        b = random.randint(1, 9)
    c = random.randint(1, 9)
    while (c == a or c == b):
        c = random.randint(1, 9)
    d = random.randint(1, 9)
    while (d == a or d == b or d == c):
        d = random.randint(1, 9)
    hidden = a * 1000 + b * 100 + c * 10 + d
    hidden1 = hidden // 1000
    hidden2 = hidden // 100 % 10
    hidden3 = (hidden - (hidden1 * 1000 + hidden2 * 100)) // 10
    hidden4 = hidden - (hidden1 * 1000 + hidden2 * 100 + hidden3 * 10)
    hidden_list = list()
    hidden_list.append(hidden1)
    hidden_list.append(hidden2)
    hidden_list.append(hidden3)
    hidden_list.append(hidden4)
    return hidden_list

def clear_text_area(y):
    text_rect = pygame.Rect(0, y - 20 // 2, WINDOW_WIDTH, 20)
    pygame.draw.rect(window, BLACK, text_rect)
def enter_chislo(i):
    guess = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # При нажатии Enter завершаем ввод
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:  # При нажатии Backspace удаляем последнюю цифру
                    guess = guess[:-1]
                else:
                    if len(guess) < 4:
                        guess += event.unicode  # Добавляем введенную цифру к числу

        clear_text_area(i)
        draw_text("Ваше число: " + guess, WINDOW_WIDTH // 2, i)
        pygame.display.update()
    return int(guess)
def play_game():
    hidden_list = generate_number()
    attempts = 0
    i = 60
    game_over = False
    if (attempts == 0):
        window.fill(BLACK)
        draw_text("Быки и коровы", WINDOW_WIDTH // 2, 20)
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if not game_over:
            guess = enter_chislo(i)
            guess1 = guess // 1000
            guess2 = guess // 100 % 10
            guess3 = (guess - (guess1 * 1000 + guess2 * 100)) // 10
            guess4 = guess - (guess1 * 1000 + guess2 * 100 + guess3 * 10)
            bulls = 0
            cows = 0
            guess_list = list()
            guess_list.append(guess1)
            guess_list.append(guess2)
            guess_list.append(guess3)
            guess_list.append(guess4)

            if (guess_list[0] == hidden_list[0]):
                bulls += 1
            if (guess_list[0] != hidden_list[0] and guess_list[0] in hidden_list):
                cows += 1

            if (guess_list[1] == hidden_list[1]):
                bulls += 1
            if (guess_list[1] != hidden_list[1] and guess_list[1] in hidden_list):
                cows += 1

            if (guess_list[2] == hidden_list[2]):
                bulls += 1
            if (guess_list[2] != hidden_list[2] and guess_list[2] in hidden_list):
                cows += 1

            if (guess_list[3] == hidden_list[3]):
                bulls += 1
            if (guess_list[3] != hidden_list[3] and guess_list[3] in hidden_list):
                cows += 1

            attempts += 1
            draw_text(f"Быки: {bulls}, Коровы: {cows}", WINDOW_WIDTH // 2, i+20)
            i+=60
            pygame.display.update()
            if (bulls == 4):
                draw_text(f"Поздравляю! Вы угадали число. Количество попыток = {attempts}", WINDOW_WIDTH // 2, i)
                game_over = True
                a = ""
                draw_text("1 - Новая игра", WINDOW_WIDTH // 2, i+20)
                draw_text("else - Выход", WINDOW_WIDTH // 2, i+40)
                pygame.display.update()
                input_active = True
                while input_active:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:  # При нажатии Enter завершаем ввод
                                input_active = False
                            elif event.key == pygame.K_BACKSPACE:  # При нажатии Backspace удаляем последнюю цифру
                                a = a[:-1]
                            else:
                                if len(a) < 1:
                                    a += event.unicode  # Добавляем введенную цифру к числу
                    clear_text_area(i+60)
                    draw_text("Ваш выбор: " + a, WINDOW_WIDTH // 2, i+60)
                    pygame.display.update()
                choice = int(a) if a else 0
                if choice == 1:
                    play_game()
                else:
                    return

play_game()
