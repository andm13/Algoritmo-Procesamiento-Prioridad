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
    print "Cual es la prioridad del proceso "+str((x+1))+"\n"
    prioridad = input()
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
for x in range(num_procesos):
    total= total+procesos[x].t_proceso
    pass
#inicio de algoritmo
for x in range(total):
    print x
    for y in range(num_procesos)
        if procesos[y] in cola:

        else
            procesos[y].estado.append(0)
            pass
        pass
    for y in range(num_procesos):
        if procesos[y].t_inicio==x:
            cola.append(procesos[y])
            t.append("/")
            pass
        pass
        for z in range(len(cola)):

            pass
    pass
