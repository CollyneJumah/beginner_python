from mymodule import general_fullname,sum_of_two_numbers
# During importing we can rename the name of the module.
from mymodule import general_fullname as gFullname, sum_of_two_numbers as sum

print(general_fullname('Collins','Jumah'))
print(sum_of_two_numbers(23,45))

#importing built-in modules
# math, datetime,os,sys,random,statstics,collections,json,re

#os Module: erform many operation system tasks. provides functions for creating,changing 
# current working directory and removing a directory(folder), fetching its content, 
# chnging and identifying the current directory.

import os
# making directory
# os.mkdir('myfolder')
# changing directory
# os.chdir('../')
# getting current woring directory
# os.getcwd()
# os.rmdir()


#Sys module:: provides functions and variables used to
#  manipulate different parts of the pyhton run-time environment. 
# Function sys.argv returns a list of command line arguments passed 
# to a python script.The item at index 0 in this list is always the name of the script,
#  at index 1 is the name of the argument passed from the command line.  
import sys 
# print ('Welcome {}. Enjoy {} challenge!' .format(sys.argv[1], sys.argv[2]) )


#to know the largest integer it takes
sys.maxsize

#to know the environment path
sys.path

# to know the version of python you Using
sys.version

#to exit
# sys.exit()


#statistic module:: provide function for mathematical statistics of numeric data.
# The polpular statistical functions which are defined in this module: means, median,modestdev

from statistics import * #importing all the statistic module
ages = [20,23,24,25,26,27,28,29]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# Maths Modules ::Module containing many methematical operations and constants

import math
print(math.pi) #pi constant
print(math.sqrt(2)) #squareroot
print(math.pow(2,3)) #exponential function
print(math.floor(9.81)) #rounding to the lowest
print(math.ceil(9.81)) #rounding to the highest
print(math.log10(100)) #logarithm with base 10

# to check what functions the module has got we use help or dir. this will display available functions in the module

# help(math)
# dir(math)

#If we want to import only aspecific function,from the module
from math import pi
print(pi)

#to import multiple functions
from math import pi, sqrt,pow,floor,ceil,log10
print(pi)
print(sqrt(5))
print(pow(3,2))
print(floor(9.89))
print(math.log10(1000))

#if you want to import all the functions use *
from math import *
print(pi)
print(sqrt(5))
print(pow(3,2))
print(floor(9.89))
print(math.log10(1000))

# you can as well rename the name of the function
from math import pi as PI
print(PI)


#String module :: 
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)


#Random module:: gives a random number returns a value between 0,0.9999
from random import random,randint

print(random())
print(randint(5,40))
