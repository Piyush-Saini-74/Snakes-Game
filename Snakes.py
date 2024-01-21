import pygame
import random

pygame.init()

# Colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 900
screen_height = 600

# Creating window
gameWinndow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()
# variable which defines font colour and size. Here colour is default and size is 55.
font = pygame.font.SysFont(None, 55)

# This function defines the text score over the screen.
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWinndow.blit(screen_text, [x,y])

def plot_snake(gameWinndow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWinndow, color, [x, y, snake_size, snake_size])

# This functions defines the welcome screen
def welcome_screen():
    exit_game = False
    while not exit_game:
        gameWinndow.fill((170, 255, 160))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Spacebar to play", black, 230, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(60)

# Game Loop
def game_loop():

    # Game specific variables
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 4

    food_x = random.randint(30, screen_width - 30)
    food_y = random.randint(30, screen_height - 40)
    score = 0

    snake_size = 20
    fps = 60

    snk_list = []
    snk_length = 1
   
    # For displaying high Score
    with open("highscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWinndow.fill(white)
            text_screen("Game Over! Press Enter to Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        velocity_x = -init_velocity
                        velocity_y = 0


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        velocity_y = -init_velocity
                        velocity_x = 0


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            # Defines the distance of Eat food at touching it .
            if abs(snake_x - food_x)<12 and abs(snake_y - food_y)<12:
                score += 10
                food_x = random.randint(30, screen_width - 30)
                food_y = random.randint(30, screen_height - 40)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score

            gameWinndow.fill((250, 250, 150))
            text_screen("Score " + str(score) + "  Highscore: " + str(hiscore),red,5,5)
            pygame.draw.rect(gameWinndow, red, [food_x, food_y, snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True 

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True

            plot_snake(gameWinndow, black, snk_list , snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()  
    quit()

welcome_screen()
