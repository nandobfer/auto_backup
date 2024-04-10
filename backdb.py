import subprocess, json, sys
import mysql.connector
from gdrive import upload

# pip3 install mysql-connector-python

def delete(filepath):
    proc = subprocess.Popen([f"rm -rf {filepath}"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print("file deleted")

def newBackup(database):
    filepath = f'/root/db_backup/{database}.sql'
    proc = subprocess.Popen([f"mysqldump -u boz -pEwhblt69!@# {database} > {filepath}"], stdout=subprocess.PIPE, shell=True)
    print()
    (out, err) = proc.communicate()

    if out:
        print(f"exported {database} ")
        print('uploading to drive')
        upload(filepath, f'{database}.sql')
        delete(filepath)
    
    if err:
        print('error exporting database:')
        print(err)

def main():
    conn = mysql.connector.connect (user='boz', password='Ewhblt69!@#',
                                host='agenciaboz.com.br',buffered=True)
    cursor = conn.cursor()
    databases = ("show databases")
    cursor.execute(databases)
    for (databases) in cursor:
        print(databases[0])
        newBackup(databases[0])

if __name__ == "__main__":
    main()

        
    