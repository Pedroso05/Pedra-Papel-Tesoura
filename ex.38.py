import random
import pygame

pygame.init()

print('VAMOS JOGAR PEDRA, PAPEL E TESOURA')
print('[0] tesoura')
print('[1] papel')
print('[2] pedra')
op = int(input('Faça uma jogada: '))

npc = random.randint(0, 2)

if op == npc:
    print('Empatou, tente de novo')
    print(npc)

elif op == 0 and npc == 1 or op == 1 and npc == 2 or op == 2 and npc == 0:
    print('Parabens voce ganhou !!!')
    pygame.mixer.music.load('success-alert.wav')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()


elif op == 0 and npc == 2 or op == 1 and npc == 0 or op == 2 and npc == 1 :
    print('Voce perdeu, tente de novo')
    pygame.mixer.music.load('error-alert.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

else:
    print("Voce selecionou uma opçao que nao existe, volte e tente de novo.")
