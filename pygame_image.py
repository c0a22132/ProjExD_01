import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bgReverse_img = pg.transform.flip(bg_img, True, False)
    koukaton_img = pg.image.load("ex01/fig/3.png")
    koukaton2_img = pg.image.load("ex01/fig/4.png")
    koukaton2R_img = pg.transform.flip(koukaton2_img, True, False)
    koukatonR_img = pg.transform.flip(koukaton_img, True, False)
    koukatonRR_img = [koukaton2R_img, pg.transform.rotate(koukatonR_img, 10)]
    x = 0
    x2 = 0

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bgReverse_img, [1600-x2, 0])
        screen.blit(bg_img, [3200-x2, 0])
        if tmr <= 40:
            screen.blit(koukatonRR_img[0], [300, 200])
        else:
            screen.blit(koukatonRR_img[1], [300, 200])
        pg.display.update()
        tmr += 1

        if tmr >= 60:
            tmr=0
        x += 1
        if x >= 1600:
            x = 0
        x2 += 1
        if x2 >= 6200:
            x2 -= 6200   
        clock.tick(200)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()