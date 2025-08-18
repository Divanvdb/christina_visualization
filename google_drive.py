from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Opens browser for authentication

drive = GoogleDrive(gauth)

# List files in a folder by folder ID
folder_id = 'YOUR_FOLDER_ID'
file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

for file in file_list:
    print(f"Title: {file['title']}, ID: {file['id']}")
