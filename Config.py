from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
from jnpr.junos.exception import *

junos_hosts = ["172.25.11.1", "1.1.1.1"]
for ip in junos_hosts:
    try:
     dev = Device(host=ip, user="lab", password="lab123")
     dev.open()
     config = Config(dev)
     config.lock()
     config.load(path="add_snmp.conf", merge=True)
     config.pdiff()
     config.commit()
     config.unlock()
     dev.close()
  except ConnectTimeoutError as e:
    print("Connnection time out!")