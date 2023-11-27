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
        print(f"compressed {domain} ")
        # proc = subprocess.Popen([f"mv /home/cpmove-{domain}.tar.gz {domain}.tar.gz"], stdout=subprocess.PIPE, shell=True)
        # (out, err) = proc.communicate()
        print("out:")
        print(out)
        # print('uploading to drive')
        # upload(domain, 'tar.gz')
        # delete(domain)
        print()
        
    

domain = sys.argv[1]
newBackup(domain)