# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
#coding: utf-8
import sys
import os
import platform
import subprocess
# from ips_list import radius
import math
import csv
import subprocess
from datetime import datetime
import time
import csv

ips = ['8.8.8.8','www.google.com']
contador=1
continuar=True
numeroDoPing=0

quantidadeDoTeste=input("Quantas vezes você deseja pingar o host?")

print "Ping #: |"," host     |", " status |"," Data Dia"
while True:
    agora = datetime.now()
    agora=agora.strftime('%d/%m/%Y %H:%M:%S')
    with open(os.devnull, "wb") as limbo:
        for ip in ips:
    
            result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "1", ip],
                    stdout=limbo, stderr=limbo).wait()
            if result:
                print ip, "inativo"
            else:
                print "    ",numeroDoPing," | ",ip," | ", "ativo"," | ",agora
    numeroDoPing+=1
    time.sleep(1)
    contador+=1
    if contador == quantidadeDoTeste:
        resposta = input('Continiuar?\n 0=SIM')
        if resposta == 0:
            contador=0
        else:
            break