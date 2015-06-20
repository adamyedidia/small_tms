def hi(hello, x):
    return hello(x)
    
def square(x):
    return x**2

print hi(square, 5)