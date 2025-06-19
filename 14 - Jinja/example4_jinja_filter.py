import yaml
from rich import print as rprint
from jinja2 import Environment,FileSystemLoader

def generate_config():
    
    
    my_vars = yaml.safe_load(open("group_vars/R1.yaml"))
    env = Environment(loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("snmp.j2")
    configuration = template.render(my_vars)
    print(configuration)

generate_config()




# | Filter    | Purpose                | Example       | Output                  |                   |
# | --------- | ---------------------- | ------------- | ----------------------- | ----------------- |
# | `upper`   | Uppercase a string     | \`{{ hostname | upper }}\`              | `R1`              |
# | `lower`   | Lowercase a string     | \`{{ hostname | lower }}\`              | `r1`              |
# | `replace` | Replace text           | \`{{ desc     | replace(" ", "\_") }}\` | `uplink_to_core`  |
# | `int`     | Convert to integer     | \`{{ "10"     | int }}\`                | `10`              |
# | `default` | Provide fallback value | \`{{ ip       | default('0.0.0.0') }}\` | `0.0.0.0`         |
# | `join`    | Join list into string  | \`{{ vlans    | join(',') }}\`          | `10,20,30`        |
# | `length`  | Get list length        | \`{{ vlans    | length }}\`             | `3`               |
# | `list`    | Convert string to list | \`{{ "abc"    | list }}\`               | `['a', 'b', 'c']` |


