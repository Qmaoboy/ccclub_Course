import pygame
import time
import random

pygame.init()


BGM_music_path="./assets_/music/naruto.mp3"
Fail_music_path="./assets_/music/Fail.mp3"
# 設定遊戲視窗大小和顏色
width, height = 600, 600
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
snake_block = 5 ## 5 的倍數
snake_speed = 10 ## 5 的倍數


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
        if self.x>=width:
            self.x=0
        elif self.x<0:
            self.x=width-self.block
        if self.y>=height:
            self.y=0
        elif self.y<0:
            self.y=height-self.block
    def grow(self):
        self.size += 1
        self.speed+=0.5
        
    def is_collision(self): ## 調整 Game Over State 咬到自己 Game Fail
        # if self.x >= width or self.x < 0 or self.y >= height or self.y < 0:
        if [self.x ,self.y] in self.body:
            return True 
        else:
            return False

    def draw(self):
        # print(self.x,self.y)
        # print(self.body)
        for idx,segment in enumerate(self.body):
            if idx==len(self.body)-1:
                pygame.draw.rect(window, green_blue, [segment[0], segment[1], self.block, self.block])
            else:
                pygame.draw.rect(window, green, [segment[0], segment[1], self.block, self.block])

# 定義食物類別
class Food:
    def __init__(self):
        self.block = snake_block
        self.x = round(random.randrange(0, width - self.block) / 20.0) * 20.0
        self.y = round(random.randrange(0, height - self.block) / 20.0) * 20.0
        self.color_list=[red,white,yellow,pink,dark_yellow]
        self.food_color=self.color_list[random.randint(0,len(self.color_list)-1)]
    def respawn(self):
        self.x = round(random.randrange(0, width - self.block) / 20.0) * 20.0
        self.y = round(random.randrange(0, height - self.block) / 20.0) * 20.0

    def draw(self):
        pygame.draw.rect(window, self.food_color, [self.x, self.y, self.block, self.block])

# 顯示得分
def display_score(score):
    value = font.render("Your Score: " + str(score), True, white)
    window.blit(value, [0, 0])

# 主遊戲迴圈
def game_loop():
    snake = Snake()
    food = Food()
    soundObj1 = pygame.mixer.Sound(BGM_music_path)
    soundObj1.play()
    soundObj1.set_volume(0.7)
    soundObj2 = pygame.mixer.Sound(Fail_music_path)
    soundObj2.set_volume(0.5)
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

        if snake.x == food.x and snake.y == food.y: ## 吃到食物
            food.respawn()
            snake.grow()



        if snake.is_collision():
            soundObj1.stop()
            soundObj2.play()
            game_over()
            
            
        window.fill(black)
        snake.body.append([snake.x, snake.y])
        if len(snake.body) > snake.size:
            del snake.body[0]
            
        snake.draw()
        food.draw()
        display_score(snake.size - 1)

        pygame.display.update()
        pygame.time.Clock().tick(snake_speed)

# 遊戲結束畫面
def game_over():
    window.fill(black)
    message("Game Over", pink)
    pygame.display.update()
    time.sleep(1.5)
    window.fill(black)
    message("Wanna Play Again ? (y/n)", pink)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_y:
                    window.fill(black)
                    message("Game Start in 1 second", pink)
                    time.sleep(1.5)
                    pygame.display.update()
                    game_loop()
                elif event.key==pygame.K_n:
                    pygame.quit()
                    quit()

# 顯示訊息
def message(msg, color):
    text = font.render(msg, True, color)
    window.blit(text, [0, height / 2])

if __name__ == "__main__":
    game_loop()
