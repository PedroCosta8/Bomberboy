import pygame
import sys
import time

pygame.init()


pygame.display.set_caption("Bomberboy")
bomber = pygame.image.load('imagens/baixo00.png')
bomberect = bomber.get_rect()
bomberect.x= 33
bomberect.y = 31
resolucao = 550, 467+40
font = pygame.font.Font(None,32)
barra = pygame.image.load('imagens/barra.png')
Enemy = pygame.image.load('imagens/inimigo/baixo00.png')
Ebaixo01 = pygame.image.load('imagens/inimigo/baixo01.png')
Ebaixo02 = pygame.image.load('imagens/inimigo/baixo02.png')
Ebaixo = [Enemy, Ebaixo01, Ebaixo02]
Edir00 = pygame.image.load('imagens/inimigo/dir00.png')
Edir01 = pygame.image.load('imagens/inimigo/dir01.png')
Edir02 = pygame.image.load('imagens/inimigo/dir02.png')
Edir = [Edir00, Edir01, Edir02]
Eesq00 = pygame.image.load('imagens/inimigo/esq00.png')
Eesq01 = pygame.image.load('imagens/inimigo/esq01.png')
Eesq02 = pygame.image.load('imagens/inimigo/esq02.png')
Eesq = [Eesq00, Eesq01, Eesq02]
Eup00 = pygame.image.load('imagens/inimigo/up00.png')
Eup01 = pygame.image.load('imagens/inimigo/up01.png')
Eup02 = pygame.image.load('imagens/inimigo/up02.png')
Eup = [Eup00, Eup01, Eup02]
pontuador = 0
vida = 1
music = pygame.mixer.music.load('sons/Super Bomberman - Level 1 (ost snes).mp3')
pygame.mixer.music.play(-1, 0.0)
explosaoSound = pygame.mixer.Sound('sons/explosion-01 (online-audio-converter.com).wav')

rect_inimies = [Enemy.get_rect(), Enemy.get_rect(), Enemy.get_rect(), Enemy.get_rect(),Enemy.get_rect()]
rect_inimies[0].x = 39
rect_inimies[0].y = 322
rect_inimies[1].x = 261
rect_inimies[1].y = 28
rect_inimies[2].x = 225
rect_inimies[2].y = 325
rect_inimies[3].x = 411
rect_inimies[3].y = 175
rect_inimies[4].x = 486
rect_inimies[4].y = 361
vel = 2
c1 = True
d1 = True
e1 = True
b1 = True

c2 = True
d2 = True
e2 = True
b2 = True

c3 = True
d3 = True
e3 = True
b3 = True

c4 = True
d4 = True
e4 = True
b4 = True

c5 = True
d5 = True
e5 = True
b5 = True

def movimento_inimigo1():
    global c1, b1, d1, e1, passCont
    if d1:
        if rect_inimies[0].x != 111:
            rect_inimies[0].x += vel
        else:
            d1 = False
            b1 = False
            e1 = False
            c1 = True
    elif c1:
        if rect_inimies[0].y != 178:
            rect_inimies[0].y -= vel
        else:
            c1 = False
            e1 = True
            d1 =False
            b1 = False
    elif e1:
        if rect_inimies[0].x != 39:
            rect_inimies[0].x -= vel
        else:
            e1 = False
            b1 = True
            d1 = False
            c1 = False
    elif b1:
        if rect_inimies[0].y != 322:
            rect_inimies[0].y += vel
        else:
            b1 = False
            d1 = True
            c1 = False
            e1 = False

def movimento_inimigo2():
    global d2, e2
    if d2:
        if rect_inimies[1].x != 379:
            rect_inimies[1].x += vel
        else:
            e2 = True
            d2 = False

    elif e2:
        if rect_inimies[1].x != 217:
            rect_inimies[1].x -= vel
        else:
            e2 = False
            d2 = True

def movimento_inimigo3():
    global c3, b3, d3, e3
    if d3:
        if rect_inimies[2].x != 487:
            rect_inimies[2].x += vel
        else:
            d3 = False
            b3 = False
            e3 = False
            c3 = True
    elif c3:
        if rect_inimies[2].y != 31:
            rect_inimies[2].y -= vel
        else:
            c3 = False
            e3 = False
            d3 = False
            b3 = True
    elif b3:
        if rect_inimies[2].y != 325:
            rect_inimies[2].y += vel
        else:
            b3 = False
            d3 = False
            c3 = False
            e3 = True
    elif e3:
        if rect_inimies[2].x != 225:
            rect_inimies[2].x -= vel
        else:
            b3 = False
            c3 = False
            e3 = False
            d3 = True

def movimento_inimigo4():
    global b4, c4
    if b4:
        if rect_inimies[3].y != 275:
            rect_inimies[3].y += vel
        else:
            c4 = True
            b4 = False

    elif c4:
        if rect_inimies[3].y != 143:
            rect_inimies[3].y -= vel
        else:
            c4 = False
            b4 = True

def movimento_inimigo5():
    global c5, b5, d5, e5
    if c5:
        if rect_inimies[4].y != 251:
            rect_inimies[4].y -= vel
        else:
            d5 = False
            b5 = False
            e5 = True
            c5 = False
    elif e5:
        if rect_inimies[4].x != 408:
            rect_inimies[4].x -= vel
        else:
            c5 = False
            e5 = False
            d5 = True
            b5 = False
    elif d5:
        if rect_inimies[4].x != 486:
            rect_inimies[4].x += vel
        else:
            e5 = False
            b5 = True
            d5 = False
            c5 = False
    elif b5:
        if rect_inimies[4].y != 361:
            rect_inimies[4].y += vel
        else:
            b5 = False
            d5 = False
            c5 = True
            e5 = False

clock = pygame.time.Clock()
left = False
right = False
up = False
down = False
parado = True
passCont = 0
temporizador = False
sec = 0
tempo = pygame.time.get_ticks()
segundos = 200

parede_sup = pygame.Rect(0, 0, 550, 28)
parede_inf = pygame.Rect(0, 435, 550, 32)
parede_dir = pygame.Rect(519, 0, 33, 467)
parede_esq = pygame.Rect(0, 0, 33, 467)

bloco1 = pygame.Rect(73, 66, 35, 30)
bloco2 = pygame.Rect(149, 66, 35, 30)
bloco3 = pygame.Rect(223, 66, 35, 30)
bloco4 = pygame.Rect(297, 66, 35, 30)
bloco5 = pygame.Rect(371, 66, 35, 30)
bloco6 = pygame.Rect(445, 66, 35, 30)
bloco7 = pygame.Rect(73, 140, 35, 30)
bloco8 = pygame.Rect(149, 140, 35, 30)
bloco9 = pygame.Rect(223, 140, 35, 30)
bloco10 = pygame.Rect(297, 140, 35, 30)
bloco11 = pygame.Rect(371, 140, 35, 30)
bloco12 = pygame.Rect(445, 140, 35, 30)
bloco13 = pygame.Rect(73, 214, 35, 30)
bloco14 = pygame.Rect(149, 214, 35, 30)
bloco15 = pygame.Rect(223, 214, 35, 30)
bloco16 = pygame.Rect(297, 214, 35, 30)
bloco17 = pygame.Rect(371, 214, 35, 30)
bloco18 = pygame.Rect(445, 214, 35, 30)
bloco19 = pygame.Rect(73, 288, 35, 30)
bloco20 = pygame.Rect(149, 288, 35, 30)
bloco21 = pygame.Rect(223, 288, 35, 30)
bloco22 = pygame.Rect(297, 288, 35, 30)
bloco23 = pygame.Rect(371, 288, 35, 30)
bloco24 = pygame.Rect(445, 288, 35, 30)
bloco25 = pygame.Rect(73, 362, 35, 30)
bloco26 = pygame.Rect(149, 362, 35, 30)
bloco27 = pygame.Rect(223, 362, 35, 30)
bloco28 = pygame.Rect(297, 362, 35, 30)
bloco29 = pygame.Rect(371, 362, 35, 30)
bloco30 = pygame.Rect(445, 362, 35, 30)


baixo0 = bomber
baixo1 = pygame.image.load('imagens/baixo01.png')
baixo2 = pygame.image.load('imagens/baixo02.png')
baixo3 = pygame.image.load('imagens/baixo02.png')
baixo4 = pygame.image.load('imagens/baixo04.png')
baixo5 = pygame.image.load('imagens/baixo05.png')
baixo6 = pygame.image.load('imagens/baixo06.png')
baixo7 = pygame.image.load('imagens/baixo07.png')
baixo = [baixo0, baixo1, baixo2, baixo3, baixo4, baixo5, baixo6, baixo7]

cima0 = pygame.image.load('imagens/up00.png')
cima1 = pygame.image.load('imagens/up01.png')
cima2 = pygame.image.load('imagens/up02.png')
cima3 = pygame.image.load('imagens/up03.png')
cima4 = pygame.image.load('imagens/up04.png')
cima5 = pygame.image.load('imagens/up05.png')
cima6 = pygame.image.load('imagens/up06.png')
cima7 = pygame.image.load('imagens/up07.png')
cima = [cima0, cima1, cima2, cima3, cima4, cima5, cima6, cima7]
lado0 = pygame.image.load('imagens/lado00.png')
lado1 = pygame.image.load('imagens/lado01.png')
lado2 = pygame.image.load('imagens/lado02.png')
lado3 = pygame.image.load('imagens/lado03.png')
lado4 = pygame.image.load('imagens/lado04.png')
lado5 = pygame.image.load('imagens/lado05.png')
lado6 = pygame.image.load('imagens/lado06.png')
lado7 = pygame.image.load('imagens/lado07.png')
lado = [lado0, lado1, lado2, lado3, lado4, lado5, lado6, lado7]

bd_image = pygame.image.load('imagens/bloco.png')
width = 35
height = 35
#blocos destrutíveis

blocos_dest = [pygame.Rect(111, 30, width, height), pygame.Rect(111+width, 30, width, height), pygame.Rect(111+(width*2), 30, width, height), pygame.Rect(409, 31, width, height), pygame.Rect(111, 30+width, width, height), pygame.Rect(409, 31+width, width, height), pygame.Rect(72, 102, width, height), pygame.Rect(72+width, 102, width, height), pygame.Rect(72+(width*2), 102, width, height), pygame.Rect(409, 102, width, height), pygame.Rect(36, 141, width, height), pygame.Rect(147, 178, width, height), pygame.Rect(222, 178, width, height), pygame.Rect(333, 178, width, height), pygame.Rect(333, 178+width, width, height), pygame.Rect(149, 250, width, height), pygame.Rect(149+width, 250, width, height), pygame.Rect(296, 250, width, height), pygame.Rect(296+width, 250, width, height), pygame.Rect(296+(width*2), 250, width, height), pygame.Rect(149+width, 286, width, height), pygame.Rect(149, 326, width, height), pygame.Rect(36, 400, width, height), pygame.Rect(111, 400, width, height), pygame.Rect(111+width, 400, width, height), pygame.Rect(305, 400, width, height), pygame.Rect(305+width, 400, width, height), pygame.Rect(305+(width*2), 400, width, height), pygame.Rect(305+(width*3), 400, width, height), pygame.Rect(305+(width*4), 400, width, height), pygame.Rect(305+(width*5), 400, width, height)]

tela = pygame.display.set_mode(resolucao)
arena = pygame.image.load('imagens/background_bomberboy.png')

def movimento(keys, bomberect):
    global left, right, up, down, passCont, parado, ele1, ele2, rect_inimies, vida
    if keys[pygame.K_LEFT]:
        left = True
        right = False
        up = False
        down = False
        parado = False
        bomberect.x -= 3
        if bomberect.colliderect(parede_esq):
            bomberect.x = parede_esq.width

    elif keys[pygame.K_RIGHT]:
        right = True
        left = False
        up = False
        down = False
        parado = False
        bomberect.x += 3
        if bomberect.colliderect(parede_dir):
            bomberect.x = 550 - parede_dir.width - bomberect.width
        if bomberect.x + bomberect.width > 550:
            bomberect.x = 550 - bomberect.width

    elif keys[pygame.K_UP]:
        left = False
        right = False
        up = True
        down = False
        parado = False
        bomberect.y -= 3
        if bomberect.colliderect(parede_sup):
            bomberect.y = parede_sup.height

    elif keys[pygame.K_DOWN]:
        left = False
        right = False
        up = False
        down = True
        parado = False
        bomberect.y += 3
        if bomberect.colliderect(parede_inf):
            bomberect.y = 467 - parede_inf.height - 35
    else:
        parado = True
        passCont = 0

    if bomberect.colliderect(bloco1):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco2):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco3):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco4):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco5):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco6):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco7):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco8):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco9):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco10):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco11):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco12):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco13):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco14):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco15):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco16):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco17):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco18):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco19):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco20):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco21):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco22):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco23):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco24):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco25):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco26):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco27):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco28):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco29):
        bomberect.left, bomberect.top = xant, yant
    if bomberect.colliderect(bloco30):
        bomberect.left, bomberect.top = xant, yant


    for elemento in blocos_dest:
        if bomberect.colliderect(elemento):
            bomberect.left, bomberect.top = xant, yant
    for inimigo in range(len(rect_inimies)):
        if bomberect.colliderect(rect_inimies[inimigo]):
            vida -= 1


def explosoes():
    global explc, exple1, exple2, explb1, explb2, expld1, expld2, explu1, explu2, blocos_dest, pontuador, vida
    explc = pygame.Rect(xbomb, ybomb, 30, 30)
    exple1 = pygame.Rect(xbomb - 30, ybomb, 30, 30)


    expld1 = pygame.Rect(xbomb + 30, ybomb, 30, 30)

    explb1 = pygame.Rect(xbomb, ybomb + 30, 30, 30)

    explu1 = pygame.Rect(xbomb, ybomb - 30, 30, 30)


    if not (exple1.colliderect(parede_esq) or exple1.colliderect(bloco1) or exple1.colliderect(
        bloco2) or exple1.colliderect(bloco3) or exple1.colliderect(bloco4) or exple1.colliderect(
        bloco5) or exple1.colliderect(bloco6) or exple1.colliderect(bloco7) or exple1.colliderect(
        bloco8) or exple1.colliderect(bloco9) or exple1.colliderect(bloco10) or exple1.colliderect(
        bloco11) or exple1.colliderect(bloco12) or exple1.colliderect(bloco13) or exple1.colliderect(
        bloco14) or exple1.colliderect(bloco15) or exple1.colliderect(bloco16) or exple1.colliderect(
        bloco17) or exple1.colliderect(bloco18) or exple1.colliderect(bloco19) or exple1.colliderect(
        bloco20) or exple1.colliderect(bloco21) or exple1.colliderect(bloco22) or exple1.colliderect(
        bloco23) or exple1.colliderect(bloco24) or exple1.colliderect(bloco25) or exple1.colliderect(
        bloco26) or exple1.colliderect(bloco27) or exple1.colliderect(bloco28) or exple1.colliderect(
        bloco29) or exple1.colliderect(bloco30)):
        tela.blit(fogo_ext_horizontal, exple1)
        exple2 = pygame.Rect(xbomb - 60, ybomb, 30, 30)
        for o in range(len(rect_inimies)):
            if exple2.colliderect(rect_inimies[o]):
                rect_inimies[o].x = 30000
                rect_inimies[o].y = 30000
        for o in range(len(blocos_dest)):
            if exple2.colliderect(blocos_dest[o]):
                del (blocos_dest[o])
                blocos_dest.insert(o, pygame.Rect(3000, 3000, 1, 1))
        if exple2.colliderect(bomberect):
            vida -=1
        if not (exple2.colliderect(parede_esq) or exple2.colliderect(bloco1) or exple2.colliderect(
                        bloco2) or exple2.colliderect(bloco3) or exple2.colliderect(bloco4) or exple2.colliderect(
                        bloco5) or exple2.colliderect(bloco6) or exple2.colliderect(bloco7) or exple2.colliderect(
                        bloco8) or exple2.colliderect(bloco9) or exple2.colliderect(bloco10) or exple2.colliderect(
                        bloco11) or exple2.colliderect(bloco12) or exple2.colliderect(
                        bloco13) or exple2.colliderect(bloco14) or exple2.colliderect(
                        bloco15) or exple2.colliderect(bloco16) or exple2.colliderect(
                        bloco17) or exple2.colliderect(bloco18) or exple2.colliderect(
                        bloco19) or exple2.colliderect(bloco20) or exple2.colliderect(
                        bloco21) or exple2.colliderect(bloco22) or exple2.colliderect(
                        bloco23) or exple2.colliderect(bloco24) or exple2.colliderect(
                        bloco25) or exple2.colliderect(bloco26) or exple2.colliderect(
                        bloco27) or exple2.colliderect(bloco28) or exple2.colliderect(
                        bloco29) or exple2.colliderect(bloco30)):
            tela.blit(ponta_esq, exple2)


    if not (expld1.colliderect(parede_dir) or expld1.colliderect(bloco1) or expld1.colliderect(
        bloco2) or expld1.colliderect(bloco3) or expld1.colliderect(bloco4) or expld1.colliderect(
        bloco5) or expld1.colliderect(bloco6) or expld1.colliderect(bloco7) or expld1.colliderect(
        bloco8) or expld1.colliderect(bloco9) or expld1.colliderect(bloco10) or expld1.colliderect(
        bloco11) or expld1.colliderect(bloco12) or expld1.colliderect(bloco13) or expld1.colliderect(
        bloco14) or expld1.colliderect(bloco15) or expld1.colliderect(bloco16) or expld1.colliderect(
        bloco17) or expld1.colliderect(bloco18) or expld1.colliderect(bloco19) or expld1.colliderect(
        bloco20) or expld1.colliderect(bloco21) or expld1.colliderect(bloco22) or expld1.colliderect(
        bloco23) or expld1.colliderect(bloco24) or expld1.colliderect(bloco25) or expld1.colliderect(
        bloco26) or expld1.colliderect(bloco27) or expld1.colliderect(bloco28) or expld1.colliderect(
        bloco29) or expld1.colliderect(bloco30)):
        tela.blit(fogo_ext_horizontal, expld1)
        expld2 = pygame.Rect(xbomb + 60, ybomb, 30, 30)
        if expld2.colliderect(bomberect):
            vida -=1
        for o in range(len(rect_inimies)):
            if expld2.colliderect(rect_inimies[o]):
                rect_inimies[o].x = 30000
                rect_inimies[o].y = 30000
                pontuador +=1
        for o in range(len(blocos_dest)):
            if expld2.colliderect(blocos_dest[o]):
                del (blocos_dest[o])
                blocos_dest.insert(o, pygame.Rect(3000, 3000, 1, 1))
        if not (expld2.colliderect(parede_dir) or expld2.colliderect(bloco1) or expld2.colliderect(
                        bloco2) or expld2.colliderect(bloco3) or expld2.colliderect(bloco4) or expld2.colliderect(
                    bloco5) or expld2.colliderect(bloco6) or expld2.colliderect(bloco7) or expld2.colliderect(
                    bloco8) or expld2.colliderect(bloco9) or expld2.colliderect(bloco10) or expld2.colliderect(
                    bloco11) or expld2.colliderect(bloco12) or expld2.colliderect(bloco13) or expld2.colliderect(
                    bloco14) or expld2.colliderect(bloco15) or expld2.colliderect(bloco16) or expld2.colliderect(
                    bloco17) or expld2.colliderect(bloco18) or expld2.colliderect(bloco19) or expld2.colliderect(
                    bloco20) or expld2.colliderect(bloco21) or expld2.colliderect(bloco22) or expld2.colliderect(
                    bloco23) or expld2.colliderect(bloco24) or expld2.colliderect(bloco25) or expld2.colliderect(
                    bloco26) or expld2.colliderect(bloco27) or expld2.colliderect(bloco28) or expld2.colliderect(
                    bloco29) or expld2.colliderect(bloco30)):
            tela.blit(ponta_dir, expld2)





    if not (explu1.colliderect(parede_sup) or explu1.colliderect(bloco1) or explu1.colliderect(
        bloco2) or explu1.colliderect(bloco3) or explu1.colliderect(bloco4) or explu1.colliderect(
        bloco5) or explu1.colliderect(bloco6) or explu1.colliderect(bloco7) or explu1.colliderect(
        bloco8) or explu1.colliderect(bloco9) or explu1.colliderect(bloco10) or explu1.colliderect(
        bloco11) or explu1.colliderect(bloco12) or explu1.colliderect(bloco13) or explu1.colliderect(
        bloco14) or explu1.colliderect(bloco15) or explu1.colliderect(bloco16) or explu1.colliderect(
        bloco17) or explu1.colliderect(bloco18) or explu1.colliderect(bloco19) or explu1.colliderect(
        bloco20) or explu1.colliderect(bloco21) or explu1.colliderect(bloco22) or explu1.colliderect(
        bloco23) or explu1.colliderect(bloco24) or explu1.colliderect(bloco25) or explu1.colliderect(
        bloco26) or explu1.colliderect(bloco27) or explu1.colliderect(bloco28) or explu1.colliderect(
        bloco29) or explu1.colliderect(bloco30)):
        tela.blit(fogo_vertical, explu1)
        explu2 = pygame.Rect(xbomb, ybomb - 60, 30, 30)
        if explu2.colliderect(bomberect):
            vida -=1
        for o in range(len(rect_inimies)):
            if explu2.colliderect(rect_inimies[o]):
                rect_inimies[o].x = 30000
                rect_inimies[o].y = 30000
                pontuador+=1
        for o in range(len(blocos_dest)):
            if explu2.colliderect(blocos_dest[o]):
                del (blocos_dest[o])
                blocos_dest.insert(o, pygame.Rect(3000, 3000, 1, 1))
        if not (explu2.colliderect(parede_sup) or explu2.colliderect(bloco1) or explu2.colliderect(
                        bloco2) or explu2.colliderect(bloco3) or explu2.colliderect(bloco4) or explu2.colliderect(
                    bloco5) or explu2.colliderect(bloco6) or explu2.colliderect(bloco7) or explu2.colliderect(
                    bloco8) or explu2.colliderect(bloco9) or explu2.colliderect(bloco10) or explu2.colliderect(
                    bloco11) or explu2.colliderect(bloco12) or explu2.colliderect(bloco13) or explu2.colliderect(
                    bloco14) or explu2.colliderect(bloco15) or explu2.colliderect(bloco16) or explu2.colliderect(
                    bloco17) or explu2.colliderect(bloco18) or explu2.colliderect(bloco19) or explu2.colliderect(
                    bloco20) or explu2.colliderect(bloco21) or explu2.colliderect(bloco22) or explu2.colliderect(
                    bloco23) or explu2.colliderect(bloco24) or explu2.colliderect(bloco25) or explu2.colliderect(
                    bloco26) or explu2.colliderect(bloco27) or explu2.colliderect(bloco28) or explu2.colliderect(
                    bloco29) or explu2.colliderect(bloco30)):
            tela.blit(ponta_up, explu2)



    if not (explb1.colliderect(parede_inf) or explb1.colliderect(bloco1) or explb1.colliderect(
        bloco2) or explb1.colliderect(bloco3) or explb1.colliderect(bloco4) or explb1.colliderect(
        bloco5) or explb1.colliderect(bloco6) or explb1.colliderect(bloco7) or explb1.colliderect(
        bloco8) or explb1.colliderect(bloco9) or explb1.colliderect(bloco10) or explb1.colliderect(
        bloco11) or explb1.colliderect(bloco12) or explb1.colliderect(bloco13) or explb1.colliderect(
        bloco14) or explb1.colliderect(bloco15) or explb1.colliderect(bloco16) or explb1.colliderect(
        bloco17) or explb1.colliderect(bloco18) or explb1.colliderect(bloco19) or explb1.colliderect(
        bloco20) or explb1.colliderect(bloco21) or explb1.colliderect(bloco22) or explb1.colliderect(
        bloco23) or explb1.colliderect(bloco24) or explb1.colliderect(bloco25) or explb1.colliderect(
        bloco26) or explb1.colliderect(bloco27) or explb1.colliderect(bloco28) or explb1.colliderect(
        bloco29) or explb1.colliderect(bloco30)):
        tela.blit(fogo_vertical, explb1)
        explb2 = pygame.Rect(xbomb, ybomb + 60, 30, 30)
        if explb2.colliderect(bomberect):
            vida -=1
        for o in range(len(rect_inimies)):
            if explb2.colliderect(rect_inimies[o]):
                rect_inimies[o].x = 30000
                rect_inimies[o].y = 30000
                pontuador+=1
        for o in range(len(blocos_dest)):
            if explb2.colliderect(blocos_dest[o]):
                del (blocos_dest[o])
                blocos_dest.insert(o, pygame.Rect(3000, 3000, 1, 1))
        if not (explb2.colliderect(parede_inf) or explb2.colliderect(bloco1) or explb2.colliderect(
                        bloco2) or explb2.colliderect(bloco3) or explb2.colliderect(bloco4) or explb2.colliderect(
                    bloco5) or explb2.colliderect(bloco6) or explb2.colliderect(bloco7) or explb2.colliderect(
                    bloco8) or explb2.colliderect(bloco9) or explb2.colliderect(bloco10) or explb2.colliderect(
                    bloco11) or explb2.colliderect(bloco12) or explb2.colliderect(bloco13) or explb2.colliderect(
                    bloco14) or explb2.colliderect(bloco15) or explb2.colliderect(bloco16) or explb2.colliderect(
                    bloco17) or explb2.colliderect(bloco18) or explb2.colliderect(bloco19) or explb2.colliderect(
                    bloco20) or explb2.colliderect(bloco21) or explb2.colliderect(bloco22) or explb2.colliderect(
                    bloco23) or explb2.colliderect(bloco24) or explb2.colliderect(bloco25) or explb2.colliderect(
                    bloco26) or explb2.colliderect(bloco27) or explb2.colliderect(bloco28) or explb2.colliderect(
                    bloco29) or explb2.colliderect(bloco30)):
            tela.blit(ponta_down, explb2)


    for i in range(len(blocos_dest)):
        if explb1.colliderect(blocos_dest[i]) or exple1.colliderect(blocos_dest[i]) or expld1.colliderect(blocos_dest[i]) or explu1.colliderect(blocos_dest[i]):
            del(blocos_dest[i])
            blocos_dest.insert(i, pygame.Rect(3000, 3000, 1, 1))
    for i in range(len(rect_inimies)):
        if explb1.colliderect(rect_inimies[i]) or exple1.colliderect(rect_inimies[i]) or expld1.colliderect(rect_inimies[i]) or explu1.colliderect(rect_inimies[i] or explc.colliderect(rect_inimies[i])):
            rect_inimies[i].x = 30000
            rect_inimies[i].y = 30000
            pontuador+=1
    if explb1.colliderect(bomberect) or exple1.colliderect(bomberect) or expld1.colliderect(
        bomberect) or explu1.colliderect(bomberect) or explc.colliderect(bomberect):
        vida -=1

def mostra_na_tela():
    global passCont, lado, cima, baixo, parado, tempo, segundos, minutos, rect_inimies
    tela.blit(arena, (0, 0))
    tela.blit(barra, (0, 467))

    for i in range(len(blocos_dest)):
        tela.blit(bd_image, blocos_dest[i])
    for i in range(len(rect_inimies)):
        tela.blit(Enemy, rect_inimies[i])

    if not parado:
        if passCont + 1 >= 24:
            passCont = 0
        elif left:
            tela.blit(lado[passCont//3], bomberect)
            passCont += 1
        elif right:
            tela.blit(lado[passCont//3], bomberect)
            passCont += 1
        elif up:
            tela.blit(cima[passCont//3], bomberect)
            passCont += 1
        elif down:
            tela.blit(baixo[passCont//3], bomberect)
            passCont += 1
    else:
       if down:
           tela.blit(bomber, bomberect)
       elif up:
           tela.blit(cima[0], bomberect)
       elif left:
           tela.blit(lado[0], bomberect)
       elif right:
           tela.blit(lado[0], bomberect)
       else:
           tela.blit(bomber, bomberect)
    
    pygame.display.flip()

limitador = False


def bomba():
    global explosaoBomba, temporizador, sec, xbomb, ybomb, limitador, fogo_central, fogo_ext_horizontal, fogo_vertical, ponta_up, ponta_down, ponta_esq, ponta_dir, tempo

    imagebomba =pygame.image.load('imagens/bomba/bomba00.png')
    rectbomba = imagebomba.get_rect()
    fogo_central = pygame.image.load('imagens/bomba/fogo_orig.png')
    fogo_ext_horizontal = pygame.image.load('imagens/bomba/fogo_ext.png')
    fogo_vertical = pygame.image.load('imagens/bomba/fogo_ext_vert.png')
    ponta_up = pygame.image.load('imagens/bomba/fogo_ponta_vert.png')
    ponta_down = pygame.image.load('imagens/bomba/ponta_down.png')
    ponta_esq = pygame.image.load('imagens/bomba/ponta_esq.png')
    ponta_dir = pygame.image.load('imagens/bomba/fogo_ponta.png')

    if keys[pygame.K_SPACE] and limitador == False:
        temporizador = True
        xbomb = bomberect.x + 0
        ybomb = bomberect.y + 0
    if temporizador == True:
        limitador = True
        tela.blit(imagebomba, (xbomb, ybomb))
        if (pygame.time.get_ticks() - tempo) >= 1000:
            sec += 1
            tempo = pygame.time.get_ticks()


        if sec == 4:
            tela.blit(fogo_central, (xbomb, ybomb))
            explosaoSound.play()
            explosoes()

        if sec > 4:
            temporizador = False
            limitador = False
            sec = 0



    pygame.display.flip()
    #print(sec)



h = pygame.time.get_ticks()
#funcionamento do jogo
jogando = 'jogando'
while jogando == 'jogando':

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    movimento(keys, bomberect)
    movimento_inimigo1()
    movimento_inimigo2()
    movimento_inimigo3()
    movimento_inimigo4()
    movimento_inimigo5()
    xant, yant = (bomberect.left, bomberect.top)

    mostra_na_tela()
    bomba()


    if pygame.time.get_ticks() - h >= 1000:
        segundos-=1
        h = pygame.time.get_ticks()
        if segundos ==-1:
            segundos -=1
    relogio = font.render("Tempo: "+ str(segundos),True,(255,255,255))
    i_vida = font.render("Vida: "+ str(vida),True,(255,255,255))
    tela.blit(relogio, (50,477))
    tela.blit(i_vida, (250, 477))
    pygame.display.update()
    print(pontuador)
    if pontuador == 5:
        jogando = 'ganhou'
    if vida == 0 or segundos == 0:
        jogando = 'perdeu'
    while jogando == 'ganhou':
        pygame.mixer.music.stop()
        tela.fill((0,0,0))
        game_over = font.render('You Won!!!!!!!!!!!', True,(255,255,255))
        tela.blit(game_over,(225,253))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
    while jogando == 'perdeu':
        pygame.mixer.music.stop()
        tela.fill((0,0,0))
        game_over = font.render('Game Over', True,(255,255,255))
        tela.blit(game_over,(225,253))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
        
    
