from boxsdk import JWTAuth
from boxsdk import Client

# read json configuration file
auth = JWTAuth.from_settings_file('config.json')

access_token = auth.authenticate_instance()

# initialize sdk client
client = Client(auth)
service_account = client.user().get()
print('Service Account user ID is {0}'.format(service_account.id))

#file name and path
file_name = 'FILE_NAME'
stream = open('PATH_TO_FILE', 'rb')

#box parameters
folder_id = '0'
user_id = '0' 
user = client.user(user_id)

#make the call
box_file = client.as_user(user).folder(folder_id).upload_stream(stream, file_name)
print('File "{0}" uploaded to Box with file ID {1}'.format(box_file.name, box_file.id))
