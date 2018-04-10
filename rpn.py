#!/usr/bin/env python3

import operator
import math


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': math.pow,
    '!': math.factorial,
    'sum': sum,
    '^': math.pow,
    '.': math.floor,
    '%': operator.truediv,
}

def calculate(myarg):
    stack = list()
    past = ''
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            if token == '!':
              stack.append(function(stack.pop()))
            elif token == 'sum':
              temp = function(stack)
              stack.clear()
              stack.append(temp)
            elif token == '.':
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.append(function(arg1 / arg2))
            elif token == '%':
                stack.append(function(stack.pop(), 100))
                past = '%'
            else:
                arg2 = stack.pop()
                arg1 = stack.pop()
                if past == '%' and token == '+':
                    function = operators['*']
                    arg2 = arg2 + 1
                if past == '%' and token == '-':
                    function = operators['*']
                    arg2 = 1 - arg2
                result = function(arg1, arg2)
                stack.append(result)
                past = ''
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
