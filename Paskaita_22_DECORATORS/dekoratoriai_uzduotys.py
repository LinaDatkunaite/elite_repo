# 1. Parašykite dekoratorių kuris riboja parametrų kiekį (tarkime, ne daugiau negu 2 parametrai funkcijai)

def args_counter(fn):
    def wrapper(*args):
        if len(args)>2:
            print("Too many parameters! Function take not more than 2")
        else:
            return fn(*args)
    return wrapper

@args_counter
def sumavimas(*args):
    print(f"Suma {sum(args)}")

sumavimas(1,2,6,9)
sumavimas(3,6)


# 2 Parašykite dekoratorių, kuris atideda funkcijos vykdymą 3s

from time import sleep
def delay(seconds):
    def delay2(func):
        def wrapper(*args):
            sleep(seconds)
            print(f"Function performance was delayed by {seconds} seconds")
            return f"Finally the result is: {func(*args)}"
        return wrapper
    return delay2

@delay(2)
def sum_count(*args):
    return sum(args)

print(sum_count(6,8,10))


# Parašykite dekoratorių, kuris leidžia į funkciją įrašyti tik string tipo parametrus.


# def string_format(func):
#     def wrapper(*args):
#         for i in args:
#             if type(i) != str:
#                 print("Only strings are taken as inputs")
#                 break
#             else:
#                 return func(*args)
#     return wrapper
#
# @delay(0)
# @string_format
# def summing(*args):
#    return args
#
# print(summing("Labas", "Labutelis"))
# print(summing(2, 2))
# print(summing("Test", "Test", 2))

def string_format(func):
    def wrapper(*args):
        list_int=[]
        for i in args:
            if type(i) != str:
                list_int.append(i)
        if len(list_int)>=1:
            return "Only strings are taken as inputs"
        else:
            return func(*args)
    return wrapper


@string_format
def joining(*args):
   string_list=[]
   for i in args:
       string_list.append(i)
   x = ''.join(string_list)
   return x

print(joining("Labas", "Labutelis"))
print(joining(2, 2))
print(joining("Test", "Test", 2))



# Parašykite dekoratorių, bet kokios funkcijos vykdymo laikui fiksuoti. Galite patobulinti, pvz funkcijos (vardas),
# su tokiais ir tokiais argumentais vykdymo laikas - XX s. Ištestuokite, su funkcija, grąžinančia svetainės atsako kodą ir su funkcija,
# išrenkančia pirminius skaičius užduotame diapazone.

from time import time
def time_counter(func):
    def wrapper(*args):
        start_time = time()
        return func(*args), print(f'Time collapsed: {time()-start_time} sec')
    return wrapper

@time_counter
def range_print(range_no):
    for i in range(range_no+1):
        print(i)

range_print(100)

import requests

@time_counter
def status_code(extention):
    r = requests.get(extention)  # sukuriame http užklausą
    print(r.status_code)

status_code('http://www.cnn.com')