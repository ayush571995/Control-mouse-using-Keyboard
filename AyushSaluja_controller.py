import pygame, sys, pyautogui
black = (0,0,0)
pygame.init()
myfont = pygame.font.SysFont("monospace", 15)
pygame.display.set_caption('Mouse Values')
size = [240,240]
screen = pygame.display.set_mode(size)
pygame.key.set_repeat(50,50)

def adjust_speed():
    return int(input())

def movemement(changex,changey):
    try:
        x, y = pyautogui.position()
        pyautogui.moveTo(x+changex,y+changey)
    except:
        pass

def values():
    left=myfont.render("Left", 1, (255, 255, 0))
    screen.blit(left, (0, 0))
    right=myfont.render("Right", 1, (255, 255, 0))
    screen.blit(right, (0,30))
    up=myfont.render("Up", 1, (255, 255, 0))
    screen.blit(up, (0,60))
    down=myfont.render("Down", 1, (255, 255, 0))
    screen.blit(down, (0,90))
speed=5
start_time=1
#speed=adjust_speed()     Uncomment this line to specify the speed by the user.
global clock, double_click_event, timer
double_click_event = pygame.USEREVENT + 1
timer = 0


def double_click():
    x,y=pyautogui.position()
    pyautogui.doubleClick(x,y,button='left')
while True:
    values()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                movemement(-speed,0)
                l=myfont.render(str(True), 1, (255, 255, 0))
                screen.blit(l, (90,0))
            if keys[pygame.K_RIGHT]:
                movemement(speed, 0)
                l = myfont.render(str(True), 1, (255, 255, 0))
                screen.blit(l, (90,30))
            if keys[pygame.K_UP]:
                movemement(0,-speed)
                l = myfont.render(str(True), 1, (255, 255, 0))
                screen.blit(l, (90,60))
            if keys[pygame.K_DOWN]:
                movemement(0,speed)
                l = myfont.render(str(True), 1, (255, 255, 0))
                screen.blit(l, (90,90))
            if event.key==pygame.K_SPACE:
                if timer == 0:
                    pygame.time.set_timer(double_click_event, 500)
                    timerset = True
                    x, y = pyautogui.position()
                    pyautogui.click(x, y, button='left')
                else:
                    if timer == 1:
                        pygame.time.set_timer(double_click_event, 0)
                        double_click()
                        timerset = False
                if timerset:
                    timer = 1
                else:
                    timer = 0
    pygame.display.update()
    screen.fill(black)