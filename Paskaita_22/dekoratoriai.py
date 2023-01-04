# def return_string(stringas):
#     return stringas
#
# def reverse(stringas):
#     return stringas[::-1]

# fu-ja fun-cijoje kai kvieciam ja nereikia ()
# def return_upper_string(text, func):
#     if type(text) != str:
#         return "input must be string tyep"
#     some_text=func(text)
#     return some_text.upper()
#
# print(return_upper_string("higher order function!", return_string))
# print(return_upper_string("higher order function!", reverse))


# def upper_decorator(func):
#     def wrapper(our_text):
#         if type(our_text) != str:
#             return "input must be string"
#         some_text =func(our_text)
#         return some_text.upper()
#     return  wrapper
#
# @upper_decorator
# def return_string(stringas):
#     return stringas
# @upper_decorator
# def reverse(stringas):
#     return stringas[::-1]
# print(return_string("higher order function!"))
# print(reverse("higher order function!"))


# from flask import Flask
# app = Flask(__name__)
# @app.route('/'):
# def hello_world():
#     return "Hello world"

# def jonas():
#     """Jonas eina namo"""
#     return "jonas"
# # Grazina dokumentacija
# print(jonas.__doc__)
# # Grazina f-jos pavadinima
# print(jonas.__name__)

from functools import wraps

def lyginis_nelyginis(funct):
    @wraps(funct)
    def wrapper(*args):
        '''
        :param args:
        :return:
        '''
        result = funct(*args)
        if result%2 !=0:
            return result, "nelyginis"
        return result, "lyginis"
    return wrapper

@lyginis_nelyginis
def give_me_10():
    """Grazina skaiciu 10"""
    return 10

@lyginis_nelyginis
def multiply(x, y):
    return x + y

@lyginis_nelyginis
def sum_all(*args):
    return sum(args)

print(give_me_10())
print(multiply(5,2))
print(sum_all(5,5,89,6))


print(give_me_10.__doc__)
print(give_me_10.__name__)


# dekoratorius su paramentrais
from time import sleep
def uzvelavimas(laikas):
    def uzvelavimas2(funct):
        def wrapper(*args):
            sleep(laikas)
            print(f"Funkcija buvo atideta {laikas} sekundes")
            return funct(*args)
        return wrapper
    return uzvelavimas2

@uzvelavimas(1)
def for_sukimas(kartai):
    for x in range(kartai):
        print(x, " ", end="")
    print()

for_sukimas(10)

def args_counter(fn):
    def wrapper(*args):
        print(f"Argumentu sk.: {len(args)}")
        return fn(*args)
    return wrapper

@args_counter
def sumavimas(*args):
    print(f"Suma {sum(args)}")

sumavimas(1,2,3,4,5,6)

