import random
import math
from person import Person
import collections


class Population:
    def __init__(self, H, M, Y = 100):
        self.hombres = []
        self.mujeres = []
        self.time = Y*12
        self.cant_parejas = 0
        self.parejas = []
        self.embarazos = collections.deque()
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
            self.cant_parejas += 1
            #pb breaking probability
            pb = random.random()
            tiempo_vida_hombre = h.death - h.edad
            tiempo_vida_mujer = m.death - m.edad
            if pb < 0.2:
                t_relacion = random.randint(1, max(min(tiempo_vida_hombre,tiempo_vida_mujer),1))
                self.parejas.append([h,m,t_relacion])
            else:
                self.parejas.append([h,m,min(tiempo_vida_hombre,tiempo_vida_mujer)])
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
                self.cant_parejas -= 1
            else: 
                i += 1

    def avanzar(self):
        self.eliminar_fallecidos()
        c = 0
        #totales = 0
        while self.time != 0:
            for h in self.hombres:
                h.envejece()
                # if h.total_hijos > 0:
                #     totales += 1
            for m in self.mujeres:
                m.envejece()
                # if m.total_hijos > 0:
                #     totales += 1
            self.eliminar_fallecidos()
            self.nacimientos()
            self.eliminar_parejas()
            self.concebimientos()
            self.emparejamiento()

            if c % 12 == 0:
                print('Hombres : ' + str(len(self.hombres)))
                print('Mujeres : ' + str(len(self.mujeres)))
                print('Parejas : ' + str(len(self.parejas)))
                print('Embarazos : ' + str(len(self.embarazos)))
                #print('Totales : ' + str(totales))
                input()

            c += 1
            self.time -= 1

    def hijos_x_embarazo(self):
        probs = [0.68, 0.86, 0.94, 0.98, 1]
        r = random.random()
        for i in range(5):
            if r < probs[i]:
                return i+1
    

    def concebimientos(self):
        ages = [12*12,15*12,21*12,35*12,45*12,60*12,125*12]
        for h,m,_ in self.parejas:
            h_desea_hijo = (abs(h.total_hijos - h.cant_hijos) > 0)
            m_desea_hijo = (abs(m.total_hijos - m.cant_hijos) > 0)
            if h_desea_hijo and m_desea_hijo:
                r = random.random()
                if m.edad >= ages[0] and m.edad < ages[1] and m.death - m.edad > 9:
                    if r < 0.2:
                        h.cant_hijos += 1
                        m.cant_hijos += 1
                        self.embarazos.append([self.hijos_x_embarazo(), 9])
                    continue
                if m.edad < ages[2] and (m.death - m.edad) > 9:
                    if r < 0.45:
                        h.cant_hijos += 1
                        m.cant_hijos += 1
                        self.embarazos.append([self.hijos_x_embarazo(), 9])
                    continue
                if m.edad < ages[3] and (m.death - m.edad) > 9:
                    if r < 0.8:
                        h.cant_hijos += 1
                        m.cant_hijos += 1
                        self.embarazos.append([self.hijos_x_embarazo(), 9])
                    continue
                if m.edad < ages[4] and (m.death - m.edad) > 9:
                    if r < 0.4:
                        h.cant_hijos += 1
                        m.cant_hijos += 1
                        self.embarazos.append([self.hijos_x_embarazo(), 9])
                    continue
                if m.edad < ages[5] and (m.death - m.edad) > 9:
                    if r < 0.2:
                        h.cant_hijos += 1
                        m.cant_hijos += 1
                        self.embarazos.append([self.hijos_x_embarazo(), 9])
                    continue
                if m.edad < ages[6] and (m.death - m.edad) > 9:
                    if r < 0.05:
                        h.cant_hijos += 1
                        m.cant_hijos += 1
                        self.embarazos.append([self.hijos_x_embarazo(), 9])
                    continue
                

    def nacimientos(self):
        cant_bebes = 0
        while len(self.embarazos) != 0 and self.embarazos[0][1] == 0:
            cant_bebes += self.embarazos[0][0]
        for _ in range(cant_bebes):
            r = random.random()
            if r < 0.5:
                self.hombres.append(Person(0,0))
            else:
                self.mujeres.append(Person(1,0))
            
