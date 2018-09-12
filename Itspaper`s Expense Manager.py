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
        expense = pkl.load(open("Expense.data", "rb"))
        dates = pkl.load(open("Dates.data", "rb"))
    except FileNotFoundError:
        expense = []
        dates = []
        pkl.dump(expense, open("Expense.data", "wb"))
        pkl.dump(dates, open("Dates.data", "wb"))
    finally:
        return expense, dates


def expense_entry():
    spent = int(input("How much did you spend today? "))
    today = date()


# Main Code


today = date()
expense, dates = load()

