def doubler(func):
    def inner():
        func()
        func()
    return inner

@doubler
def dtcjaya():
    print("Datacomm jaya jaya jaya")

dtcjaya()