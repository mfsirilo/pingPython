# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
#coding: utf-8
import sys
import os
import platform
import subprocess
from ips_list import radius
import math
import csv

def metodoPosicaoFalsaPosicao(f, a, b, tol, N):
    i = 1
    FA = f
    a1 = FA(a)
    b1 = FA(b)
    print('# iteracao:', 'Valor a: ','Valor f(a):','Valor b:', ' Valor f(b):', ' Valor xc:',' Valor f(xc)',' Valor a1 * b1')
    try:
        while i <= N:
            xc = ((a*b1)-(b*a1))/((b1-a1))
            fxc = FA(xc)
            # print('Ite:', i,'Val a: ', a,'Val f(a):', a1, 'Val b:',b, ' Val f(b):', b1, ' Val xc:', xc,' Val f(c)',fxc,' Val f(a)*f(b)',a1*b1)
            print(i,' | ', a,' | ',a1,' | ',b,' | ', b1,' | ', xc,' | ',fxc,' | ',a1*b1)
            arq = csv.writer(open("ping.csv", 'ab+'))
            arq.writerow([i, xc, fxc])
            if fxc == 0 or abs(fxc) < tol:
                return xc
            if a1 * fxc > 0:
                a = xc
                a1 = f(xc) 
            else:
                b = xc
                b1 = f(xc)
            i=i+1
    except:
            return 'The procedure was unsuccessful.'

def rewriteB():
    linhas = []
    with open("ping.csv", 'r') as file:
        spamreader = csv.reader(file, delimiter=',')
        for linha in spamreader:
            linhas.append({'iteracao': linha[0], 'x': linha[1], 'f(x)': linha[2]})
        file.close()
    with open("ping.csv", 'wb') as file:
        field = ['iteracao', 'x', 'f(x)']
        writer = csv.DictWriter(file, fieldnames=field)
        writer.writeheader()
        for i in linhas:
            writer.writerow(i)

#ENTRADA DE DADOS

# funcao = lambda x: (x**3)-(x) - 4.0
funcao = lambda x: (x**3)-(9.0*x)+5.0

pontoa = 0.5
pontob = 1.0
tolerancia = 0.01
NumeroTentativas = 10

metodoPosicaoFalsaPosicao(funcao, pontoa, pontob, tolerancia, NumeroTentativas)
# rewriteB()