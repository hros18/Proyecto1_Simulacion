import random
import math
from person import Person
import collections


class Population:
    def __init__(self, H, M, Y = 100):
        self.hombres = []
        self.mujeres = []
        self.time = Y*12
        self.parejas = 0
        self.parejas = []
        self.hijos = collections.deque()
        for _ in range(0, H):
            self.hombres.append(Person(0, int(random.uniform(0,100))))
        
        for _ in range(0, M):
            self.mujeres.append(Person(1, int(random.uniform(0,100))))

    def eliminar_fallecidos(self):
        i = 0
        while(i < len(self.hombres)):
            if self.hombres[i].edad == self.hombres[i].death:
                self.hombres.remove(self.hombres[i])
            else:
                i += 1
        i = 0
        while( i < len(self.mujeres)):
            if self.mujeres[i].edad == self.mujeres[i].death:
                self.mujeres.remove(self.mujeres[i])
            else:
                i += 1 

    def emparejamiento(self):
        for w in self.mujeres:
            if w.soltero and w.desea_pareja and w.etapa_separacion == 0:
                for m in self.hombres:
                    if m.soltero and m.desea_pareja and m.etapa_separacion == 0:
                        diferencia_edad = int(abs(m.edad - w.edad)/12)
                        if diferencia_edad < 5:
                            if self.crea_pareja(m,w,0.45):
                                break
                            else:
                                continue
                        if diferencia_edad < 10:
                            if self.crea_pareja(m,w,0.4):
                                break
                            else:
                                continue
                        if diferencia_edad < 15:
                            if self.crea_pareja(m,w,0.35):
                                break
                            else:
                                continue
                        if diferencia_edad < 20:
                            if self.crea_pareja(m,w,0.25):
                                break
                            else:
                                continue
                        
                        self.crea_pareja(m,w,0.15)
    #pep Probabilidad de establecer pareja x diferencia de edad
    def crea_pareja(self, h, m, pep):
        p = random.random()
        if p < pep:
            self.parejas += 1
            #pb breaking probability
            pb = random.random()
            tiempo_vida_hombre = h.death - h.edad
            tiempo_vida_mujer = m.death - m.edad
            if pb < 0.2:
                t_relacion = random.randint(1, max(min(tiempo_vida_hombre,tiempo_vida_mujer),1))
                self.parejas.append([h,m,t_relacion,0])
            else:
                self.parejas.append([h,m,min(tiempo_vida_hombre,tiempo_vida_mujer),0])
            h.soltero = False
            m.soltero = False
            return True
        return False

    def eliminar_parejas(self):
        i = 0
        while ( i < len(self.parejas)):
            if self.parejas[i][2] == 0:
                self.parejas[i][0].soltero = True
                self.parejas[i][0].tiempo_de_espera()
                self.parejas[i][1].soltero = True
                self.parejas[i][1].tiempo_de_espera()
                self.parejas.remove(self.parejas[i])
                self.parejas -= 1
            else: 
                i += 1

    def avanzar(self):
        pass

    def hijos_x_embarazo(self):
        probs = [0.68, 0.86, 0.94, 0.98, 1]
        r = random.random()
        for i in range(5):
            if r < probs[i]:
                return i+1
    

    def concebimientos(self):
        ages = [12*12,15*12,21*12,35*12,45*12,60*12,125*12]
        for p in self.parejas:


    def nacimientos(self):
        pass
