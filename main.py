import pygame
import shop.upgrades as upgrades
import time

pygame.init()


#############################################   ADDING IMAGES   ##############################################
icon = pygame.image.load("images\\icon.png")
bg_img = pygame.image.load("images\\background.png")
upgrades_background = pygame.image.load("shop\\icon_upgrades\\upgrades_background.png")
cookie_img = pygame.image.load("images\\cookie.gif")
Shop_img = pygame.image.load("shop\\icon_upgrades\\shop.png")
Cursor_img = pygame.image.load("shop\\icon_upgrades\\Cursor.png")
Autoclick_img = pygame.image.load("shop\\icon_upgrades\\Autoclick.png")
Grandma_img = pygame.image.load("shop\\icon_upgrades\\Grandma.png")
Cookie_farm_img = pygame.image.load("shop\\icon_upgrades\\Cookie_farm.png")
Cookie_factory_img = pygame.image.load("shop\\icon_upgrades\\Cookie_factory.png")
Cookie_planet_img = pygame.image.load("shop\\icon_upgrades\\Cookie_planet.png")
Cookie_galaxy_img = pygame.image.load("shop\\icon_upgrades\\Cookie_galaxy.png")
cost_cookie = pygame.image.load("images\\cost_cookie.png") #it's cookie on the right of cost of upgrade
text_cookie = pygame.image.load("images\\text_cookie.png") #it's cookie on the right of number of cookies
###################################### WINDOW GAME SETTINGS #####################################################
bg = pygame.transform.scale(bg_img, (1280,1024))
pygame.display.set_icon(icon)
WIDTH, HEIGHT = 1280,1024
display_width = 1280
display_height = 1024
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("COOKIE CLICKER")
#############################################   CENTER OF UPGRADES   #############################################

# Center of image button upgrade is let me detect do player clicks button of upgrade

cookie_rect = cookie_img.get_rect(center=(390,500))
window.blit(cookie_img, cookie_rect)
mask = pygame.mask.from_surface(cookie_img)
cursor_rect = Cursor_img.get_rect(center = (1050,180))
autoclick_rect = Autoclick_img.get_rect(center = (1050, 300))
Grandma_rect = Grandma_img.get_rect(center = (1050, 420))
Cookie_farm_rect = Cookie_farm_img.get_rect(center = (1050,540))
Cookie_factory_rect = Cookie_factory_img.get_rect(center = (1050,660))
Cookie_planet_rect = Cookie_planet_img.get_rect(center = (1050,780))
Cookie_galaxy_rect = Cookie_galaxy_img.get_rect(center = (1050,900))
###################################################################################################################

white = pygame.color.Color("#ffffff")
font = pygame.font.Font(None, 52)
fontcookie = pygame.font.Font(None, 98)
fontcookiepersecond = pygame.font.Font(None, 30)

cookies = 0
cookies_per_second = 0
current_time = 0

def draw_window():
    window.blit(bg, (0, 0))
    window.blit(upgrades_background,(805,0))        # it's background for upgrades! #
    window.blit(upgrades_background, (805, 370))    # it's background for upgrades! #
    window.blit(upgrades_background, (805, 650))    # it's background for upgrades! #
    window.blit(cookie_img, (240,350))

    window.blit(text, (330, 150))
    window.blit(text_cookie,(490,150)) ###  It's image of cookie, that's on the right side of cookies number ###


    window.blit(Cursor_img,(810,120))  ### Adding images of upgrades ###
    window.blit(Shop_img,(810,0))
    window.blit(Autoclick_img, (810,240))
    window.blit(Grandma_img, (810, 360))
    window.blit(Cookie_farm_img, (810, 480))
    window.blit(Cookie_factory_img,(810,600))
    window.blit(Cookie_planet_img,(810,720))
    window.blit(Cookie_galaxy_img,(810,840))


    window.blit(upgrades.Cursor.text_cost,(1150,200))  ### Adding text which showing cost of upgrade ###
    window.blit(upgrades.Autoclick.text_cost,(1150,320))
    window.blit(upgrades.Grandma.text_cost,(1140,440))
    window.blit(upgrades.Cookie_farm.text_cost,(1140,560))
    window.blit(upgrades.Cookie_factory.text_cost,(1130,680))
    window.blit(upgrades.Cookie_planet.text_cost,(1120, 800))
    window.blit(upgrades.Cookie_galaxy.text_cost,(1120, 920))


    window.blit(cost_cookie, (1240, 200))  ### images of cookie are everywhere on the right of cost upgrade ###
    window.blit(cost_cookie, (1240, 320))
    window.blit(cost_cookie, (1240, 440))
    window.blit(cost_cookie, (1240, 560))
    window.blit(cost_cookie, (1240, 680))
    window.blit(cost_cookie, (1240, 800))
    window.blit(cost_cookie, (1240, 920))






def main():
    global cookies, text, Cursor_img, tap_cookies, current_time, Autoclick_img,Grandma_img, Cookie_farm_img,\
        Cookie_factory_img,Cookie_planet_img,Cookie_galaxy_img, cookies_per_second

    tap_cookies = 1
    run = True
    while run:
        text = fontcookie.render(f"{cookies}", False, white)

#############################################################################################################

        # It's actually cost of upgrade

        upgrades.Cursor.text_cost = font.render(f" {upgrades.Cursor.cost_upgrade}", False, white)
        upgrades.Autoclick.text_cost = font.render(f"{upgrades.Autoclick.cost_upgrade}", False, white)
        upgrades.Grandma.text_cost = font.render(f"{upgrades.Grandma.cost_upgrade}", False, white)
        upgrades.Cookie_farm.text_cost = font.render(f" {upgrades.Cookie_farm.cost_upgrade}", False, white)
        upgrades.Cookie_factory.text_cost = font.render(f"{upgrades.Cookie_factory.cost_upgrade}", False, white)
        upgrades.Cookie_planet.text_cost = font.render(f"{upgrades.Cookie_planet.cost_upgrade}", False, white)
        upgrades.Cookie_galaxy.text_cost = font.render(f"{upgrades.Cookie_galaxy.cost_upgrade}", False, white)

##############################################################################################################

        # This timer every second adding cookies_per_second to cookies

        timer = pygame.time.get_ticks() / 1000
        if timer - current_time >= 1:
            cookies = cookies + cookies_per_second

            current_time = pygame.time.get_ticks() / 1000

##############################################################################################################

        # When player don't have cookies for buy upgrade, image is red,
        # #When player have cookies for buy upgrade, image is green

        if cookies >= upgrades.Cursor.cost_upgrade:
            Cursor_img = pygame.image.load("shop\\icon_upgrades\\Cursor_green.png")
        else:
            Cursor_img = pygame.image.load("shop\\icon_upgrades\\Cursor_red.png")

        if cookies >= upgrades.Autoclick.cost_upgrade:
            Autoclick_img = pygame.image.load("shop\\icon_upgrades\\Autoclick_green.png")
        else:
            Autoclick_img = pygame.image.load("shop\\icon_upgrades\\Autoclick_red.png")

        if cookies >= upgrades.Grandma.cost_upgrade:
            Grandma_img = pygame.image.load("shop\\icon_upgrades\\Grandma_green.png")
        else:
            Grandma_img = pygame.image.load("shop\\icon_upgrades\\Grandma_red.png")

        if cookies >= upgrades.Cookie_farm.cost_upgrade:
            Cookie_farm_img = pygame.image.load("shop\\icon_upgrades\\Cookie_farm_green.png")
        else:
            Cookie_farm_img = pygame.image.load("shop\\icon_upgrades\\Cookie_farm_red.png")
        
        if cookies >= upgrades.Cookie_factory.cost_upgrade:
            Cookie_factory_img = pygame.image.load("shop\\icon_upgrades\\Cookie_factory_green.png")
        else:
            Cookie_factory_img = pygame.image.load("shop\\icon_upgrades\\Cookie_factory_red.png")
            
        if cookies >= upgrades.Cookie_planet.cost_upgrade:
            Cookie_planet_img = pygame.image.load("shop\\icon_upgrades\\Cookie_planet_green.png")
        else:
            Cookie_planet_img = pygame.image.load("shop\\icon_upgrades\\Cookie_planet_red.png")
            
        if cookies >= upgrades.Cookie_galaxy.cost_upgrade:
            Cookie_galaxy_img = pygame.image.load("shop\\icon_upgrades\\Cookie_galaxy_green.png")
        else:
            Cookie_galaxy_img = pygame.image.load("shop\\icon_upgrades\\Cookie_galaxy_red.png")

#############################################   Checking do player click upgrade   ##########################


        for event in pygame.event.get():


            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if Cookie_galaxy_rect.collidepoint(x,y):                             ###  COOKIE_GALAXY  ###
                    if cookies >= upgrades.Cookie_galaxy.cost_upgrade:
                        print("Zakupiono Cookie_galaxy")
                        cookies_per_second = cookies_per_second + upgrades.Cookie_galaxy.cookies_per_second
                        print(cookies_per_second)
                        cookies = cookies - upgrades.Cookie_galaxy.cost_upgrade
                        upgrades.Cookie_galaxy.quantity += 1

                        print(upgrades.Cookie_galaxy.quantity)
                        if upgrades.Cookie_galaxy.quantity >= 2:
                            upgrades.Cookie_galaxy.cost_upgrade = upgrades.Cookie_galaxy.cost_upgrade + 4000


                    else:
                        print("Nie stać Cię na Cookie_galaxy!")



            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if Cookie_planet_rect.collidepoint(x,y):                             ###  COOKIE_PLANET  ###
                    if cookies >= upgrades.Cookie_planet.cost_upgrade:
                        print("Zakupiono Cookie_planet")
                        cookies_per_second = cookies_per_second + upgrades.Cookie_planet.cookies_per_second
                        print(cookies_per_second)
                        cookies = cookies - upgrades.Cookie_planet.cost_upgrade
                        upgrades.Cookie_planet.quantity += 1

                        print(upgrades.Cookie_planet.quantity)
                        if upgrades.Cookie_planet.quantity >= 2:
                            upgrades.Cookie_planet.cost_upgrade = upgrades.Cookie_planet.cost_upgrade + 8000

                    else:
                        print("Nie stać Cię na Cookie_planet!")



            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if Cookie_factory_rect.collidepoint(x,y):                             ###  COOKIE_FACTORY  ###
                    if cookies >= upgrades.Cookie_factory.cost_upgrade:
                        print("Zakupiono Cookie_factory")
                        cookies_per_second = cookies_per_second + upgrades.Cookie_factory.cookies_per_second
                        print(cookies_per_second)
                        cookies = cookies - upgrades.Cookie_factory.cost_upgrade
                        upgrades.Cookie_factory.quantity += 1

                        print(upgrades.Cookie_factory.quantity)
                        if upgrades.Cookie_factory.quantity >= 2:
                            upgrades.Cookie_factory.cost_upgrade = upgrades.Cookie_factory.cost_upgrade + 20000

                    else:
                        print("Nie stać Cię na Cookie_factory!")



            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if Cookie_farm_rect.collidepoint(x,y):                             ###  COOKIE_FARM  ###
                    if cookies >= upgrades.Cookie_farm.cost_upgrade:
                        print("Zakupiono Cookie_farm")
                        cookies_per_second = cookies_per_second + upgrades.Cookie_farm.cookies_per_second
                        print(cookies_per_second)
                        cookies = cookies - upgrades.Cookie_farm.cost_upgrade
                        upgrades.Cookie_farm.quantity += 1

                        print(upgrades.Cookie_farm.quantity)
                        if upgrades.Cookie_farm.quantity >= 2:
                            upgrades.Cookie_farm.cost_upgrade = upgrades.Cookie_farm.cost_upgrade + 2500

                    else:
                        print("Nie stać Cię na Cookie_farm!")
                
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if Grandma_rect.collidepoint(x,y):                                ###  GRANDMA  ###
                    if cookies >= upgrades.Grandma.cost_upgrade:
                        print("Zakupiono Grandma")
                        cookies_per_second = cookies_per_second + upgrades.Grandma.cookies_per_second
                        print(cookies_per_second)
                        cookies = cookies - upgrades.Grandma.cost_upgrade
                        upgrades.Grandma.quantity += 1

                        print(upgrades.Grandma.quantity)
                        if upgrades.Grandma.quantity >= 2:
                            upgrades.Grandma.cost_upgrade = upgrades.Grandma.cost_upgrade + 500

                    else:
                        print("Nie stać Cię na Grandma!")



            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if autoclick_rect.collidepoint(x,y):                                ###  AUTOCLICK  ###
                    if cookies >= upgrades.Autoclick.cost_upgrade:
                        print("Zakupiono Autoclick")
                        cookies_per_second = cookies_per_second + upgrades.Autoclick.cookies_per_second
                        print(cookies_per_second)
                        cookies = cookies - upgrades.Autoclick.cost_upgrade
                        upgrades.Autoclick.quantity += 1

                        print(upgrades.Autoclick.quantity)
                        if upgrades.Autoclick.quantity >= 3:
                            upgrades.Autoclick.cost_upgrade = upgrades.Autoclick.cost_upgrade + 200

                    else:
                        print("Nie stać Cię na Autoclick!")



            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if cursor_rect.collidepoint(x,y):                                ###  CURSOR  ###
                    if cookies >= upgrades.Cursor.cost_upgrade:
                        print("Zakupiono Cursor")
                        tap_cookies += 1
                        cookies = cookies - upgrades.Cursor.cost_upgrade
                        upgrades.Cursor.quantity += 1
                        print(upgrades.Cursor.quantity)
                        if upgrades.Cursor.quantity >= 2:
                            upgrades.Cursor.cost_upgrade = upgrades.Cursor.cost_upgrade + 100

                    else:
                        print("Nie stać Cię na Cursor!")



#####################################   PLAYER CLICK COOKIE    ##############################################

            position_of_mouse = pygame.mouse.get_pos()
            mouse_position_in_mask = position_of_mouse[0] - cookie_rect.x, position_of_mouse[1] - cookie_rect.y
            if cookie_rect.collidepoint(position_of_mouse) and mask.get_at(mouse_position_in_mask) == 1:
                if_touching = 1
            else:
                if_touching = 0
            if event.type == pygame.MOUSEBUTTONDOWN and if_touching:
                print('clicked on image')
                cookies += tap_cookies
                print(cookies)

######################################## PYGAME QUIT #########################################################

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        draw_window()

        pygame.display.update()

if __name__ == "__main__":
    main()