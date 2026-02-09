import pygame, sys, random
from pygame.locals import *

# ---------------- INIT ----------------
pygame.init()
clock = pygame.time.Clock()

# ---------------- SCREEN SETTINGS ----------------
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
FPS = 32

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

GROUND_Y = int(SCREEN_HEIGHT * 0.8)

HIGH_SCORE = 0

# ---------------- LOAD IMAGES ----------------
def load_images():
    images = {}

    images["background"] = pygame.image.load("images/theback.jpg").convert_alpha()
    images["ground"] = pygame.image.load("images/down.png").convert_alpha()

    pipe_image = pygame.image.load("images/pipe.png").convert_alpha()
    images["pipe_top"] = pygame.transform.rotate(pipe_image, 180)
    images["pipe_bottom"] = pipe_image

    images["score_digits"] = [
        pygame.image.load(f"images/{i}.png").convert_alpha() for i in range(10)
    ]

    images["birds"] = [
        pygame.image.load("images/laib.png").convert_alpha(),
        pygame.image.load("images/ham.png").convert_alpha(),
        pygame.image.load("images/manal.png").convert_alpha(),
        pygame.image.load("images/bush.png").convert_alpha()
    ]

    return images

IMAGES = load_images()

# ---------------- CHARACTER SELECT ----------------
def choose_bird():
    selected_index = 0
    font = pygame.font.SysFont(None, 36)

    while True:
        SCREEN.blit(IMAGES["background"], (0, 0))
        title = font.render("Choose Your Bird (ENTER)", True, (255, 255, 255))
        SCREEN.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))

        for i, bird in enumerate(IMAGES["birds"]):
            x = 100 + i * 120
            y = 220
            SCREEN.blit(bird, (x, y))

            if i == selected_index:
                pygame.draw.rect(
                    SCREEN, (255, 255, 0),
                    (x - 5, y - 5, bird.get_width() + 10, bird.get_height() + 10), 3
                )

        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    selected_index = (selected_index + 1) % len(IMAGES["birds"])
                if event.key == K_LEFT:
                    selected_index = (selected_index - 1) % len(IMAGES["birds"])
                if event.key == K_RETURN:
                    return IMAGES["birds"][selected_index]

# ---------------- CREATE PIPE ----------------
def create_pipe_pair():
    gap_height = SCREEN_HEIGHT // 3
    pipe_height = IMAGES["pipe_top"].get_height()

    bottom_pipe_y = random.randint(80, SCREEN_HEIGHT - gap_height - 120)

    top_pipe = {
        "x": SCREEN_WIDTH + 20,
        "y": bottom_pipe_y - pipe_height,
        "scored": False
    }

    bottom_pipe = {
        "x": SCREEN_WIDTH + 20,
        "y": bottom_pipe_y + gap_height
    }

    return top_pipe, bottom_pipe

# ---------------- COLLISION CHECK ----------------
def check_collision(bird_x, bird_y, bird_image, pipes):
    bird_width = bird_image.get_width()
    bird_height = bird_image.get_height()

    if bird_y < 0 or bird_y > GROUND_Y - bird_height:
        return True

    pipe_width = IMAGES["pipe_top"].get_width()
    pipe_height = IMAGES["pipe_top"].get_height()

    for top_pipe, bottom_pipe in pipes:
        if bird_x + bird_width > top_pipe["x"] and bird_x < top_pipe["x"] + pipe_width:
            if bird_y < top_pipe["y"] + pipe_height:
                return True
            if bird_y + bird_height > bottom_pipe["y"]:
                return True

    return False

# ---------------- GAME LOOP ----------------
def play_game(bird_image):
    bird_x = SCREEN_WIDTH // 5
    bird_y = SCREEN_HEIGHT // 2

    bird_velocity = 0
    gravity = 1
    jump_strength = -8

    pipe_speed = -4
    pipes = [create_pipe_pair()]

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key in (K_SPACE, K_UP):
                    bird_velocity = jump_strength

        # Bird movement
        bird_velocity += gravity
        bird_y += bird_velocity

        # Move pipes
        for top_pipe, bottom_pipe in pipes:
            top_pipe["x"] += pipe_speed
            bottom_pipe["x"] += pipe_speed

        # Score logic
        for top_pipe, bottom_pipe in pipes:
            if not top_pipe["scored"] and top_pipe["x"] + IMAGES["pipe_top"].get_width() < bird_x:
                top_pipe["scored"] = True
                score += 1

        # Add new pipe
        if pipes[0][0]["x"] < -IMAGES["pipe_top"].get_width():
            pipes.pop(0)
            pipes.append(create_pipe_pair())

        # Collision
        if check_collision(bird_x, bird_y, bird_image, pipes):
            return score

        # Draw everything
        SCREEN.blit(IMAGES["background"], (0, 0))

        for top_pipe, bottom_pipe in pipes:
            SCREEN.blit(IMAGES["pipe_top"], (top_pipe["x"], top_pipe["y"]))
            SCREEN.blit(IMAGES["pipe_bottom"], (bottom_pipe["x"], bottom_pipe["y"]))

        SCREEN.blit(IMAGES["ground"], (0, GROUND_Y))
        SCREEN.blit(bird_image, (bird_x, bird_y))

        # Draw score
        score_x = SCREEN_WIDTH // 2
        for digit in map(int, str(score)):
            SCREEN.blit(IMAGES["score_digits"][digit], (score_x, 20))
            score_x += IMAGES["score_digits"][digit].get_width()

        pygame.display.update()
        clock.tick(FPS)

# ---------------- GAME OVER ----------------
def show_game_over(score):
    global HIGH_SCORE
    HIGH_SCORE = max(HIGH_SCORE, score)

    font = pygame.font.SysFont(None, 40)

    while True:
        SCREEN.blit(IMAGES["background"], (0, 0))

        SCREEN.blit(font.render("GAME OVER", True, (255, 0, 0)), (200, 100))
        SCREEN.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (200, 160))
        SCREEN.blit(font.render(f"High Score: {HIGH_SCORE}", True, (255, 255, 0)), (200, 200))
        SCREEN.blit(font.render("SPACE = Replay | ESC = Quit", True, (200, 200, 200)), (120, 260))

        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# ---------------- MAIN MENU ----------------
bird = choose_bird()

while True:
    SCREEN.blit(IMAGES["background"], (0, 0))
    SCREEN.blit(bird, (SCREEN_WIDTH // 5, SCREEN_HEIGHT // 2))
    SCREEN.blit(IMAGES["ground"], (0, GROUND_Y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key in (K_SPACE, K_UP):
            final_score = play_game(bird)
            show_game_over(final_score)
