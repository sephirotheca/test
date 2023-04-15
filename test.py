
import pygame
import random

# 初始化pygame
pygame.init()

# 设置游戏窗口大小
screen_width = 480
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置游戏标题
pygame.display.set_caption("贪吃蛇小游戏")

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 定义蛇的初始位置和大小
snake_size = 10
snake_x = screen_width / 2
snake_y = screen_height / 2

# 定义蛇的移动速度
snake_speed = 1

# 定义食物的初始位置和大小
food_size = 10
food_x = round(random.randrange(0, screen_width - food_size) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - food_size) / 10.0) * 10.0

# 定义蛇的移动方向
direction = "right"

# 定义游戏结束标志
game_over = False

# 定义游戏时钟
clock = pygame.time.Clock()

# 定义绘制蛇的函数
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_size, snake_size])

# 定义游戏循环
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"

    # 移动蛇的位置
    if direction == "right":
        snake_x += snake_speed
    elif direction == "left":
        snake_x -= snake_speed
    elif direction == "up":
        snake_y -= snake_speed
    elif direction == "down":
        snake_y += snake_speed

    # 判断蛇是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - food_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - food_size) / 10.0) * 10.0

    # 绘制游戏背景
    screen.fill(white)

    # 绘制食物
    pygame.draw.rect(screen, red, [food_x, food_y, food_size, food_size])

    # 绘制蛇
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list = []
    snake_list.append(snake_head)
    draw_snake(snake_size, snake_list)

    # 更新游戏显示
    pygame.display.update()

    # 设置游戏时钟
    clock.tick(30)

# 退出pygame
pygame.quit()





