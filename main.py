from person import Person
from population import Population

if __name__ == '__main__'
    line = input().split(' ')
    h = int(line[0])
    m = int(line[1])
    y = int(line[2])

    p = Population(h,m,y)

    p.avanzar()

