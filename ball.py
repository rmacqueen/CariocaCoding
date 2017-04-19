import palgame

cor = (0, 0, 0)
LARGURA_DA_TELA = 500
ALTURA_DA_TELA = 300
palgame.build_screen(LARGURA_DA_TELA, ALTURA_DA_TELA) 
bola_x = 30
bola_y = 200
raio = 10
velocidade_x = 10
velocidade_y = 15
COLUNAS = 8
LINHAS = 5

DISTANCA = 10
LARGURA_DO_BLOCO = (LARGURA_DA_TELA / COLUNAS) - DISTANCA
ALTURA = 16

posicao_y = 0
blocos = []
for i in range(LINHAS):
    posicao_x = 5
    for j in range(COLUNAS):
        b = [posicao_x, posicao_y]
        blocos.append(b)
        posicao_x = posicao_x + LARGURA_DO_BLOCO + DISTANCA
    posicao_y = posicao_y + ALTURA + 5

while True:
    palgame.get_event()
    palgame.clear_screen()

    # Aqui estou atualizando a posicao da bola
    bola_x = bola_x + velocidade_x
    bola_y = bola_y + velocidade_y

    # Aqui as paredes
    if bola_x >= (LARGURA_DA_TELA - raio) or bola_x <= raio:
        velocidade_x = velocidade_x * (-1)


    if bola_y >= (ALTURA_DA_TELA - raio) or bola_y <= raio:
        velocidade_y = velocidade_y * (-1)

    palgame.draw_circle(bola_x, bola_y, raio, cor)

    for a in blocos:
        if (bola_x + raio) >= a[0] and (bola_x - raio) <= (a[0] + LARGURA_DO_BLOCO) and (bola_y + raio) >= a[1] and (bola_y - raio) <= (a[1] + ALTURA):
            blocos.remove(a)
            velocidade_y = velocidade_y * -1

    for b in blocos:
        palgame.draw_rect(b[0], b[1], LARGURA_DO_BLOCO, ALTURA)

    palgame.draw_everything()

