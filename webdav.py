import easywebdav
import requests
user='test'
pw='boobs'
webdav = easywebdav.connect('h711.webhop.me',
                            username=user,
                            password=pw,
                            path="remote.php/webdav",
                            protocol='https',
                            verify_ssl='./h711.webhop.me.pem'
                            )
# Do some stuff:
print webdav.ls("iTunes")
