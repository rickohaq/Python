import yaml
from rich import print as rprint
from jinja2 import Environment,FileSystemLoader

def generate_config():
    """
    load vars from file 
    Generate config from template
    """
    
    my_vars = yaml.safe_load(open("group_vars/R1.yaml"))
    env = Environment(loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("bgp.j2")
    configuration = template.render(my_vars)
    print(configuration)

generate_config()

