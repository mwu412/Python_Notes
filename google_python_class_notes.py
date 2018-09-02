"""Python Notes by Michael Wu 2018"""

# source:
# https://developers.google.com/edu/python
# https://youtu.be/tKTZoB2Vjuk


"""Concepts"""

# Python does things in the last moment
# Python checks the line when it runs the line

# Python don't need syntax of declare
# So you'd better make a good habit of naming variables
# For example: lists are always named "Something'''s'''"

# Move incrementally

# String is immutable

# for num in range(20) ...

# Do not modify the list while iterating over

# list: [a, b, c] can grow and shrink
# tuple: (a, b, c) fixed size, elements can't be changed

# Important concept

a = [1, 2, 3]
b = a  # this does NOT make a copy. it points to the same thing.
c = a[:]  # this makes a copy of a
del a[1]  # "b" will also be changed
del a  # "a" will be destroyed. but "b" will remain intact!!!!!

# How sorted & join & split works

a = ['aaaa', 'bb', 'ccc', 'd']
sorted(a, key=len)  # "len" is a function. sorted by length
':'.join(a)  # result: 'd:bb:ccc:aaaa'
a.split(':')  # result: [d, bb, ccc, aaaa]
'aa bb cc'.split()  # = ['aa', 'bb', 'cc']

# Dictionary

d = {}  # the elements of dictionary have no order. can only be sorted when outputting
d = {key1: value1, key2: value2}
d['a'] = 'alpha'  # d['key'] = 'value'
d.get('a')
d.get('not_exist')  # will do nothing
d.keys()  # = list of all keys
d.values()  # = list of all values
d.items()  # = [(key, value), (key, value), ...]

# How main function & sys.argv works

import sys


def hello(name):
    if name == 'Alice' or name == 'Paul':  # or
        name = name + '!'
    print('Hello', name)  # 'Hello Sean'


def main():
    hello(sys.argv[1])  # in command line: ./filename.py Sean
    # notice that it starts at [1]


if __name__ == '__main__':
    main()

# How to open a file

with open('test_text.txt', 'r+') as f:
    list_of_lines = f.readlines()  # make lines into list
    text = f.read()  # read entire file into a string

    f.write('yo\n')

    for line in f:  # loop through the file line by line
        print(line, end='')  # print will automatically make a new line each time
        # (end = '' helps us to avoid that)
        # (print(line, ) will also work)

# How to convert string to int

s = '123'
a = int(s)
b = 321
print(a + b)


# How to use class

class Car:  # inheritance: "DerivedClass(BaseClass01, BaseClass02):"
    def __init__(self, engine, gearbox):
        self.engine = engine
        self.gearbox = gearbox
        self.list = []
        self._foo = 1  # one under score: this is a convention: non-public
        self.__fat = 2  # two under scores: this is a syntax: name mangling
        pass  # (it will actually be: _method02__fat)

    def method01(self):  # method must have at least one argument.
        pass

    def _method(self):  # one under score: this is a convention: non-public
        pass  # (it should be treated as a non-public part of the API)


# What is generator

xvec = [1, 2, 3]
yvec = [4, 11, 6]

sum(x * y for x, y in zip(xvec, yvec))  # this will return the dot product
# "zip" is like a list but with parentheses instead of square brackets
# the generator is a tool for creating iterators. it resumes where it left off
# (it remembers all the data values and which statement was last executed)


# search

import re

m = re.search(r'([\w.]+)@([\w.]+)', "blah nick.p@gmail.com yatta")
m.group()  # = mick.p@gmail.com
m.group(1)  # = nick.p
m.group(2)  # = gmail.com

re.findall(r'[\w.]+@[\w.]+', "blah nick.p@gmail.com foo@bar")  # = ['nick.p@gmail.com, 'foo@bar']

# os

import os

dir(os)  # will show all methods come with os. use them as "os.example"

#

import commands


def list_of_directories(directory):
    cmd = 'ls -l' + directory
    (status, output) = commands.getstatusoutout(cmd)
    print(output)


# after importing a module(can be any module.py),
# you can dir(module), this will show all functions under this module
# you can then help(module.function), this will show """function description"""

def function_cool_man():
    """
    Describe the function here yo!

    """

# description of classes and methods works the same way
# help(module.class)
# help(module.class.method)


# urllib

import urllib

uf = urllib.urlopen('http://google.com')  # this will load the source code of the website
uf.read()

urllib.urlretrieve('http://google.com.intl/en_ALL/images/logo.git', 'foo.gif')
# this will retrieve and download the gif as 'foo.gif'


# more of lists

a = ['aaaa', 'bb', 'ccccc']
[len(s) for s in a]  # = [4, 2, 5]
