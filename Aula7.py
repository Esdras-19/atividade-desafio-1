from moda import moda
from media import media
from mediana import mediana
from desvio import desvio



empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]
empresa5 = [1400,1750,2000,4500,5900]





print('Escolha uma das empresas abaixo para exibir os dados: ')

print(f'''
      
1-Empresa 1 
2-Empresa 2 
3-Empresa 3 
4-Empresa 4 
5-Empresa 5 

''')

escolha=int(input('>>'))

def analise():

 if escolha ==1:
    print('Salários:',empresa1)
    moda(empresa1)
    media(empresa1)
    mediana(empresa1)
    desvio(empresa1)

 elif escolha ==2:
    print('Salários:',empresa2)
    moda(empresa2)
    media(empresa2)
    mediana(empresa2)
    desvio(empresa2)

 elif escolha ==3:
    print('Salários:',empresa3)
    moda(empresa3)
    media(empresa3)
    mediana(empresa3)
    desvio(empresa3)

 elif escolha ==4:
    print('Salários:',empresa4)
    moda(empresa4)
    media(empresa4)
    mediana(empresa4)
    desvio(empresa4)

 elif escolha ==5:
    print('Salários:',empresa5)
    moda(empresa5)
    media(empresa5)
    mediana(empresa5)
    desvio(empresa5)

analise()

# Justifique sua escolha: entre as três empresas apresentadas, a mais adequada analisando os salários é a empresa 2, pois apresenta 
# uma das maiores médias dos salários  em comparação as demais empresas, além de possuir um teto salárial maior que as das demais. 
