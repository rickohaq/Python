import yaml
from rich import print as rprint
def pull_yaml():
    """ this is function to pull yaml into python"""
    # config_data = yaml.safe_load(open("/group_vars/R1.yaml"))
    config_data = yaml.safe_load(open("group_vars/R1.yaml"))

    rprint(config_data)
    
    asn = config_data["BGP"]["ASN"]
    print(f"router bgp {asn}")
    
    peers_list = config_data["BGP"]["peers"]
    rprint(peers_list)
    for peer in peers_list:
        print(f"neighbor {peer['neighbor']} remote-as {peer['peer_asn']}")
        # atau
    
    
pull_yaml()