from person import Person
from population import Population

if __name__ == '__main__':
    print('Escriba tres enteros separados por espacio con el siguiente formato:')
    print('H M Y')
    print('H: cantidad inicial de hombres en la poblacion')
    print('M: cantidad inicial de mujeres en la poblacion')
    print('Y: cantidad de años para realizar la simulacion')
    print('Presione enter para que transcurra un año')
    line = input().split(' ')
    h = int(line[0])
    m = int(line[1])
    y = int(line[2])

    p = Population(h,m,y)

    p.avanzar()

