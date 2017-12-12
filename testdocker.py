###################################
# Some docker env manipulations
###################################

import docker
client = docker.from_env()
client = docker.from_env()

def run_ctnr():
   client.create_container("ubuntu:latest", "echo hello world")
   #client.containers.run("ubuntu:latest", "echo hello world")
 
if __name__ == '__main__':
   run_ctnr()
