#!/usr/bin/env python
# coding=utf-8

def decorator_function(original_function):
    def wrapper_funtcion():
        print("This is being ran 22")
        return original_function()
    return wrapper_funtcion

def display():
    print("display function ran")

display = decorator_function(display)


