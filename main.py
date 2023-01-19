import subprocess, json, sys
from datetime import datetime
from gdrive import drive

def upload(user):
    parent_folder = '12URAbEpT-96N1XOH9Vaco9cOJwu9aTyL'
    today = str(datetime.now().date())
    print(today)

    file_metadata = {
    'title': today,
    'parents': [{'id': parent_folder}],
    'mimeType': 'application/vnd.google-apps.folder'
    }

    folder = drive.ListFile({'q': f"title = '{today}' and trashed=false"}).GetList()
    if not folder:

        folder = drive.CreateFile(file_metadata)
        folder.Upload()
        print(f"folder id: {folder['id']}")
        
    else:
        folder = folder[0]

    file = drive.CreateFile({'parents': [{'id': folder['id']}],})
    file.SetContentFile(f"{user}.tar.gz")
    file.Upload()
    print(f"uploaded {user}.tar.gz")

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