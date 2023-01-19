import subprocess, json, sys
from gdrive import upload

def delete(user):
    proc = subprocess.Popen([f"rm -rf {user}.tar.gz"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print("file deleted")

def newBackup(user):
    print(f'compressing {user}')
    proc = subprocess.Popen([f"/scripts/pkgacct {user}"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    
    if out:
        print(f"compressed {user} ")
        proc = subprocess.Popen([f"mv /home/cpmove-{user}.tar.gz {user}.tar.gz"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        print('uploading to drive')
        upload(user, 'tar.gz')
        delete(user)
        print()
        
    

user = sys.argv[1]
newBackup(user)