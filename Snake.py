import pygame
from time import sleep
import random

pygame.init()
screen = pygame.display.set_mode((601, 601))
pygame.display.set_caption('Snake')
running = True
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()

#Snake position
snakes = [[4, 4], [4, 5], [4, 6], [4, 7]]
direction = "right"

# Tạo quả táo
#apple_image = pygame.image.load("apple.png")  # Hoặc sử dụng pygame.draw
apple_x = random.randrange(0, 600, 30)
apple_y = random.randrange(0, 600, 30)

score = 0
font = pygame.font.Font(None, 36)

game_over = False
font_game_over = pygame.font.Font(None, 72)
while running:
	clock.tick(60)
	screen.fill(BLACK)

	#Draw gird
	for i in range(21):
		pygame.draw.line(screen, WHITE, (0, i*30), (600, i*30))
		pygame.draw.line(screen, WHITE, (i*30, 0), (i*30, 600))

	# Draw snake
	for snake in snakes:
		pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))

	# Vẽ quả táo (sử dụng hình tròn màu đỏ)
	pygame.draw.circle(screen, RED, (apple_x + 15, apple_y + 15), 15)

	# Snake move
	if not game_over:
		if direction == "right":
			snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
		if direction == "left":
			snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
		if direction == "up":
			snakes.append([snakes[-1][0], snakes[-1][1] - 1])		
		if direction == "down":
			snakes.append([snakes[-1][0], snakes[-1][1] + 1])
		snakes.pop(0)

	# Xử lý khi con rắn đi ra khỏi màn hình
	if snakes[-1][0] < 0:
		snakes[-1][0] = 19
	elif snakes[-1][0] > 19:
		snakes[-1][0] = 0
	if snakes[-1][1] < 0:
		snakes[-1][1] = 19
	elif snakes[-1][1] > 19:
		snakes[-1][1] = 0

	# Xử lý va chạm với bản thân
	for i in range(len(snakes) - 1):
		if snakes[-1] == snakes[i]:
			game_over = True
			break


	# Xử lý va chạm
	if snakes[-1][0] == apple_x // 30 and snakes[-1][1] == apple_y // 30:
		apple_x = random.randrange(0, 600, 30)
		apple_y = random.randrange(0, 600, 30)
		snakes.insert(0, snakes[0])
		score += 10

	#Hien thi diem so
	score_text = font.render("Score: " + str(score), True, WHITE)
	screen.blit(score_text, (10, 10))

	#Hien thi Game Over
	if game_over:
		game_over_text = font_game_over.render("Game Over", True, WHITE)
		text_rect = game_over_text.get_rect(center = (300, 300))
		screen.blit(game_over_text, text_rect)

	sleep(0.15)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direction != "down":
				direction = "up"
			if event.key == pygame.K_DOWN and direction != "up":
				direction = "down"
			if event.key == pygame.K_LEFT and direction != "right":
				direction = "left"
			if event.key == pygame.K_RIGHT and direction != "left":
				direction = "right"
				

	pygame.display.flip()

pygame.quit()