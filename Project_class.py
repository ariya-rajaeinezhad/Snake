import random, pygame, sys
from pygame.locals import *

FPS = 7
WINwidth = 1280
WINheight = 680
CELLsize = 20
assert WINwidth % CELLsize == 0
assert WINheight % CELLsize == 0
CELLwidth = WINwidth // CELLsize
CELLheight = WINheight // CELLsize

DARKGREEN = "#006400"
WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#FF0000"
DARKRED = "#8B0000"
GREEN = "#18ff00"
DARKGRAY = "#A9A9A9"
ORANGE = "#FFA500"
YELLOW = "#ffd932"
BGCOLOR = GREEN

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

HEAD = 0


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINwidth, WINheight))
    BASICFONT = pygame.font.Font("freesansbold.ttf", 30)
    pygame.display.set_caption("SNAKE")

    showstartscreen()

    while True:
        rungame()
        showgameoverscreen()


def spawn_grass(count=90, clusters=10):

    grass = []

    for _ in range(clusters):
        cx = random.randint(0, CELLwidth - 1)
        cy = random.randint(0, CELLheight - 1)

        for _ in range(random.randint(6, 12)):
            gx = cx + random.randint(-2, 2)
            gy = cy + random.randint(-2, 2)

            if 0 <= gx < CELLwidth and 0 <= gy < CELLheight:
                grass.append({
                    "x": gx,
                    "y": gy,
                    "offset": random.random() * 6.28  
                })

    while len(grass) < count:
        grass.append({
            "x": random.randint(0, CELLwidth - 1),
            "y": random.randint(0, CELLheight - 1),
            "offset": random.random() * 6.28
        })

    return grass


def draw_grass_patches(surface, patches):

    t = pygame.time.get_ticks() * 0.002

    for g in patches:
        x = g["x"] * CELLsize
        y = g["y"] * CELLsize

        vec = pygame.math.Vector2(1, 0).rotate_rad(t + g["offset"])
        sway = int(2 * vec.x)  

        pygame.draw.line(
            surface, (30, 140, 30),
            (x + 10, y + 18),
            (x + 10 + sway, y + 6),
            2
        )
        pygame.draw.line(
            surface, (50, 180, 50),
            (x + 13, y + 18),
            (x + 13 + sway, y + 8),
            2
        )
        pygame.draw.line(
            surface, (20, 120, 20),
            (x + 7, y + 18),
            (x + 7 + sway, y + 9),
            2
        )


def rungame():
    startx = random.randint(5, CELLwidth - 5)
    starty = random.randint(5, CELLheight - 5)
    snakecoords = [
        {"x": startx, "y": starty},
        {"x": startx - 1, "y": starty},
        {"x": startx - 2, "y": starty}
    ]
    direction = RIGHT

    apple = getRandomLocation()

    grass_patches = spawn_grass(90, clusters=10)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if (event.key in (K_LEFT, K_a)) and direction != RIGHT:
                    direction = LEFT
                elif (event.key in (K_RIGHT, K_d)) and direction != LEFT:
                    direction = RIGHT
                elif (event.key in (K_UP, K_w)) and direction != DOWN:
                    direction = UP
                elif (event.key in (K_DOWN, K_s)) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        headX = snakecoords[HEAD]["x"]
        headY = snakecoords[HEAD]["y"]

        if headX < 0 or headX >= CELLwidth or headY < 0 or headY >= CELLheight:
            return

        for block in snakecoords[1:]:
            if block["x"] == headX and block["y"] == headY:
                return

        if headX == apple["x"] and headY == apple["y"]:
            apple = getRandomLocation()
        else:
            del snakecoords[-1]

        if direction == UP:
            newhead = {"x": headX, "y": headY - 1}
        elif direction == DOWN:
            newhead = {"x": headX, "y": headY + 1}
        elif direction == LEFT:
            newhead = {"x": headX - 1, "y": headY}
        else:
            newhead = {"x": headX + 1, "y": headY}

        snakecoords.insert(0, newhead)

        DISPLAYSURF.fill(GREEN)

        draw_grass_patches(DISPLAYSURF, grass_patches)

        drawGrid()
        drawsnake(snakecoords)
        drawApple(apple)
        drawscore(len(snakecoords) - 3)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawPressKeyMsg():
    presskeysurf = BASICFONT.render("press a key to play", True, BLACK)
    rect = presskeysurf.get_rect()
    rect.bottomright = (WINwidth - 20, WINheight - 10)
    DISPLAYSURF.blit(presskeysurf, rect)


def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            return event.key
    return None


def showstartscreen():
    titlefont = pygame.font.Font("freesansbold.ttf", 130)
    titlesurf1 = titlefont.render("snake!", True, DARKGREEN)
    titlesurf2 = titlefont.render("snake!", True, DARKGREEN)
    titlesurf3 = titlefont.render("snake!", True, GREEN)

    degrees1 = 0
    degrees2 = 0
    degrees3 = 0

    while True:
        DISPLAYSURF.fill(WHITE)

        rotate1 = pygame.transform.rotate(titlesurf1, degrees1)
        rect1 = rotate1.get_rect(center=(WINwidth // 2, WINheight // 2))
        DISPLAYSURF.blit(rotate1, rect1)

        rotate2 = pygame.transform.rotate(titlesurf2, degrees2)
        rect2 = rotate2.get_rect(center=(WINwidth // 2, WINheight // 2))
        DISPLAYSURF.blit(rotate2 , rect2)

        rotate3 = pygame.transform.rotate(titlesurf3, degrees3)
        rect3 = rotate3.get_rect(center=(WINwidth // 2, WINheight // 2))
        DISPLAYSURF.blit(rotate3, rect3)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()
            return

        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {"x": random.randint(0, CELLwidth - 1),
            "y": random.randint(0, CELLheight - 1)}


def showgameoverscreen():
    font = pygame.font.Font("freesansbold.ttf", 200)
    gamesurf = font.render("GAME", True, RED)
    oversurf = font.render("OVER", True, RED)

    gamerect = gamesurf.get_rect(midtop=(WINwidth // 2, 10))
    overrect = oversurf.get_rect(midtop=(WINwidth // 2, gamerect.height + 35))

    DISPLAYSURF.blit(gamesurf, gamerect)
    DISPLAYSURF.blit(oversurf, overrect)

    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return


def drawscore(score):
    surf = BASICFONT.render(f"score : {score}", True, WHITE)
    rect = surf.get_rect(topleft=(WINwidth - 160, 10))
    DISPLAYSURF.blit(surf, rect)


def drawsnake(snakecoords):
    for coord in snakecoords:
        x = coord["x"] * CELLsize
        y = coord["y"] * CELLsize
        outer = pygame.Rect(x, y, CELLsize, CELLsize)
        inner = pygame.Rect(x + 4, y + 4, CELLsize - 8, CELLsize - 8)
        pygame.draw.rect(DISPLAYSURF, ORANGE, outer)
        pygame.draw.rect(DISPLAYSURF, YELLOW, inner)


def drawApple(coord):
    x = coord["x"] * CELLsize
    y = coord["y"] * CELLsize
    outer = pygame.Rect(x, y, CELLsize, CELLsize)
    inner = pygame.Rect(x + 4, y + 4, CELLsize - 8, CELLsize - 8)
    pygame.draw.rect(DISPLAYSURF, DARKRED, outer)
    pygame.draw.rect(DISPLAYSURF, RED, inner)


def drawGrid():
    for x in range(0, WINwidth, CELLsize):
        pygame.draw.line(DISPLAYSURF, GREEN, (x, 0), (x, WINheight))
    for y in range(0, WINheight, CELLsize):
        pygame.draw.line(DISPLAYSURF, GREEN, (0, y), (WINwidth, y))


if __name__ == "__main__":
    main()