def first_function(func):
    def second_function():
        print("BEGINNING to EXECURE THE FUNCTION")
        func()
        print("THE END of FUNCTION")
    return second_function

def greeter():
    print("hello everyone, my name is ricko")

print(first_function(greeter))

greeter= first_function(greeter)
#Kamu bilang, "Hai Python, tolong bungkus fungsi greeter ini dengan first_function, lalu simpan hasilnya lagi di nama greeter."
greeter()

def bungkus():
    print("tolong bungkus kata ini")

bungkus = first_function(bungkus)
bungkus()