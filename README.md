# box-python-sdk-large-file-upload
A simple python 3 script to upload large files to Box.com using the box sdk for python.

# installing the sdk
`pip install boxsdk`

#install jwt
`pip install "boxsdk[jwt]"`

# obtaining the configuration file from box developers
1. create an app on https://app.box.com/developers/console
2. add or generate a public/provate key pair
3. download the json from the app settings section

# edit upload.py
edit this file to suite your requirements, ensuring the user id and folder id is correct.

# execute upload.py
`pyhton3 upload.py`

Read more on Box developers https://developer.box.com/