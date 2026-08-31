import pygame
import random
import sys

# =========================
# 🪱 지렁이 게임 설정
# =========================

pygame.init()

WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🪱 지렁이 게임")

clock = pygame.time.Clock()

# 색깔
BLACK = (20, 20, 25)
WHITE = (255, 255, 255)
GREEN = (50, 220, 100)
DARK_GREEN = (30, 150, 70)
RED = (255, 70, 70)
YELLOW = (255, 220, 50)
GRAY = (100, 100, 100)

font = pygame.font.SysFont("malgungothic", 30)
big_font = pygame.font.SysFont("malgungothic", 55)


# =========================
# 🍎 랜덤 먹이 생성
# =========================
def create_food(snake):
    while True:
        x = random.randrange(0, WIDTH, GRID_SIZE)
        y = random.randrange(0, HEIGHT, GRID_SIZE)

        if (x, y) not in snake:
            return (x, y)


# =========================
# 🎮 게임 시작
# =========================
def game():

    snake = [
        (400, 300),
        (380, 300),
        (360, 300)
    ]

    direction = (GRID_SIZE, 0)
    next_direction = direction

    food = create_food(snake)

    score = 0
    speed = 10

    game_over = False

    while True:

        # =========================
        # ⌨️ 이벤트 처리
        # =========================
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                # 🔼 위
                if event.key in [pygame.K_UP, pygame.K_w]:
                    if direction != (0, GRID_SIZE):
                        next_direction = (0, -GRID_SIZE)

                # 🔽 아래
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    if direction != (0, -GRID_SIZE):
                        next_direction = (0, GRID_SIZE)

                # ◀️ 왼쪽
                elif event.key in [pygame.K_LEFT, pygame.K_a]:
                    if direction != (GRID_SIZE, 0):
                        next_direction = (-GRID_SIZE, 0)

                # ▶️ 오른쪽
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    if direction != (-GRID_SIZE, 0):
                        next_direction = (GRID_SIZE, 0)

                # 🔄 게임오버 후 다시 시작
                elif event.key == pygame.K_r and game_over:
                    return

                # ❌ ESC 종료
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        # =========================
        # 🪱 게임 진행
        # =========================
        if not game_over:

            direction = next_direction

            head_x, head_y = snake[0]

            new_head = (
                head_x + direction[0],
                head_y + direction[1]
            )

            # 💥 벽 충돌
            if (
                new_head[0] < 0 or
                new_head[0] >= WIDTH or
                new_head[1] < 0 or
                new_head[1] >= HEIGHT
            ):
                game_over = True

            # 💥 자기 몸 충돌
            elif new_head in snake:
                game_over = True

            else:
                snake.insert(0, new_head)

                # 🍎 먹이 먹음
                if new_head == food:

                    score += 1

                    # 점수 올라갈수록 빨라짐
                    speed = min(25, 10 + score // 3)

                    food = create_food(snake)

                else:
                    snake.pop()


        # =========================
        # 🎨 화면 그리기
        # =========================
        screen.fill(BLACK)

        # 격자
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, (35, 35, 40), (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (35, 35, 40), (0, y), (WIDTH, y))


        # 🍎 먹이
        pygame.draw.rect(
            screen,
            RED,
            (food[0], food[1], GRID_SIZE, GRID_SIZE),
            border_radius=6
        )


        # 🪱 지렁이
        for i, part in enumerate(snake):

            color = GREEN if i == 0 else DARK_GREEN

            pygame.draw.rect(
                screen,
                color,
                (part[0], part[1], GRID_SIZE, GRID_SIZE),
                border_radius=5
            )


        # 👀 지렁이 눈
        if len(snake) > 0:

            head = snake[0]

            pygame.draw.circle(
                screen,
                WHITE,
                (head[0] + 6, head[1] + 6),
                3
            )

            pygame.draw.circle(
                screen,
                WHITE,
                (head[0] + 14, head[1] + 6),
                3
            )


        # 🏆 점수
        score_text = font.render(
            f"🏆 SCORE : {score}",
            True,
            WHITE
        )

        screen.blit(score_text, (20, 15))


        # =========================
        # 💀 게임 오버 화면
        # =========================
        if game_over:

            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))

            screen.blit(overlay, (0, 0))

            text1 = big_font.render(
                "GAME OVER 💀",
                True,
                RED
            )

            text2 = font.render(
                f"최종 점수 : {score}",
                True,
                WHITE
            )

            text3 = font.render(
                "R키 : 다시 시작   |   ESC : 종료",
                True,
                YELLOW
            )

            screen.blit(
                text1,
                text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 70))
            )

            screen.blit(
                text2,
                text2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            )

            screen.blit(
                text3,
                text3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 70))
            )


        pygame.display.flip()

        clock.tick(speed)


# =========================
# 🔥 게임 계속 실행
# =========================
while True:
    game()
