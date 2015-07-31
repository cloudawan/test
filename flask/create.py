import json
import os
import time
from httplib2 import Http


# create a replication controller to replicate nodes
os.system("kubectl create -f flask-controller.json")


# create a service 
os.system("kubectl create -f flask-service.json")


