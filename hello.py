from flask import Flask
from functools import wraps
import random
app = Flask(__name__)
print(__name__)
print(random.__name__)
def make_bold(func,*args,**kwargs):
    @wraps(func)
    def wrapper_function(*args,**kwargs):
        store=func(*args,**kwargs)
        return f"<b>{store}</b>"
    return wrapper_function

def make_italic(func):
    @wraps(func)
    def wrapper_func():
        store=func()
        return f"<em>{store}</em>"
    return wrapper_func

def make_underline(func):
    @wraps(func)
    def wrapper_func():
        store=func()
        return f"<u>{store}</u>"
    return wrapper_func

@app.route("/")

def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p> this is a pargraph</p>"
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGt1aTYxbWRxZHYxbnBpaDFpbXk0ZGhmdzV4Y3JjczI1aTFnOXRyZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ihQVlz99wLj0BSYVCZ/giphy.gif'>")

@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "bye"



@app.route("/on")
@make_bold
@make_italic
@make_underline
def on():
    return "<a href=www.gandu.com'> chotu </a>"

@app.route("/<path:name>")
def greet(name):
    return f"hello there {name +"12"}!"



if __name__=="__main__":
# auto reload the server and using the flask debugger
    app.run(debug=True)

#advanced python decorators

class User:
    def __init__(self,name):
        self.name=name
        self.is_logged_in=False


def is_authenticated_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in==True:
            function(args[0])
    return wrapper


#we have to create an authenticator to know whether logged in or not
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name} here,creating a new blog")

new_user=User("Aditya")
new_user.is_logged_in=True
create_blog_post(new_user)







