import palgame

LARGURA_DA_TELA = 500
ALTURA_DA_TELA = 300
palgame.build_screen(LARGURA_DA_TELA, ALTURA_DA_TELA) 

while True:
    palgame.get_event()
    palgame.clear_screen()

    palgame.draw_everything()

