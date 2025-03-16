import pygame
import os
import sys
from os import path
import schedule

pygame.init()
WIDTH, HEIGHT = 900, 600
bank_balance = 0
ball_balance = 250
dohod = 180
font = pygame.font.SysFont(None, 15)
font1 = pygame.font.SysFont(None, 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Игра плюс')

def load_image(name: str) -> pygame.Surface:
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.getcwd()
    full_path = path.join(base_path, name)
    if not path.exists(full_path):
        print(f'Не удалось найти файл {full_path}')
        sys.exit(1)
    image = pygame.image.load(full_path).convert_alpha()
    return image

def info():
    button_info = pygame.Surface((120, 30))
    button_info.set_alpha(0)
    btn_info = pygame.Rect(130, 55, 120, 30)
    pygame.draw.rect(button_info, 'white', btn_info)
    screen.blit(button_info, (130, 55))
    return btn_info

def tasks():
    button_tasks = pygame.Surface((90, 30))
    button_tasks.set_alpha(0)
    btn_tasks = pygame.Rect(260, 55, 90, 30)
    pygame.draw.rect(button_tasks, 'white', btn_tasks)
    screen.blit(button_tasks, (260, 55))
    return btn_tasks

def balance():
    button_balance = pygame.Surface((70, 30))
    button_balance.set_alpha(0)
    btn_balance = pygame.Rect(365, 55, 70, 30)
    pygame.draw.rect(button_balance, 'white', btn_balance)
    screen.blit(button_balance, (365, 55))
    return btn_balance

def partners():
    button_partners = pygame.Surface((80, 30))
    button_partners.set_alpha(0)
    btn_partners = pygame.Rect(450, 55, 80, 30)
    pygame.draw.rect(button_partners, 'white', btn_partners)
    screen.blit(button_partners, (450, 55))
    return btn_partners

def leaders():
    button_leaders = pygame.Surface((100, 30))
    button_leaders.set_alpha(0)
    btn_leaders = pygame.Rect(550, 55, 100, 30)
    pygame.draw.rect(button_leaders, 'white', btn_leaders)
    screen.blit(button_leaders, (550, 55))
    return btn_leaders

def shop():
    button_shop = pygame.Surface((85, 30))
    button_shop.set_alpha(0)
    btn_shop = pygame.Rect(650, 55, 85, 30)
    pygame.draw.rect(button_shop, 'white', btn_shop)
    screen.blit(button_shop, (650, 55))
    return btn_shop

def button(x, y, w, h):
    button = pygame.Surface((w, h))
    button.set_alpha(0)
    btn = pygame.Rect(x, y, w, h)
    pygame.draw.rect(button, 'white', btn)
    screen.blit(button, (x, y))
    return btn

def show_main_menu():
    screen.blit(pygame.transform.scale(load_image('data/main.png'), (900, 600)), (0, 0))
    button1 = pygame.Surface((90, 60))
    button1.set_alpha(0)
    btn1 = pygame.Rect(470, 0, 90, 60)
    pygame.draw.rect(button1, 'white', btn1)
    screen.blit(button1, (470, 0))
    return btn1

def show_info():
    screen.blit(pygame.transform.scale(load_image('data/info.png'), (900, 600)), (0, 0))

    btn_tasks = tasks()
    btn_balance = balance()
    btn_partners = partners()
    btn_leaders = leaders()
    btn_shop = shop()

    pygame.display.flip()
    return btn_tasks, btn_balance, btn_partners, btn_leaders, btn_shop

def show_tasks():
    screen.blit(pygame.transform.scale(load_image('data/tasks.png'), (900, 600)), (0, 0))

    btn_info = info()
    btn_balance = balance()
    btn_partners = partners()
    btn_leaders = leaders()
    btn_shop = shop()

    buttons = []
    for i in range(6):
        buttons.append(button(260, 157 + 47 * i, 355, 35))

    pygame.display.flip()
    return btn_info, btn_balance, btn_partners, btn_leaders, btn_shop, buttons

def show_balance():
    screen.blit(pygame.transform.scale(load_image('data/balance.png'), (900, 600)), (0, 0))

    btn_info = info()
    btn_tasks = tasks()
    btn_partners = partners()
    btn_leaders = leaders()
    btn_shop = shop()

    count = pygame.Rect(310, 330, 40, 20)
    pygame.draw.rect(screen, 'white', count)
    text_count = font.render(f"{bank_balance}", True, 'black')
    screen.blit(text_count, (320, 337))

    pygame.display.flip()
    return btn_info, btn_tasks, btn_partners, btn_leaders, btn_shop

def show_partners():
    screen.blit(pygame.transform.scale(load_image('data/partners.png'), (900, 600)), (0, 0))

    btn_info = info()
    btn_tasks = tasks()
    btn_balance = balance()
    btn_leaders = leaders()
    btn_shop = shop()

    btns_upgrade = []
    for i in range(3):
        btn = button(635, 205 + i * 50, 200, 30)
        btns_upgrade.append(btn)

    count = pygame.Rect(370, 140, 50, 40)
    pygame.draw.rect(screen, 'white', count)
    text_count = font1.render(f"{dohod}", True, 'black')
    screen.blit(text_count, (370, 150))

    bally = pygame.Rect(720, 125, 35, 30)
    pygame.draw.rect(screen, '#fac710', bally)
    text_balance = font1.render(f'{ball_balance}', True, 'black')
    screen.blit(text_balance, (720, 135))

    pygame.display.flip()
    return btn_info, btn_tasks, btn_balance, btn_leaders, btn_shop, btns_upgrade

def show_leaders():
    screen.blit(pygame.transform.scale(load_image('data/leaders.png'), (900, 600)), (0, 0))

    btn_info = info()
    btn_tasks = tasks()
    btn_balance = balance()
    btn_partners = partners()
    btn_shop = shop()

    pygame.display.flip()
    return btn_info, btn_tasks, btn_balance, btn_partners, btn_shop

def show_ex():
    screen.blit(pygame.transform.scale(load_image('data/ex.png'), (900, 600)), (0, 0))
    btn = button(50, 20, 30, 30)
    return btn

def job(flag):
    global bank_balance, dohod
    if bank_balance + dohod >= 250000:
        bank_balance = 250000
    else:
        bank_balance += dohod
    if flag == 'balance':
        count = pygame.Rect(310, 330, 40, 20)
        pygame.draw.rect(screen, 'white', count)
        text_count = font.render(f"{bank_balance}", True, 'black')
        screen.blit(text_count, (320, 337))

pygame.display.flip()
button1 = show_main_menu()
flag = 'main'
schedule.every().minute.at(":00").do(job, flag=flag)
running = True
while running:
    schedule.run_pending()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button1.collidepoint(mouse_pos) and flag == 'main':
                flag = 'info'
                btn_tasks, btn_balance, btn_partners, btn_leaders, btn_shop = show_info()
            elif btn_tasks.collidepoint(mouse_pos) and flag != 'main':
                flag = 'tasks'
                btn_info, btn_balance, btn_partners, btn_leaders, btn_shop, buttons = show_tasks()
            elif btn_balance.collidepoint(mouse_pos) and flag != 'main':
                flag = 'balance'
                btn_info, btn_tasks, btn_partners, btn_leaders, btn_shop = show_balance()
            elif btn_partners.collidepoint(mouse_pos) and flag != 'main':
                flag = 'partners'
                btn_info, btn_tasks, btn_balance, btn_leaders, btn_shop, btns_upgrade = show_partners()
            elif btn_leaders.collidepoint(mouse_pos) and flag != 'main':
                flag = 'leaders'
                btn_info, btn_tasks, btn_balance, btn_partners, btn_shop = show_leaders()
            elif flag == 'tasks':
                for i in buttons:
                    if i.collidepoint(mouse_pos):
                        flag = 'ex'
                        btn_back = show_ex()
                        break
            elif flag == 'ex' and btn_back.collidepoint(mouse_pos):
                flag = 'tasks'
                btn_info, btn_balance, btn_partners, btn_leaders, btn_shop, buttons = show_tasks()
            elif flag == 'partners':
                if btns_upgrade[0].collidepoint(mouse_pos) and ball_balance >= 50:
                    dohod += 20
                    ball_balance -= 50
                    btn_info, btn_tasks, btn_balance, btn_leaders, btn_shop, btns_upgrade = show_partners()
                elif btns_upgrade[1].collidepoint(mouse_pos) and ball_balance >= 100:
                    dohod += 30
                    ball_balance -= 100
                    btn_info, btn_tasks, btn_balance, btn_leaders, btn_shop, btns_upgrade = show_partners()
                elif btns_upgrade[2].collidepoint(mouse_pos) and ball_balance >= 150:
                    dohod += 40
                    ball_balance -= 150
                    btn_info, btn_tasks, btn_balance, btn_leaders, btn_shop, btns_upgrade = show_partners()
            elif btn_info.collidepoint(mouse_pos) and flag != 'main':
                flag = 'info'
                btn_tasks, btn_balance, btn_partners, btn_leaders, btn_shop = show_info()
        pygame.display.update()