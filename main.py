class Proceso:
    def __init__(self, inicio, proceso, prioridad):
        self.t_inicio=inicio
        self.t_finaliza=999
        self.t_proceso=proceso
        self.prioridad=prioridad
        self.estado=[]
        pass
    pass
print "Cuantos procesos son:"
num_procesos = input()
procesos= []
cola=[]
#ingreso de datos
for x in range(num_procesos):
    print "Cual es el tiempo de entrada del proceso "+str((x+1))
    inicio = input()
    print "Cual es el tiempo de procesamiento del proceso "+str((x+1))
    proceso = input()
    print "Cual es la prioridad del proceso "+str((x+1))
    prioridad = input()
    print ""
    procesos.append(Proceso(inicio, proceso, prioridad))
    pass
#imprimir los datos
for x in range(num_procesos):
    print "Proceso "+str(x+1)
    print "Tiempo entrada: "+str(procesos[x].t_inicio)
    print "Tiempo procesamiento: "+str(procesos[x].t_proceso)
    print "Prioridad: "+str(procesos[x].prioridad)
    pass
    print ""
total=0
#tiempo de ejecucion total
for x in range(num_procesos):
    total= total+procesos[x].t_proceso
    pass
#inicio de algoritmo
for x in range(total):
    for y in range(num_procesos):
        if procesos[y].t_inicio==x:
            cola.append(procesos[y])
            if len(cola)>1:
                for z in range(len(cola)-1):
                    if(cola[z].prioridad>cola[z+1].prioridad):
                        aux = cola[z]
                        cola[z]=cola[z+1]
                        cola[z+1]=aux
                        pass
                    pass
                pass
        pass
    for y in range(num_procesos):
        if procesos[y] not in cola:
            procesos[y].estado.append(0)
            pass
        elif procesos[y]==cola[0]:
            procesos[y].estado.append(1)
            cola[0].t_proceso-=1
            if cola[0].t_proceso==0:
                cola.pop(0)
                procesos[y].t_finaliza=x+1
                pass
            pass
        elif (procesos[y] in cola) and (procesos[y] != cola[0]):
            procesos[y].estado.append(2)
            pass
    pass
"""
for x in range(total):
    print x
    for y in range(num_procesos):
        if procesos[y] in cola:
            procesos[y].estado.append(1)
            pass
        else:
            procesos[y].estado.append(0)
        pass
    for y in range(num_procesos):
        if procesos[y].t_inicio==x:
            cola.append(procesos[y])
            procesos[y].estado.append(0)
            if(len(cola)!=1):
                for z in range(len(cola)-1):
                    if(cola[z].prioridad>cola[z+1].prioridad):
                        aux = cola[z]
                        cola[z]=cola[z+1]
                        cola[z+1]=aux
                        pass
                pass
            pass
            if cola[0].t_inicio != x:
                pro = procesos.index(cola[0])
                cola[0].t_proceso -=1
                procesos[pro].estado.append(1)
                pass
            if cola[0].t_inicio ==0:
                pro=procesos.index(cola[0])
                cola.pop(0)
                procesos[pro].t_finaliza=x;
        pass
    pass
"""

#estado 0= no hace nada
#estado 1= ejecuta
#estado 2= espera

#impresion de datos
for x in range(num_procesos):
    print "Proceso "+str(x+1)
    print "Tiempo t_finaliza: "+str(procesos[x].t_finaliza)
    print "Tiempo procesamiento: "+str(procesos[x].t_proceso)
    print "Prioridad: "+str(procesos[x].prioridad)
    print procesos[x].estado
    pass
    print ""
