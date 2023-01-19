import subprocess, json, sys
from gdrive import upload

def newBackup(user):
    proc = subprocess.Popen([f"/scripts/pkgacct {user}"], stdout=subprocess.PIPE, shell=True)
    print()
    (out, err) = proc.communicate()
    
    if out:
        print(f"successfully compressed {user} ")
        proc = subprocess.Popen([f"mv /home/cpmove-{user}.tar.gz {user}.tar.gz"], stdout=subprocess.PIPE, shell=True)
        print()
        (out, err) = proc.communicate()
        upload(user)
        
    

user = sys.argv[1]
newBackup(user)