import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習１
    bg_img2 = pg.transform.flip(bg_img, True, False)  # 練習8
    kk_img = pg.image.load("fig/pg.jpg") #練習３
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_rct = kk_img.get_rect()  # 練習10：こうかとんRectの取得
    kk_rct.center = 300, 200  # 練習10：こうかとんの初期座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()  # 練習10：すべてのキーの押下状態の取得
        # print(key_lst)
        if key_lst[pg.K_UP]:  # 上矢印キーが押されていたら
            kk_rct.move_ip(0, -1)
        if key_lst[pg.K_DOWN]:  # 下矢印キーが押されていたら
            kk_rct.move_ip(0, +1)
        if key_lst[pg.K_LEFT]:  # 左矢印キーが押されていたら
            kk_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]:  # 右矢印キーが押されていたら
            kk_rct.move_ip(+1, 0)
    
        x=tmr%3200 #練習５
        screen.blit(bg_img, [0, 0]) #練習２
        screen.blit(bg_img2, [-x+1600, 0])  # 練習7
        screen.blit(bg_img, [-x+3200, 0])  # 練習9
        
        screen.blit(kk_img, kk_rct)  # 練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習６


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()