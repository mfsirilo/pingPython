# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import math
import csv

def bisection_method(fx, a, b, tol, N):
        i = 1
        FA = fx(a)
        print('# iteracao:', 'Valor a: ','Valor f(a):','Valor b:',' Valor xc:',' Valor f(xc)',)
        try:
            while i <= N:
                p = (a+b)/2.0
                FP = fx(p)
                print(i,' | ',a,' | ',FA,' | ',b,' | ',p,' | ', FP)
                arq = csv.writer(open("bisseccao.csv", 'ab+'))
                arq.writerow([i, p, FP])
                if FP == 0 or abs(p) < tol:
                    return p
                i+=1

                if FA*FP > 0:
                    a = p
                    FA=fx(a)
                else:   
                    b = p
        except:
            return 'The procedure was unsuccessful.'
# abmais 

def rewriteB():
    linhas = []
    with open("bisseccao.csv", 'r') as file:
        spamreader = csv.reader(file, delimiter=',')
        for linha in spamreader:
            linhas.append({'iteracao': linha[0], 'x': linha[1], 'f(x)': linha[2]})
        file.close()
    with open("bisseccao.csv", 'wb') as file:
        field = ['iteracao', 'x', 'f(x)']
        writer = csv.DictWriter(file, fieldnames=field)
        writer.writeheader()
        for i in linhas:
            writer.writerow(i)


funcao = lambda x: (x**3)-(9.0*x)+5.0

pontoa = 0.5
pontob = 1.0
tolerancia = 0.01
NumeroTentativas = 10000

bisection_method(funcao,pontoa,pontob,tolerancia,NumeroTentativas)

rewriteB()
