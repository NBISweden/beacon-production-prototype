from beacon.request.parameters import RequestParams
from beacon.response.schemas import DefaultSchemas
import yaml
from beacon.connections.mongo.__init__ import client
from bson.json_util import dumps
from typing import Optional
from beacon.connections.mongo.utils import get_docs_by_response_type
import subprocess
from beacon.logs.logs import LOG
import paramiko

host = 'beaconcli'
username = 'root'
password = 'hola'

def create_ssh(host=host, username=username, password=password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    try:
       LOG.debug("creating connection")
       ssh.connect(host, username=username, password=password)
       LOG.debug("connected")
       yield ssh
    finally:
       LOG.debug("closing connection")
       ssh.close()
       LOG.debug("closed")

def get_variants(entry_id: Optional[str], qparams: RequestParams, dataset: str):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command('cd /CLItest && python3 main.py -rg 37 -c 1 -p 1 --range 1000000000 --public')
    try:
        bash = stdout.read()
    except subprocess.CalledProcessError as e:
        output = e.output
        LOG.debug(output)
    bash_list = bash.split(b'\n')

    new_bash_list=[]
    for item in bash_list:
        item = item.decode("utf-8") 
        item = item.replace('[', '')
        item = item.replace(']', '')
        item = item.replace('(', '')
        item = item.replace(')', '')
        item = item.replace(' ', '')
        item = item.replace("'", '')
        item = item.replace('"', '')
        item_list = item.split(',')
        boolean = item_list[0]
        count = int(item_list[1])
        dataset_count=count
        end = len(item_list)
        #datasets_list = item_list[2:end]

        break
    docs={}
    schema = DefaultSchemas.GENOMICVARIATIONS

    return schema, count, dataset_count, docs, dataset