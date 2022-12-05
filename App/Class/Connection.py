import pyodbc

server = 'trackvisiondb.database.windows.net'
database = 'trackvisiondb'
username = 'CloudSA49c766d4'
password = 'Urubu1004'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER=' + driver + ';'
                    'SERVER=tcp:' + server + ';'
                    'PORT=1433;'
                    'DATABASE=' + database + ';'
                    'UID=' + username + ';'
                    'PWD=' + password)

cursor = conn.cursor()

def inserir(consumo,plano):
    syntax = "DECLARE @Date DATETIME; SET @Date = GETDATE(); insert into dadoEnergia (fkCaixa,consumo,plano,momento) values (1,?,?,@Date)"
    values = [consumo,plano]
    cursor.execute(syntax,values)
    conn.commit()

def getFluxo():
    syntax = "select top 10 avg(cpuPorcentagem) from Leitura"
    cursor.execute(syntax)
    rows = cursor.fetchone()
    return int(rows[0])


