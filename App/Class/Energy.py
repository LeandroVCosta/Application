import sys, os
import wmi
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import psutil as ps
import time

def getTDP():
    # Pego o nome do processador para utiizar no crawler
    comando = "wmic cpu get name"
    resposta = os.popen(comando).read().split("\n")[2].replace("(R)","").replace("(TM)","").replace("CPU","").replace("Intel","").replace("R","")
    resposta = resposta.split(" ")
    processador = str(resposta[0] + " " + resposta[1] + " " + resposta[2] + " "+ resposta[3])
    #Definição de Variáveis do Crawler e Tratamento do Dado
    
    driver = webdriver.Chrome()
    time.sleep(5)
    driver.get("https://www.techpowerup.com/cpu-specs/")
    time.sleep(5)
    driver.find_element(By.ID,'quicksearch').send_keys(processador)
    time.sleep(5)
    content = driver.page_source
    soup = BeautifulSoup(content,'html.parser')
    try:
     resultado = soup.findAll('tbody')[2].findNext('tr').findAll('td')[7]
     resultado = str(resultado).replace("<td>","").replace("</td>","").replace("W","")
    except:
     print("Erro Processador não encontrado..., tente trocar a posição dos vetores de acordo com o seu processador na váriavel processador dentro da classe Energy")
     return
    #Transformado em INT
    consumo = int(resultado)
    return consumo

def listarPlano():
    comando = "powercfg /L"
    resposta = os.popen(comando).read().split("\n")
    return resposta

def alterarPlano(GUID):
    comando = "powercfg /S "
    resposta = os.popen(comando + GUID).read()
    if(resposta == ""):
        return "Plano de Energia foi trocado com sucesso!"
    return "Houve um problema ao trocar o plano"

def getWatt():
     consumo = 0
     w = wmi.WMI(namespace="root\OpenHardwareMonitor")
     voltage_infos = w.Sensor()
     for sensor in voltage_infos:
        if sensor.SensorType == u"Power":
            if sensor.Name == "CPU Package":
                wattCPU = round(sensor.Value,2)
                consumo += wattCPU * 1.10
            if sensor.Name == "GPU Total":
                wattGPU = round(sensor.Value,2)
                consumo += wattGPU
     if consumo == 0:
         consumo = getTDP()
     return consumo
