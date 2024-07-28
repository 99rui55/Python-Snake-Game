import pygame
from GameSettings import game_settings
from Snake import Snake
import GraphicUtils
import LogicUtils
from FoodManager import FoodManager
from StatisticsManager import StatisticsManager

pygame.init()
snake = Snake(g_settings=game_settings, color=(255, 0, 174), initPos=(0, 0))
f_manager = FoodManager(g_settings=game_settings)
display = pygame.display.set_mode((game_settings.w_width, game_settings.w_height))
GraphicUtils.board = display
st_manger = StatisticsManager(g_settings=game_settings, snake=snake, board=display)

gameOver = False


def snakeLoop():
    global gameOver
    current_time = pygame.time.get_ticks()
    #check if snake need to move
    if current_time - snake.last_moved >= 1000 // game_settings.s_speed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            #determine movement direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if snake.last_direction != LogicUtils.right:
                        snake.setDirection(LogicUtils.left)
                elif event.key == pygame.K_RIGHT:
                    if snake.last_direction != LogicUtils.left:
                        snake.setDirection(LogicUtils.right)
                elif event.key == pygame.K_UP:
                    if snake.last_direction != LogicUtils.down:
                        snake.setDirection(LogicUtils.up)
                elif event.key == pygame.K_DOWN:
                    if snake.last_direction != LogicUtils.up:
                        snake.setDirection(LogicUtils.down)
                elif event.key == pygame.K_e:
                    exit()
        if not snake.isDead():
            snake.move()
        else:
            gameOver = True

        snake.last_moved = current_time


def boardLoop():
    # Clear the screen at the beginning of each frame
    display.fill(game_settings.b_color)

    # draw the grid
    GraphicUtils.drawGrid(g_settings=game_settings)
    GraphicUtils.drawBoard(g_settings=game_settings)

    # blink the food
    time = pygame.time.get_ticks()
    f_manager.blinkFood(time)
    f_manager.drawFood()

    # draw the snake
    GraphicUtils.drawSnake(g_settings=game_settings, snake=snake)

    # draw statistics
    st_manger.update(g_settings=game_settings, snake=snake)
    st_manger.drawStatistics()

    # check if snake has eaten food
    eaten_food = snake.checkFoodContact(f_manager.f_list)
    if eaten_food != None:
        f_manager.removeFood(eaten_food)
        snake.addToSnake(1)

    # respawn food if needed
    if f_manager.noFood():
        f_manager.generateFood()

    # display game over text
    if gameOver:
        st_manger.displayEndMessage()

    # update game board
    pygame.display.update()


def restartGame():
    global gameOver
    gameOver = False
    snake.restart()
    game_settings.restart()


def exit():
    pygame.quit()
    quit()


def gameLoop():
    while True:
        while not gameOver:
            # preform snake loop by snake speed
            snakeLoop()

            # preform board loop
            boardLoop()
            GraphicUtils.drawBoard(game_settings)

            clock = pygame.time.Clock()
            # Limit the frame rate to 60 FPS
            clock.tick(60)  

        #after player has lost, check if restart game or exit
        boardLoop()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    restartGame()
                elif event.key == pygame.K_e:
                    exit()

#call gameLoop
gameLoop()
