import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

# tamanho da tela
largura = 640
altura = 480
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('timesnewroman', 30, bold = False, italic = False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Curso de Game no Python')
relogio = pygame.time.Clock()
lista_cobra = []

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = [x,y]
        # XeY[0] = x
        # XeY[1] = y

        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

# Duração do game aberto
while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    # Controle de movimentos
    if pygame.key.get_pressed()[K_LEFT]:
        x_cobra -= 20
    if pygame.key.get_pressed()[K_RIGHT]:
        x_cobra += 20
    if pygame.key.get_pressed()[K_UP]:
        y_cobra -= 20
    if pygame.key.get_pressed()[K_DOWN]:
        y_cobra += 20

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (460, 40))
    pygame.display.update()
