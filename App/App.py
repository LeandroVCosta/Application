from Class import Repositorio
from Class import Energy
from time import sleep
from Class import Connection as con

while True:
 consumo = Energy.getWatt()
 plano = Repositorio.alterarEnergia()
 con.inserir(consumo,plano)
 sleep(30)
