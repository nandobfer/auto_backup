from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()   
gauth.LocalWebserverAuth()    
drive = GoogleDrive(gauth)  

# upload_file = 'teste.txt'
# gfile = drive.CreateFile({'parents': [{'id': '1pzschX3uMbxU0lB5WZ6IlEEeAUE8MZ-t'}]})
# # Read file and set it as the content of this instance.
# gfile.SetContentFile(upload_file)
# gfile.Upload() # Upload the file.

file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1cIMiqUDUNldxO6Nl-KVuS9SV-cWi9WLi')}).GetList()
for file in file_list:
	print('title: %s, id: %s' % (file['title'], file['id']))