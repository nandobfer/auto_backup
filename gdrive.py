from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from datetime import datetime
import sys

def download(user):
    def getUserFile(backup_list):
        for file in backup_list:
            if file['title'].split('.tar')[0] == user:
                return file

    folder_id = '12URAbEpT-96N1XOH9Vaco9cOJwu9aTyL'

    str = "\'" + folder_id + "\'" + " in parents and trashed=false"
    file_list = drive.ListFile({'q': str}).GetList()[0]


    backup_str = "\'" + file_list['id'] + "\'" + " in parents and trashed=false"
    backup_list = drive.ListFile({'q': backup_str}).GetList()
    
    file = getUserFile(backup_list)
    print(f"downloading {file['title']}")
    
    file.GetContentFile(file['title'])


    

def upload(filepath: str, filename: str):
    parent_folder = '12URAbEpT-96N1XOH9Vaco9cOJwu9aTyL'
    today = str(datetime.now().date())


    folder = drive.ListFile({'q': f"title = '{today}' and trashed=false"}).GetList()
    if not folder:
        folder = drive.CreateFile({
            'title': today,
            'parents': [{'id': parent_folder}],
            'mimeType': 'application/vnd.google-apps.folder'
            })
        folder.Upload()
        print(f"folder id: {folder['id']}")
        
    else:
        folder = folder[0]

    file = drive.CreateFile({'title': filename, 'parents': [{'id': folder['id']}]})
    file.SetContentFile(filepath)
    file.Upload()
    print(f"uploaded {filepath}")

gauth = GoogleAuth()   

# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")

if gauth.credentials is None:
    # Authenticate if they're not there

    # This is what solved the issues:
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})

    gauth.LocalWebserverAuth()

elif gauth.access_token_expired:

    # Refresh them if expired

    gauth.Refresh()
else:

    # Initialize the saved creds

    gauth.Authorize()

# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")  

drive = GoogleDrive(gauth)

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])