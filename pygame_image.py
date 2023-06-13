import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgs = [bg_img,pg.transform.flip(bg_img, True, False)]
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img2 = pg.image.load("ex01/fig/4.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img2 = pg.transform.flip(kk_img2,True,False)
    x = 0
    
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img, 10, 1.0),kk_img,pg.transform.rotozoom(kk_img2, 0, 1.0)]
    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        ##

        print(x)
        screen.blit(bg_imgs[tmr % 1],[-tmr, 0])

        #screen.blit(bg_imgs[0],[0, 0])


        screen.blit(kk_imgs[tmr % len(kk_imgs)],[300, 200])
        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()