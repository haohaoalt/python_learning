# coding utf-8
from termcolor import colored  
import sys

if len(sys.argv)!=2:
    print(colored("Usage: python hello.py <N>", "yellow"))
    sys.exit()

N = int(sys.argv[1])

for i in range(N):
    print("hello world!")