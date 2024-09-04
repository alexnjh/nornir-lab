from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from pprint import pprint as pprint
from nornir.core.task import Task, Result
from getpass import getpass

password = getpass()

nr = InitNornir(
    inventory={
        "transform_function": "load_credentials",
        "transform_function_options": {"password": password},
    }
)

print(nr.inventory.hosts)

result = nr.filter(name="nxos_a").run(
    task=netmiko_send_command,
    command_string="show ip route vrf management",
    use_textfsm=True,
)

print_result(result)

for i in result["nxos_a"]:
    for x in i.result:
        print(x)
