import subprocess, json, sys
from gdrive import upload

def delete(filepath):
    proc = subprocess.Popen([f"rm -rf {filepath}"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err:
        print('erro ao deletar')
        print(err)
    else:
        print("tar.gz file deleted")


    proc = subprocess.Popen([f"rm -rf {filepath.split('.tar')[0]}"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if err:
        print(err)
    else:
        print('backup dir deleted')


def newBackup(domain):
    print(f'compressing {domain}')
    proc = subprocess.Popen([f"cyberpanel createBackup --domainName {domain}"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    
    if out:
        timestamp = out.decode('utf-8').split('backup_log.')[1].replace("\n", "")
        path = f"/home/{domain}/backup/"
        filename = f"backup-{domain}-{timestamp}.tar.gz"
        filepath = f"{path}{filename}"

        print(f"backup file: {filepath}")

        print(f"compressed {domain} ")
        # proc = subprocess.Popen([f"mv /home/cpmove-{domain}.tar.gz {domain}.tar.gz"], stdout=subprocess.PIPE, shell=True)
        # (out, err) = proc.communicate()
        print('uploading to drive')
        upload(filepath, f"{domain}.tar.gz")
        delete(filepath)
        print()
        
    

if __name__ == "__main__":
    domain = sys.argv[1]
    newBackup(domain)