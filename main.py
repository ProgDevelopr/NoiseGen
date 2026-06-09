from rich import print
from random import choice
from math import sqrt

def is_prime(i):
    if i < 2:
        return False
    for j in range(2,int(sqrt(i)+1)):
        if i % j == 0:
            return False
    return True

def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        old_a = a
        a = b
        b = old_a + b
    return a

color = {
    'w': "[bold white]█[/]",
    'b': "[bold black]█[/]",
    'bl': "[bold blue]█[/]",
    'g': "[bold green]█[/]",
    'r': "[bold red]█[/]",
    'y': "[bold yellow3]█[/]",
    'p': "[bold pink1]█[/]",
    'c': "[bold cyan]█[/]",
    'o': "[bold orange]█[/]",
    'def': "█"
}

elements = [x.lower() for x in color.keys()]
H = 9
W = H

def formula(X):
    def display(color):
        pattern.append(color)
    for i in range(1,(X**2)+1):
        if is_prime(i):
            display('p')
        else:
            display('w')

pattern = []
if H > W:
    formula(H)
elif H < W:
    formula(W)
else:
    formula(H)

def random_noise():
    for _ in range(H):
        for _ in range(W):
            elem = color[choice(elements)]
            for _ in range(2):
                print(elem,end="")
        print()
        
def explicit_noise(pattern):
    i=0
    for _ in range(H):
        for j in range(W):
            j+=i
            try:
                elem = color[pattern[j]]
            except:
                elem = color['def']
            for _ in range(2):
                print(elem,end="")
        print()
        i+=W
        
explicit_noise(pattern=pattern)