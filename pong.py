import pygame
import sys
pygame.font.init()
FPS = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
BAT_WIDTH = 20
BAT_HEIGHT = 120
BAT_OFFSET = 10
ROK_WIDTH = 20
ROK_HEIGHT = 120
ROK_OFFSET = 30
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
score_left_text = 0
score_right_text = 0
#отталкивание мяча от ракеток
def point_in_rect(pointx, pointy, rectx, recty, rect_width, rect_height):
    inx = rectx <= pointx <= rectx <= + rect_width
    iny = recty <= pointy<= recty + rect_height
    
clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))

r = 20
# координаты круга
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
#скорости мячя
ball_speed_x = 3
ball_speed_y = 1
#координаты ракетки
#левая
bat_x = BAT_OFFSET
bat_y = (SCREEN_HEIGHT - BAT_HEIGHT) // 2
#правая
rok_x = SCREEN_WIDTH - ROK_OFFSET
rok_y = (SCREEN_HEIGHT - ROK_HEIGHT) // 2
#score
f2 = pygame.font.SysFont('algerian', 48)
left_score = 0
right_score = 0

#скорость ракетки
bat_speed_y = 0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #передвигаем мяч по экрану
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    #выход за края экрана
    #левый
    if ball_x <= r:
        ball_speed_x = -ball_speed_x
        right_score += 1
        
    #правый
    if ball_x >= SCREEN_WIDTH -r:
        
        #летел на право-полетел на лево
        ball_speed_x = -ball_speed_x
    if ball_y <= r:
        ball_speed_y = -ball_speed_y
        left_score += 1
    #правый
    if ball_y >= SCREEN_HEIGHT -r:
        #летел на право-полетел на лево
        ball_speed_y = -ball_speed_y
    #передвигаем ракетку по экрану
    #левая
    keys = pygame.key.get_pressed()
    bat_y +=bat_speed_y
    if keys[pygame.K_w]:
        bat_y -= 3
    elif keys[pygame.K_s ]:
        bat_y += 3
    if bat_y <= 0:
        bat_y = 0
    elif bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        bat_y = SCREEN_HEIGHT - BAT_HEIGHT
    #правая
        keys = pygame.key.get_pressed()
    bat_y +=bat_speed_y
    if keys[pygame.K_UP]:
        rok_y -= 3
    elif keys[pygame.K_DOWN ]:
        rok_y += 3
    if rok_y <= 0:
        rok_y = 0
    elif rok_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        rok_y = SCREEN_HEIGHT - BAT_HEIGHT
    # проверяем попал ли мяч в ракетку
    #вычесляем середины сторон квадрата описаного вокруг мяча
    mid_leftx = ball_x - r
    mid_lefty = ball_y
    
    mid_rightx = ball_x + r
    mid_righty =  ball_y
    
    mid_topx = ball_x
    mid_topy = ball_y - r
    
    mid_bottomx = ball_x
    mid_bottomy = ball_y - r
    
    #правая граница
    if point_in_rect(mid_leftx, mid_lefty, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball_speed_x = -ball_speed_x
        
    #верхняя граница    
    if point_in_rect(mid_leftx, mid_lefty, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball_speed_y = -ball_speed_x
        
    #нижняя граница
    if point_in_rect(mid_topx, mid_topy, bat_x, bat_y,
                     BAT_WIDTH, BAT_HEIGHT):
        ball_speed_y = -ball_speed_x
    #счётчик баллов
    score_left_text  = f2.render(str(left_score), True,(255, 180, 0))
    # заливаем фон
    sc.fill(WHITE)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    #рисуем ракетки
    pygame.draw.rect(sc, ORANGE, (bat_x, bat_y, BAT_WIDTH, BAT_HEIGHT))
    pygame.draw.rect(sc, ORANGE, (rok_x, rok_y, ROK_WIDTH, ROK_HEIGHT))
    # обновляем окно
    sc.blit(score_left_text, (10, 100))
    pygame.display.update()
    clock.tick(FPS)
