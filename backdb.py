import subprocess, json, sys
import mysql.connector
from gdrive import upload

def newBackup(database):
    proc = subprocess.Popen([f"mysqldump -u fernando -pmfux6xpj {database} > {database}.sql"], stdout=subprocess.PIPE, shell=True)
    print()
    (out, err) = proc.communicate()
    
    print(f"exported {database} ")
    print('uploading to drive')
    upload(database, 'sql')
        
conn = mysql.connector.connect (user='fernando', password='mfux6xpj',
                               host='agenciaboz.com.br',buffered=True)
cursor = conn.cursor()
databases = ("show databases")
cursor.execute(databases)
for (databases) in cursor:
    print(databases[0])
    newBackup(databases[0])

        
    