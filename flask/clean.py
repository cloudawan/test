import os
import subprocess



os.system("kubectl delete -f flask-controller.json")
os.system("kubectl delete -f flask-service.json")



p = subprocess.Popen(['kubectl', 'get', 'pod'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate()
output_line_list = output.split("\n")
for output_line in output_line_list:
    if output_line.startswith("flask"):
        os.system("kubectl delete pod " + output_line.split(" ")[0])

