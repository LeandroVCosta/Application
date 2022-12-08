from Class import Repositorio
from Class import Energy
from time import sleep
from Class import Connection as con
import psutil as ps

consumo = Energy.getWatt()

while True:
 usocpu = round(ps.cpu_percent(),2)/100
 plano = Repositorio.alterarEnergia()
 EnergiaW = round(consumo * usocpu + 10,2)
 print("Consumo de Energia Estimado:" + str(EnergiaW))
 con.inserir(EnergiaW,plano)
 sleep(30)
