# coding utf-8
# Add some note for wls2 test
from termcolor import colored  
import sys

if len(sys.argv)!=2:
    print(colored("Usage: python print_color.py <N>", "yellow"))
    sys.exit()

N = int(sys.argv[1])

for i in range(N):
    print("hello world!")
    