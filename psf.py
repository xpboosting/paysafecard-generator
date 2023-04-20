import random
import string
import os
from colorama import init, Fore, Back, Style
import colorama

init(convert=True)
f = open('pscgen.txt', 'a')
print()
print(Fore.WHITE + 'how many codes do you want?: ')
amount = int(input())
fix = 1
os.system('cls')
while fix <= amount:
  psf = ('').join(random.choices(string.digits, k=15))
  url = "[Generating] PSC: "
  f.write(url + '0' + psf + '\n')
  psf_code = url + psf
  print(Fore.WHITE + url + '0' + psf)
  fix = fix+1
