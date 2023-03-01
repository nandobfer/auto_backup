import subprocess, json, sys
from gdrive import download

def delete(user):
    proc = subprocess.Popen([f"rm -rf {user}.tar.gz"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print("file deleted")

def newBackup(user):
    print(f'restoring {user}')
    proc = subprocess.Popen([f"/scripts/restorepkg {user}.tar.gz"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    
    if out:
        print(out)
        
    

user = sys.argv[1]

download(user)