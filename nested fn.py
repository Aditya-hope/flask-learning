# def outer():
#     print("I am outer")
#     def inner():
#         print("I am inner")
#     return inner
# msg=outer()
# msg()
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")

say_hello()

def say_bye():
    print("bye")

decorated_msg=delay_decorator(say_bye)
decorated_msg()