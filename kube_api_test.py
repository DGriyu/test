#!/usr/bin/env python
from flask import Flask
#Not sure what this does, but probably imortant to Flask
app = Flask(__name__)
import os
import kubernetes


#main route
@app.route("/")
def hello():
	#returns the function access as an http dump
    return "hello Korymbus"#access()

def access():
	#configure whatever kubernetes cluster is in the local environment
	kubernetes.config.load_kube_config(os.path.join(os.environ["HOME"], '.kube/config'))
	#default info, may need to change in the future.
	v1 = kubernetes.client.CoreV1Api()
	pod_list = v1.list_namespaced_pod("default")
	pod_data = []

	#grabs only the vital data from the metadata
	for pod in pod_list.items:

		pod_meta = ("%s\t%s\t%s")%(pod.metadata.name, 
	                          pod.status.phase,
	                          pod.status.pod_ip)
		pod_data.append(pod_meta)

	#Better for readability
	return " ".join(str(x) for x in pod_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
#print(access())
