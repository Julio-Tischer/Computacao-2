import numpy as np
import pandas as panda
import math
import matplotlib.pyplot as plot

def edo_Function (x,y):
    """"Escreva a EDO aqui, qualquer uma"""
    result = -(y+1)*(y+3)
    return result

def edo_ExactSolution (x):
    """"Sol exata vem aqui, não esqeuça"""
    result = -3+2/(1+math.e**(-2*x))
    return result


def met_Euler (EDO_Function,start_Point,end_Point,steps,initial_Value):
    """"Esta vai ser a função responsavel por realizar o metodo de Euler normal"""

    #Definir comprimento do intervalo
    h = (end_Point - start_Point)/steps

    #Criar usando numpy uma tabela de zeros de tamnaho steps por 2 colunas
    resultsTable = np.zeros((steps+1,2))

    #Define W0 e X0 (primeiro valor da tabela, como ponto inicial e valor inicial)
    resultsTable[0] = [start_Point,initial_Value]

    #Para toda linha da tabela
    for i in range(len(resultsTable)-1):
        
        #Lembre que Wi é o [i,1] e Xi é o [i,0]

        #Encontrar X(i+1)
        resultsTable[i+1,0] = resultsTable[i,0] + h

        #Encontrar W(i+1)
        resultsTable[i+1,1] = resultsTable[i,1] + h*EDO_Function(resultsTable[i,0],resultsTable[i,1])
        
    
    return resultsTable



def met_PMedio (EDO_Function,start_Point,end_Point,steps,initial_Value):
    """"Esta vai ser a função responsavel por realizar o metodo de ponto medio"""

    #Definir comprimento do intervalo
    h = (end_Point - start_Point)/steps

    #Criar usando numpy uma tabela de zeros de tamnaho steps por 2 colunas
    resultsTable = np.zeros((steps+1,2))

    #Define W0 e X0 (primeiro valor da tabela, como ponto inicial e valor inicial)
    resultsTable[0] = [start_Point,initial_Value]

    #Para toda linha da tabela
    for i in range(len(resultsTable)-1):
        
        #Lembre que Wi é o [i,1] e Xi é o [i,0]

        #Encontrar X(i+1)
        resultsTable[i+1,0] = resultsTable[i,0] + h

        #Encontrar W(i+1)
        resultsTable[i+1,1] = resultsTable[i,1] + h*EDO_Function((resultsTable[i,0]+h/2),(resultsTable[i,1]+(h/2)*EDO_Function(resultsTable[i,0],resultsTable[i,1])))
        
    
    return resultsTable

def met_EulerMelhorado (EDO_Function,start_Point,end_Point,steps,initial_Value):
    """"Esta vai ser a função responsavel por realizar o metodo de ponto medio"""

    #Definir comprimento do intervalo
    h = (end_Point - start_Point)/steps

    #Criar usando numpy uma tabela de zeros de tamnaho steps por 2 colunas
    resultsTable = np.zeros((steps+1,2))

    #Define W0 e X0 (primeiro valor da tabela, como ponto inicial e valor inicial)
    resultsTable[0] = [start_Point,initial_Value]

    #Para toda linha da tabela
    for i in range(len(resultsTable)-1):
        
        #Lembre que Wi é o [i,1] e Xi é o [i,0]

        #Encontrar X(i+1)
        resultsTable[i+1,0] = resultsTable[i,0] + h

        #Encontrar W(i+1)
        resultsTable[i+1,1] = resultsTable[i,1] + h*((1/2)*EDO_Function(resultsTable[i,0],resultsTable[i,1]) + (1/2)*EDO_Function(resultsTable[i,0]+h,resultsTable[i,1]+h*EDO_Function(resultsTable[i,0],resultsTable[i,1])))
        
    
    return resultsTable

def exact_Solutions (EDO_ExactSol,start_Point,end_Point,steps):
    #Definir comprimento do intervalo
    h = (end_Point - start_Point)/steps
    curr_X = start_Point

    #Criar usando numpy uma tabela de zeros de tamnaho steps por 2 colunas
    resultsTable = np.zeros((steps+1,2))

    for i in range(len(resultsTable)):
        resultsTable[i] = [curr_X,EDO_ExactSol(curr_X)]
        curr_X = curr_X+h

    return resultsTable


#O "int main() " fica aqui

r_Euler = met_Euler(edo_Function,0,2,5,-2)
r_Pmedio = met_PMedio(edo_Function,0,2,5,-2)
r_EulerMelhor = met_EulerMelhorado(edo_Function,0,2,5,-2)
r_Exatos = exact_Solutions(edo_ExactSolution,0,2,5)

#Definir cabeçalho, passar a tabela para estrutura pandas e imprimir resultados

#Passa pra estrutura panda do seguinte modo: Define Xi como os Xi de Euler (são todos iguais) e depois coloca a segunda coluna de cada ja com o cabeçalho correto
r_Final = panda.DataFrame({
    'Xi': r_Euler[:,0].copy(),
    'Wi Exato': r_Exatos[:,1].copy(),
    'Wi Euler': r_Euler[:,1].copy(),
    'Wi PMedio': r_Pmedio[:,1].copy(),
    'Wi Euler Melhorado': r_EulerMelhor[:,1].copy()
})

r_Final.to_csv('ResultadosEuler.csv', encoding = 'utf-8', index=False)

#Graficos!
#Define que r_final sera plotado como linha
r_Final.plot(kind='line',title='Soluções e metodos',x='Xi')

##error_Calc(r_Final)

plot.savefig('Resultados.png')
plot.show()


