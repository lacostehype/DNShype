import socket
import os

os.system ('clear')
os.system('figlet -f slant DNS hype')
os.system('figlet -f digital V - 1.0')
host = input(' Digite o Dominio:')

try:
    print (host, '>>>', socket.gethostbyname(host))
except Exception as erro:
    print ('OCORREU UM ERRO >>>', erro)


# Espero que gostem é a primeira versão então está bem simples
