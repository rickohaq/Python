from rich import print as rprint

def politeness(func):
    # def wrapper(): # TypeError: politeness.<locals>.wrapper() takes 0 positional arguments but 1 was given
    def wrapper(*args, **kwargs):  
        rprint("[green]Hi, thank you for using this code for learning[/green]")
        func(*args, **kwargs)
        rprint("[yellow]i Hope you can understand my code[/yellow]")
    return wrapper

@politeness
def nameprinter(name):
    print(f"Your name is {name}")

nameprinter("ricko")

@politeness
def tambah(a,b):
    print(a+b)

tambah(4,5)