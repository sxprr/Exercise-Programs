# Python Inventory.
# script01102020

import sys
import time
import os
import random

class Game:
       def Start():
              versNum = 0.56 
              print("-------- Version" , versNum)
              print("""Hello, welcome to the game.
Type 'Game.Help()' if you need information.""")
       
       def Help():
              print("""Command list:
------ Player ------
1. 'Player.Stats(Name) = Prints the players name.' """)

class Item:

       def __init__(self, Name, Stock, Desc, Price, Effect):
              self.itemName = Name
              self.itemStock = '('+ str(Stock) + ') ' + 'in stock.'
              self.itemDesc = Desc
              self.itemPrice = Price
              self.itemEffect = Effect

       def Info(self):
              print('Information about ' + self.itemName + ':')
              print(self.itemStock)
              print("'" + self.itemDesc + "'")
              print(self.itemPrice)
              print(self.itemEffect)

       def Refine(self):
              pass

       def anotherTest():
              pass


class Player:
       def __init__(self, name, inventory, balance, debt):
              self.name = name
              self.inventory = inventory
              self.balance = balance
              self.debt = debt

       def Stats(self):
              print("Stats for " + self.name + ":")
              print("Items:" , self.inventory)
              print("Money: " + str(self.balance))
              print(self.name + " currently owes " + str(self.debt))

       def Kill(self):
              playerDeath = self.name + " is now dead."
              print(playerDeath + " He has lost everything.")
              print()
              self.inventory = ['']
              self.balance = 0

       def PunchFace(self):
              playerResult = self.balance / 2
              print(self.name + ' got punched in thier face.')
              print(self.name + ' also lost some money. ' + str(self.name) + ' now has ' + str(playerResult))

              #Update the variable
              self.balance = playerResult 

       def IsAlive(self):
              # whether they are alive depends on how much stuff they have
              aliveBool = 0
              aliveBool > len(self.inventory)

              if len(self.inventory) == 0:
                     print(self.name + " is alive.")
              else:
                     print(self.name + " is dead.")
                     




Game.Start()      



       ## shield
       ## (5) in stock
       ## this is a sturdy shield
       ## price = 400  
