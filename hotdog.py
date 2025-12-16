"""
HOTDOG
===
an util for math 
version : 1.0.0 
for use ::
    >>> import hotdog as hd
expmples ::
    >>> valieble = hd.gauss(1 , 100 , 1)
    >>> print(valieble)
    output ::
    >>> 5050
github link :
    <https://www.github/example.com>
    
"""





#------------------simple--math-------------------#
#                                                 #
pi = 3.14


                             
def add(num1 , num2):
    return num1 + num2


def circle_area(r):
    return r * r * 3.14


def circle_round(r):
    return r * 3.14

def square_area(a):
    return a * a

def minus(num1 , num2):
    return num1 - num2

def deon(num1 , num2):
    return num1 / num2

def avge(num1 ,num2):
    first = num1 + num2
    return first / 2

def gauss(start:float , count:float , step:float)-> float:
    a = start
    b = count
    c = step
    first = ((b - a) / c) + 1
    secound = ((a + b) / 2)* first
    return secound

def volume(a:float , b:float , height:float):
    return a * b * height
 

def bos(number1:float , number2:float)-> float:
    if number1 >= number2:
        return number1 
    else :
        return number2
    
def DeonN(num1:float, num2:float)-> float:
    return num1 // num2

def help():
    a = """hotbog its math module"""
    return a


def mean(numbers):
    """محاسبه میانگین یک لیست از اعداد"""
    if len(numbers) == 0:
        return 0  # یا می‌توانید خطا بدهید
    return sum(numbers) / len(numbers)

def angpolygon(interior:float)->float:
    inte = interior
    return (inte - 2) * 180

import math

# فرمول‌های هندسی
def trapezoid_area(base1, base2, height):
    return (base1 + base2) * height / 2

def interior_angles_sum(n_sides):
    return (n_sides - 2) * 180

# فرمول‌های جبری
def quadratic_formula(a, b, c):
    """ریشه‌های معادله درجه دو"""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    return x1, x2
