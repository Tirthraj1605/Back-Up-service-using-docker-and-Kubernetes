# import os
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.http import MediaFileUpload

# # Define scopes and other constants
# SCOPES = ['https://www.googleapis.com/auth/drive']
# # CLIENT_SECRET_FILE = 'your credential json'  # Path to your downloaded credentials file
# CLIENT_SECRET_FILE = 'C:\Users\tirthraj bhalodiya\Desktop\Programing Language\Github_Projects\Project-5\Archive\app\credentials.json'  # Path to your downloaded credentials file
# API_NAME = 'drive'
# API_VERSION = 'v3'
# DIRECTORY_TO_WATCH = './ur dir wehre u r uploading files'

# def authenticate():
#     creds = None
#     if os.path.exists('./token.json'):
#         print('Token exists')
#         creds = Credentials.from_authorized_user_file('./token.json')
#     if not creds or not creds.valid:
#         print('Token doesnt exist')
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())
#     return creds

# # Function to upload file to Google Drive
# def upload_to_drive(folder_id):
#     creds = authenticate()
#     service = build('drive', 'v3', credentials=creds)
    
#     drive_files = get_filenames_from_folder(folder_id)


#     print('hi')
#     for root,dirs,files in os.walk(DIRECTORY_TO_WATCH):
#         print('hi for')
#         print(files)
#         for file_name in files:
#             if file_name not in drive_files:
#                 file_metadata = {'name': file_name,'parents':[folder_id]}
#                 file_path = DIRECTORY_TO_WATCH+'/'+file_name
#                 print(file_path)
#                 media = MediaFileUpload(file_path, resumable=True)
#                 file = service.files().create(body=file_metadata,media_body=media,fields='id').execute()
#                 print('File uploaded: %s' % file.get('id'))
#             else:
#                 print('file already present')

# def get_filenames_from_folder(folder_id):
#     creds = authenticate()
#     service = build('drive', 'v3', credentials=creds)

#     # List files in the folder
#     results = service.files().list(q=f"'{folder_id}' in parents",
#                                    fields='files(name)').execute()
    
#     # Extract filenames from the results
#     filenames = [file['name'] for file in results.get('files', [])]
#     print(set(filenames))
#     return set(filenames)


# # Main function to start monitoring the directory
# def main():
#     # folder_id = 'your folder id of drive folder check url of drive folder to get folder id'
#     folder_id = 'https://drive.google.com/drive/folders/1G40rU4dzS1W7cy7XYOi1q-G1eD4RrWAU'
#     # while True:
#     #     pass
#     upload_to_drive(folder_id)

# if __name__ == "_main_":
#     main()









from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# Load OAuth 2.0 credentials from the credentials JSON file
flow = InstalledAppFlow.from_client_secrets_file(
    r'C:\Users\urvas\OneDrive - PESUNIVERSITY\Sem 6\CC-Project\client_secret_958244684000-nc48rg2kop8mvlqutt99iep3lm8s4nk2.apps.googleusercontent.com.json',
    scopes=['https://www.googleapis.com/auth/drive']
)
credentials = flow.run_local_server()

with open( r'C:\Users\urvas\OneDrive - PESUNIVERSITY\Sem 6\CC-Project\credentials.json', 'w') as credentials_file:
    credentials_file.write(credentials.to_json())

# Interaction
from googleapiclient.discovery import build
credentials = Credentials.from_authorized_user_file(r'C:\Users\urvas\OneDrive - PESUNIVERSITY\Sem 6\CC-Project\credentials.json')
service = build('drive', 'v3', credentials=credentials)
results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
items = results.get('files', [])
if not items:
    print('No files found.')
else:
    print('Files:')
    for item in items:
        print(f'{item["name"]} ({item["id"]})')
