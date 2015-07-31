import json
import os
import time
from httplib2 import Http


os.system("sudo docker build -t private-repository:31000/flask src")
os.system("sudo docker push private-repository:31000/flask")



