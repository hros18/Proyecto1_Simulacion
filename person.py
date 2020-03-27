import random
import math


class Person:
    def __init__(self, sexo, edad):
        self.sexo = sexo
        #edad en meses
        self.edad = edad
        #edad de muerte en meses
        self.death = self.Death()
        self.cant_hijos = 0
        self.total_hijos = 0
        self.soltero = True
        self.etapa_separacion = 0
        self.desea_pareja = False
        self.Desea_Pareja()


    def Death(self):
        # prob[0] - 0 --> 12 years
        # prob[1] - 13 --> 45 years
        # prob[2] - 46 --> 75 years
        # prob[3] - 76 --> 125 years
        # prob[4] - +125 years
        prob = [0] * 5
        ages = [0,12*12,45*12,76*12,125*12,125*12]
        top = 4
        if self.edad < ages[1]:
            prob[0] = 0.25
        if self.edad < ages[2]:
            prob[1] = 0.1 if self.sexo else 0.15
        if self.edad < ages[3]:
            prob[2] = 0.3 if self.sexo else 0.35
        if self.edad < ages[4]:
            prob[3]  = 0.7 if self.sexo else 0.65
        prob[-1] = 1
        
        for i in range(0, 5):
            r = random.random()
            if r < prob[i]:
                top = i + 1
                break
        return random.randint(max(self.edad, ages[top-1]), ages[top])
    

    def Desea_Pareja(self):
        r = random.random()
        ages = [12*12,15*12,21*12,35*12,45*12,60*12,125*12]
        solve = False
        if self.edad < ages[0]:
            solve = False
        if self.edad >= ages[0] and self.edad < ages[1]:
            solve = r < 0.6
        if self.edad >= ages[1] and self.edad < ages[2]:
            solve = r < 0.65
        if self.edad >= ages[2] and self.edad < ages[3]:
            solve = r < 0.8
        if self.edad >= ages[3] and self.edad < ages[4]:
            solve = r < 0.6
        if self.edad >= ages[4] and self.edad < ages[5]:
            solve = r < 0.5
        if self.edad >= ages[5] and self.edad < ages[6]:
            solve = r < 0.2
        
        self.desea_pareja = solve

    def tiempo_de_espera(self):
        t = random.random()
        l = 0
        ages = [12*12,15*12,21*12,35*12,45*12,60*12,125*12]
        if self.edad >= ages[0] and self.edad < ages[1]:
            l = 1/3
        if self.edad >= ages[1] and self.edad < ages[3]:
            l = 1/6
        if self.edad >= ages[3] and self.edad < ages[4]:
            l = 1/12
        if self.edad >= ages[4] and self.edad < ages[5]:
            l = 1/24
        if self.edad >= ages[5] and self.edad < ages[6]:
            l = 1/48
        
        self.etapa_separacion = math.ceil(math.log(t, math.e)) / (-1*l)
    
    def envejece(self):
        self.edad += 1
        ages = [12*12,15*12,21*12,35*12,45*12,60*12,125*12]
        if ages.__contains__(self.edad):
            self.Desea_Pareja()
            if self.etapa_separacion > 0:
                self.etapa_separacion -= 1
    
    def calcula_total_hijos(self):
        prob = [0, 0.6, 0.75,0.35,0.2,0.1,0.05]
        solve = True
        while solve:
            if self.total_hijos >= 5:
                if random.random() < prob[-1]:
                    self.total_hijos += 1
                    continue
            else:
                if random.random() < prob[self.total_hijos]:
                    self.total_hijos += 1
                    continue
            solve = False
