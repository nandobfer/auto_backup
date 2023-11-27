import subprocess, json, sys
from gdrive import upload

def delete(user):
    proc = subprocess.Popen([f"rm -rf {user}.tar.gz"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print("file deleted")

def newBackup(domain):
    print(f'compressing {domain}')
    proc = subprocess.Popen([f"cyberpanel createBackup --domainName {domain}"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    
    if out:
        timestamp = out.decode('utf-8').split('backup_log.')[1].replace("\n", "")
        path = f"/home/{domain}/backup/"
        filename = f"backup-{domain}-{timestamp}.tar.gz"

        print(f"backup file: {path}{filename}")

        print(f"compressed {domain} ")
        # proc = subprocess.Popen([f"mv /home/cpmove-{domain}.tar.gz {domain}.tar.gz"], stdout=subprocess.PIPE, shell=True)
        # (out, err) = proc.communicate()
        # print('uploading to drive')
        # upload(domain, 'tar.gz')
        # delete(domain)
        print()
        
    

domain = sys.argv[1]
newBackup(domain)