import pygame, sys, time, random

from pygame.locals import *
pygame.init()

#screen settings
pygame.display.set_caption('Isometric Rendering')
screen = pygame.display.set_mode((500,500),0,32)
display = pygame.Surface((300,300))

#img settings
grass_img = pygame.image.load('data/grass.png').convert()
grass_img.set_colorkey((0,0,0)) 

f = open('data/map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()  

def start():
    while True:
        display.fill((0,0,0)) 
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile:
                    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                    display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))
                    if random.randint(0,1):
                        display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5 - 14))


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                        
        screen.blit(pygame.transform.scale(display, screen.get_size()),(0,0))
        pygame.display.update() 
        time.sleep(1)

if __name__ == '__main__':
    start()