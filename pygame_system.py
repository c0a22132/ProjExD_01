import pygame as pg
import sys

def main():
    pg.display.set_caption("はじめてのPygame")# タイトルバーに表示する文字
    screen = pg.display.set_mode((800, 600))# 画面を作成
    clock = pg.time.Clock()# クロックオブジェクトを作成
    font = pg.font.Font(None, 80)# フォントオブジェクトを作成

    enn = pg.Surface((20, 20))#空のSurfaceオブジェクトを作成
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)# Surfaceオブジェクトに円する描画
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200])
        screen.blit(enn, [100, 400])
        pg.display.update()
        tmr += 1        
        clock.tick(1)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()