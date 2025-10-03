import pyeapi
import os
import yaml

pyeapi.load_config('eapi.conf')

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

file = open('switches.yml', 'r')
yaml_dict = yaml.safe_load(file)

switches = yaml_dict['switches']

for switch in switches:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    path = directory+'/'+switch+'.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")