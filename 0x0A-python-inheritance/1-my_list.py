#!/usr/bin/python3
# 1-my_lists.py
# Sweilam
""" Inheritance """

class MyList(list):
    """ The class mylist inherits from list class. """

    def print_sorted(self):
        print(sorted(self))
        
