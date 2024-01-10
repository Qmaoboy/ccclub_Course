import pygame
import time
import random

pygame.init()

# 設定遊戲視窗大小和顏色
width, height = 400, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Greedy Snake Game")

# 定義顏色
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,87)
pink = (255,140,250)
green_blue = (10,209,139)
grey = (150,150,150)
grey2 = (130,130,130)
dark_yellow = (228,128,16)

# 設定字體和文字大小
font = pygame.font.SysFont(None, 35)

# 設定貪食蛇和食物的大小
snake_block = 20
snake_speed = 15
FPS=15


# 定義貪食蛇類別
class Snake:
    def __init__(self):
        self.size = 1
        self.block = snake_block
        self.speed = snake_speed
        self.direction = 'RIGHT'
        self.x = width / 2
        self.y = height / 2
        self.body = []

    def move(self):
        if self.direction == 'RIGHT':
            self.x += self.block
        elif self.direction == 'LEFT':
            self.x -= self.block
        elif self.direction == 'UP':
            self.y -= self.block
        elif self.direction == 'DOWN':
            self.y += self.block

    def grow(self):
        self.size += 1

    def is_collision(self):
        return self.x >= width or self.x < 0 or self.y >= height or self.y < 0

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(window, green, [segment[0], segment[1], self.block, self.block])

# 定義食物類別
class Food:
    def __init__(self):
        self.block = snake_block
        self.x = round(random.randrange(0, width - self.block) / 20.0) * 20.0
        self.y = round(random.randrange(0, height - self.block) / 20.0) * 20.0

    def respawn(self):
        self.x = round(random.randrange(0, width - self.block) / 20.0) * 20.0
        self.y = round(random.randrange(0, height - self.block) / 20.0) * 20.0

    def draw(self):
        pygame.draw.rect(window, red, [self.x, self.y, self.block, self.block])

# 顯示得分
def display_score(score):
    value = font.render("Your Score: " + str(score), True, white)
    window.blit(value, [0, 0])

# 主遊戲迴圈
def game_loop():
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'
                elif event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'

        snake.move()

        if snake.x == food.x and snake.y == food.y:
            food.respawn()
            snake.grow()

        window.fill(black)
        snake.body.append([snake.x, snake.y])
        if len(snake.body) > snake.size:
            del snake.body[0]

        if snake.is_collision():
            game_over()
        
        snake.draw()
        food.draw()
        display_score(snake.size - 1)

        pygame.display.update()
        pygame.time.Clock().tick(snake.speed)

# 遊戲結束畫面
def game_over():
    window.fill(black)
    message("Game Over", red)
    pygame.display.update()
    time.sleep(3)
    while True:
        message("Wanna Play Again ? (y/n)", red)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_y:
                    message("Game Start in 3 second", pink)
                    pygame.display.update()
                    game_loop()
                else:
                    pygame.quit()
                    quit()

# 顯示訊息
def message(msg, color):
    text = font.render(msg, True, color)
    window.blit(text, [width / 2, height / 2])

if __name__ == "__main__":
    game_loop()
