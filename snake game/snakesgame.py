import pygame
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("bgm.mp3")
pygame.mixer.music.play()

# colours
red = (255, 0, 0)  # fill rgb values for colours here
black = (0, 0, 0)  # fill rgb values for colours here
white = (255, 255, 255)  # fill rgb values for colours here
blue = (0,0,255)
green = (0,255,0)
orange = (255,115,12)
yellow = (255,255,0)
pink = (200,112,167)
maroon = (223,210,229)

screen_width = 900
screen_height = 600

# creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snakes Game made by SARANG RAO")
pygame.display.update()
clock = pygame.time.Clock()  # defining clock
font = pygame.font.SysFont(None, 50)



bg = pygame.image.load("download.jpg")
bg = pygame.transform.scale(bg, (screen_width, screen_height)).convert_alpha()




def text_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))


def snake_plot(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def start():

    exit_game = False
    game_over = False
    # exit_game = False
    while( not exit_game):
        gameWindow.fill(maroon)
        gameWindow.blit(bg ,(0,0))
    
        text_score("Welcome to mine PYGAME project.",red,100,100)
        text_score("I AM Sarang Rao from PICT ECE, FY3. ",red,100,150)

        text_score("Controls:-",blue,100,300)    
        text_score("press WASD for snake movement",red,100,350)

        text_score("Press Enter to Enter the Game",red,100,400)
        text_score("Press Escape to quit",red,100,450)

        text_score("If someone reaches 250+ points in this",orange,100,500)
        text_score(" game, send me pic, you will get",orange,100,530)
        text_score("special credit.",orange,100,560)
      

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    pygame.mixer.music.load("bgm.mp3")
                    pygame.mixer.music.play()

                    gameloop()

def gameloop():
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play()
    with open("high_score.txt","r") as f:
        high_score = f.read()
    # game loop
    # game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 35
    snake_size = 20
    food_size = 15
    fps = 40
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(100, screen_width - 100)
    food_y = random.randint(100, screen_height-100)
    score = 0
    init_velocity = 10

    clock = pygame.time.Clock()  # defining clock
    font = pygame.font.SysFont(None, 30)

    snake_list = []
    snake_length = 1

    while not exit_game:
        
        if game_over:
            gameWindow.fill(maroon)
            text_score("Game Over : Press Enter to continue",red,100,300)
            text_score("Press escape to quit.",red,100,350)
            text_score("Credits:- Sarang Rao PICT ECE FY3",red,100,500)
            with open("high_score.txt","w") as f:
                f.write(str(high_score))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("bgm.mp3")
                        pygame.mixer.music.play()
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        # snake_x += 10
                        velocity_x = init_velocity
                        velocity_y = 0
                        pygame.mixer.music.load("move.mp3")
                        pygame.mixer.music.play()

                    if event.key == pygame.K_a:
                        # snake_x -= 10
                        velocity_x = -init_velocity
                        velocity_y = 0
                        pygame.mixer.music.load("move.mp3")
                        pygame.mixer.music.play()

                    if event.key == pygame.K_w:
                       
                        velocity_y = -init_velocity
                        velocity_x = 0
                        pygame.mixer.music.load("move.mp3")
                        pygame.mixer.music.play()

                    if event.key == pygame.K_s:
                        velocity_y = +init_velocity
                        velocity_x = 0
                        pygame.mixer.music.load("move.mp3")
                        pygame.mixer.music.play()

            snake_y += velocity_y
            snake_x += velocity_x

            if (abs(snake_x - food_x) < 8) and (abs(snake_y - food_y) < 12):
                score += 10
                snake_length +=1
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                pygame.mixer.music.load("food.mp3")
                pygame.mixer.music.play()
                if score > int(high_score):
                    high_score = score

            gameWindow.fill(yellow)
            text_score(("Score: " + str(score) + "   Highscore: " + str(high_score)), red, 5, 5)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
         
            if snake_x < 0 or snake_x > screen_width or snake_y<0 or snake_y > screen_height:
                game_over = True
              
            snake_plot(gameWindow, black, snake_list, snake_size)
            pygame.draw.rect(gameWindow, blue, [food_x, food_y, food_size, food_size])
        pygame.display.update()  # after any change in display we need to update the display so that we can see the changes made by us.
        clock.tick(fps)

    pygame.quit()
    quit()



start()