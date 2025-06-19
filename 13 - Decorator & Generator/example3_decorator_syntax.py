from rich import print as rprint

def prettify(func):
    def wrapper():
        rprint("[cyan]******************************************[cyan]")
        func()
        rprint("[cyan]******************************************[cyan]")
    return wrapper

@prettify # @ symbol adalah decorator syntax jadi tidak perlu banner = prettify(banner)
def banner ():
    print("DO NOT ACCESS UNLESS AUTHORIZED")

# banner = prettify(banner)
banner()


