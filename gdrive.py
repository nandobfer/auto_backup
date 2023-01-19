from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime

def upload(user, extension):
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
    file.SetContentFile(f"{user}.{extension}")
    file.Upload()
    print(f"uploaded {user}.{extension}")

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

