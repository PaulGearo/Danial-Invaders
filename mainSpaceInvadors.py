import pygame

windowWidth = 900
windowHeight = 1000

black = (0,0,0)
white = (255,255,255)
blue = (40,80,255)

pygame.init()

gameDisplay = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption('Danial Invaders')

class GameObject(object):
    def __init__(self, xcor, ycor, image, speed):
        self.xcor = xcor
        self.ycor = ycor
        self.img = image
        self.speed = speed
        self.width = image.get_width()
        self.height = image.get_height()
    def show(self):
        gameDisplay.blit(self.img, (self.xcor, self.ycor))

class Player(GameObject):
    def __init__(self, xcor, ycor, image, speed):
        super().__init__(xcor, ycor, image, speed)
        self.is_alive = True
        self.direction = 0
    def show(self):
        new_xcor = self.xcor + self.direction * self.speed
        if new_xcor < 0 or new_xcor > windowWidth - self.width:
            self.xcor = self.xcor
        else:
            self.xcor = new_xcor
        super().show()
    def move_right(self):
        self.direction = 1
    def move_left(self):
        self.direction = -1
    def stop_moving(self):
        self.direction = 0

class Enemy(GameObject):
    def __init__(self, xcor, ycor, image, speed):
        super().__init__(xcor, ycor, image, speed)  
        self.direction = 1
    def move_over(self):
        self.xcor += self.direction * self.speed
    def move_down(self):
        self.ycor += 15
    def change_direction(self):
        self.direction *= -1

clock = pygame.time.Clock()

playerImg = pygame.image.load("daniel-headshot.png")
enemyImg = pygame.image.load("definitely-not-daniel.png")

player1 = Player(200, 870, playerImg, 5)

enemies = []

for x in range(0,5):
    newEnemy = Enemy((enemyImg.get_width() + 5) * x + 1, 10, enemyImg, 2)
    enemies.append(newEnemy)

while player1.is_alive:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player1.is_alive = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.move_left()
            elif event.key == pygame.K_RIGHT:
                player1.move_right()

    gameDisplay.blit(gameDisplay, (0,0))
    gameDisplay.fill(black)

# check all enimies to see if one has rached a wall
    for enemy in enemies:
        if enemy.xcor <= 0 or enemy.xcor >= windowWidth - enemy.width:
            #since one enemy has reached a wall, change all enimies directions
            for e in enemies:
                e.change_direction()
                e.move_down()
            # since one enemy has reached a wall, stop checking the others
            break

     # move and show all enemies       
    for enemy in enemies:
        enemy.move_over()
        enemy.show()



    player1.show()

 
    pygame.display.update()

    clock.tick(60)









pygame.quit()