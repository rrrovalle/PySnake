import pygame 
import random

pygame.init() 

#colors
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

WIDTH = 890
HEIGHT = 600  

#snake body
snake_radius = 10
snake_size   = snake_radius * 2

#game default
screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Snake game') 
pygame.mouse.set_visible(False) 

clock = pygame.time.Clock()

#message fontsize
font = pygame.font.SysFont('Comic Sans MS', 30)

def snake(snake_radius, snake_list):
    for i in snake_list:
        pygame.draw.circle(display_surface, white, [i[0], i[1]], snake_radius)


def message(input_text, color):
    text = font.render(input_text, True, color)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    display_surface.blit(text, text_rect)


def score(score):
    value = font.render("Score: " + str(score), True, white)
    display_surface.blit(value, [10,10])


def game():

    game_over = False
    game_close = False

    x1 = (((WIDTH // snake_size) // 2) * snake_size) - snake_radius
    y1 = (((HEIGHT // snake_size) // 2) * snake_size) - snake_radius

    x1_change = 0
    y1_change = 0  
    
    snake_list   = []
    snake_lenght = 1 

    food_x = round(random.randrange(snake_radius,(WIDTH // snake_size) * snake_size, snake_size))
    food_y = round(random.randrange(snake_radius,(HEIGHT // snake_size) * snake_size, snake_size)) 
 
    while not game_over:

        while game_close == True:
            screen.fill((black))
            message("Game over! Press Q to Quit or R to Restart", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True
                    if event.key == pygame.K_r:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change  

        #reset snake body after change position
        screen.fill((black))

        #create food to feed the snake (rats hehe)
        pygame.draw.circle(display_surface,green, [food_x,food_y], snake_radius)
       
        #list of eaten rats
        snake_list.append((x1,y1))

        if len(snake_list) > snake_lenght:
            del snake_list[0]

        #check if she hit his on body
        snake_head = []
        snake_head.append((x1,y1))

        for i in snake_list[:-1]:
            for j in snake_head:
                if i == j:
                    game_close = True

        #draw a brand new snake :D
        snake(snake_radius, snake_list)
        score(snake_lenght - 1)

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(snake_radius, WIDTH - snake_radius, snake_size))
            food_y = round(random.randrange(snake_radius, HEIGHT - snake_radius, snake_size))
            snake_lenght += 1 

        pygame.display.update()

        #set snake speed
        clock.tick(20) 

game()



