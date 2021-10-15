import random
import pygame
from Player import Player
from Deck import Deck
from Card import Card

from sys import exit

deck = Deck()
players = [Player(), Player(), Player(), Player()]
pygame.init()

# Setting up screen and gui pop up
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Truco")
screen.fill((0, 128, 0))  # Makes the background green using (R, G, B) values

# Creating the players and passing out cards
for i in range(0, 4):
    for j in range(0, 3):
        players[i].take_card(deck.draw())


def player_Hand():
    for p in players:
        cards = [p.myCards[0].toString(), p.myCards[1].toString(), p.myCards[2].toString()]
        if p == players[0]:
            xPos, yPos = 338, 500 # Bottom of the screen (338, 500)
            for i in range(0, 3):
                screen.blit(pygame.image.load(cards[i]), (xPos, yPos))
                xPos += 32
        if p == players[1]:
            xPos, yPos = 700, 300 # middle right of the screen (700,300)
            for i in range(0, 3):
                image = pygame.image.load(cards[i])
                rotated_Card = pygame.transform.rotate(image, 90)
                screen.blit(rotated_Card, (xPos, yPos))
                yPos -= 32
        if p == players[2]:
            xPos, yPos = 400, 16 # Top middle of the screen (400, 16)
            for i in range(0, 3):
                image = pygame.image.load(cards[i])
                rotated_Card = pygame.transform.rotate(image, 180)
                screen.blit(rotated_Card, (xPos, yPos))
                xPos -= 32
        if p == players[3]:
            xPos, yPos = 16, 228 # middle left of the screen (16, 228)
            for i in range(0, 3):
                image = pygame.image.load(cards[i])
                rotated_Card= pygame.transform.rotate(image, 270)
                screen.blit(rotated_Card, (xPos, yPos))
                yPos += 32


while True: # runs the game and only quits if the X button was pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN: # checks if the mouse button was pressed
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]


    player_Hand()
    pygame.display.update()

