
class Proceso:
    def __init__(self, inicio, proceso, prioridad):
        self.t_inicio=inicio
        self.t_finaliza=999
        self.t_proceso=proceso
        self.tproceso=proceso
        self.prioridad=prioridad
        self.estado=[]
        self.T=999
        self.W=999
        self.P=999
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
for x in range(total+1):

    for y in range(num_procesos):
        if procesos[y] not in cola:
            procesos[y].estado.append(0)
            pass
        elif procesos[y]==cola[0] and procesos[y].t_inicio!=x:
            procesos[y].estado.append(1)
            cola[0].t_proceso-=1
        elif (procesos[y] in cola) and (procesos[y] != cola[0]):
            procesos[y].estado.append(2)
            pass
    pass
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
    if cola:
        if cola[0].t_proceso==0:
            lugar= procesos.index(cola[0])
            procesos[lugar].t_finaliza=x
            cola.pop(0)
            pass
        pass

#estado 0= no hace nada
#estado 1= ejecuta
#estado 2= espera

#impresion de datos
for x in range(num_procesos):
    print "Proceso "+str(x+1)
    print "Tiempo t_finaliza: "+str(procesos[x].t_finaliza)
    print "Tiempo procesamiento: "+str(procesos[x].tproceso)
    print "Prioridad: "+str(procesos[x].prioridad)
    print procesos[x].estado
    pass
    print ""


#imprime diagrama
for x in range(num_procesos):
    print procesos[x].estado
    pass

print ""
#imprime tabla
t=0
w=0
p=0
print "Proceso\tT_llegada\tt\tT_finaliza\tT\tW\tP"
for x in range(num_procesos):
    procesos[x].T=procesos[x].t_finaliza-procesos[x].t_inicio
    procesos[x].W=procesos[x].T-procesos[x].tproceso
    procesos[x].P=float(procesos[x].T)/float(procesos[x].tproceso)
    print str(x+1)+"\t   "+str(procesos[x].t_inicio)+"\t\t"+str(procesos[x].tproceso)+"\t   "+str(procesos[x].t_finaliza)+"\t\t"+str(procesos[x].T)+"\t"+str(procesos[x].W)+"\t"+str(procesos[x].P)
    t+=procesos[x].T
    w+=procesos[x].W
    p+=procesos[x].P
    pass

print "Promedio de T "+ str(float(t)/float(num_procesos))
print "Promedio de W "+str(float(w)/float(num_procesos))
print "Promedio de P "+str(float(p)/float(num_procesos))
