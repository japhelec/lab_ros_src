from threading import Timer

def hello():
    print("hello, world")

t = Timer(10.0, hello)
t.start()