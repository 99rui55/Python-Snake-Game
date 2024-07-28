import pygame
from GameSettings import game_settings
from Snake import Snake
import GraphicUtils
import LogicUtils
from FoodManager import FoodManager
from StatisticsManager import StatisticsManager

snake = None
f_manager = None
display = None
st_manger = None
game_over = None

def Init():
    global snake, f_manager, display, st_manger, game_over
    pygame.init()
    snake = Snake(g_settings=game_settings, color=(255, 0, 174), initPos=(0, 0))
    f_manager = FoodManager(g_settings=game_settings)
    display = pygame.display.set_mode((game_settings.w_width, game_settings.w_height))
    GraphicUtils.board = display
    st_manger = StatisticsManager(g_settings=game_settings, snake=snake, board=display)
    game_over = False


def SnakeLoop():
    global game_over
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
                        snake.SetDirection(LogicUtils.left)
                elif event.key == pygame.K_RIGHT:
                    if snake.last_direction != LogicUtils.left:
                        snake.SetDirection(LogicUtils.right)
                elif event.key == pygame.K_UP:
                    if snake.last_direction != LogicUtils.down:
                        snake.SetDirection(LogicUtils.up)
                elif event.key == pygame.K_DOWN:
                    if snake.last_direction != LogicUtils.up:
                        snake.SetDirection(LogicUtils.down)
                elif event.key == pygame.K_e:
                    exit()
        if not snake.IsDead():
            snake.Move()
        else:
            game_over = True

        snake.last_moved = current_time


def BoardLoop():
    # Clear the screen at the beginning of each frame
    display.fill(game_settings.b_color)

    # draw the grid
    GraphicUtils.DrawGrid(g_settings=game_settings)
    GraphicUtils.DrawBoard(g_settings=game_settings)

    # blink the food
    time = pygame.time.get_ticks()
    f_manager.blinkFood(time)
    f_manager.drawFood()

    # draw the snake
    GraphicUtils.DrawSnake(g_settings=game_settings, snake=snake)

    # draw statistics
    st_manger.Update(g_settings=game_settings, snake=snake)
    st_manger.DrawStatistics()

    # check if snake has eaten food
    eaten_food = snake.CheckFoodContact(f_manager.f_list)
    if eaten_food != None:
        f_manager.removeFood(eaten_food)
        snake.AddToSnake(1)

    # respawn food if needed
    if f_manager.noFood():
        f_manager.generateFood()

    # display game over text
    if game_over:
        st_manger.DisplayEndMessage()

    # update game board
    pygame.display.update()


def RestartGame():
    global game_over
    game_over = False
    snake.Restart()
    game_settings.Restart()


def exit():
    pygame.quit()
    quit()


def GameLoop():
    Init()
    while True:
        while not game_over:
            # preform snake loop by snake speed
            SnakeLoop()

            # preform board loop
            BoardLoop()
            GraphicUtils.DrawBoard(game_settings)

            clock = pygame.time.Clock()
            # Limit the frame rate to 60 FPS
            clock.tick(60)  

        #after player has lost, check if restart game or exit
        BoardLoop()
        print("outside of game")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    RestartGame()
                elif event.key == pygame.K_e:
                    exit()


