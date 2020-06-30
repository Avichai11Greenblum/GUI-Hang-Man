import random
import math
import pygame
pygame.init()

# Making the frame + logo + title
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hang Man Game")
logo = pygame.image.load("plugin.png")
pygame.display.set_icon(logo)

# Loading photos
images = []
for i in range(7):
    IMG = pygame.image.load("hangman" + str(i) + ".png")
    images.append(IMG)

# Buttons
Radius = 20
Diameter = Radius * 2
Gap = 15
letters_pos = []

startX = 30
startY = 400
A = 65 # Making the first value in the ABC that will convert to numbers using chr.

for i in range(26):
    x = startX + Diameter + ( (Diameter + Gap) * (i % 13) )
    y = startY + (i // 13) * (Gap + Diameter)
    letters_pos.append([x, y, chr(A + i), True])

# Letters Font
FONT = pygame.font.SysFont('comicsans', 40)
UI_FONT = pygame.font.SysFont('comicsans', 60)


# Draw function
def draw():
    screen.fill((120,120,120))
    screen.blit(images[mistakes],(150, 70) )

    # Drawing the buttons
    for ele in letters_pos:
        x, y, letter, visible = ele
        if visible:
            pygame.draw.circle(screen, (0,0,0), (x,y), Radius, 3 )
            text = FONT.render(letter, 1, (0,0,0))
            screen.blit(text, (x - text.get_width() / 2 , y - text.get_height() / 2) )


    # Making the UI code on screen
    global ui_show
    code_show = UI_FONT.render(" ".join(ui_show), 1, (0,0,0))
    screen.blit(code_show, (340, 160))

def win_or_lose():

    global lose
    if lose:
        # Lose Screen
        win_text = "YOU LOST! :( "
        LOSE_SHOW = UI_FONT.render(win_text, 1, (0,0,0))
        screen.blit(LOSE_SHOW, (300, 300))
    else:
        # Win Screen
        win_text = "YOU WON!"
        WIN_SHOW = UI_FONT.render(win_text, 1, (0,0,0))
        screen.blit(WIN_SHOW, (300, 300))



# Game loop
mistakes = 0
end_screen = False

words_bank = ["magic", "pizza", "galaxy", "shalom", "spaceship", "shoes", "chess", "baseball", "ancient"]
FPS = 60
my_clock = pygame.time.Clock()

code = words_bank[random.randint(0,len(words_bank) - 1)]
code = code.upper()

global ui_list
ui_list = ["_" for char in code]

global lose
lose = False

run = True
while run:
    my_clock.tick(FPS)

    # Updating the word after every guess
    global ui_show
    ui_show = " ".join(ui_list)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not end_screen:
            mouseX, mouseY = pygame.mouse.get_pos()
            for ele in letters_pos:
                letX, letY, letter, visible = ele
                dis = math.sqrt( math.pow(mouseX - letX, 2) + math.pow(mouseY - letY, 2))
                if dis < Radius:
                    ele[3] = False # remove the chosen letter from the screen by turning visible to False

                    if letter in code:
                        i = 0
                        for char in code:
                            if letter == char:
                                ui_list[i] = letter
                            i += 1

                    else:
                        mistakes += 1
                        if mistakes == 6:
                            end_screen = True
                            lose = True

    if "_" not in ui_list:
        end_screen = True

    if end_screen:
            win_or_lose()



    pygame.display.update()

