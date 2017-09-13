import IEM as iem
import pickle as pkl
import time as t

pause = iem.pause
clear = iem.cls

__version__ = "ALPHA"
__author__ = "Rodrigo 'ItsPaper' Muñoz"
expense = []
dates = []
# Functions

def date():
    date = t.strftime("%B %d")
    return date

def load():
    try:
        expense = pikle.load(open("Expense.data", "rb"))
        dates = pikle.load(open("Dates.data", "rb"))
        return expense, dates
