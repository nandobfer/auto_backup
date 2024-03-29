import subprocess, os, sys
from gdrive import download

def delete(user):
    proc = subprocess.Popen([f"rm -rf {user}.tar.gz"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print("backup file deleted")

def load(user):
    print(f'restoring {user}')
    os.system(f"cyberpanel restoreBackup --fileName ./{user}.tar.gz")
        
    

user = sys.argv[1]

download(user)
load(user)
delete(user)