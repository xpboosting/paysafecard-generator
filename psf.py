import random
import string
from colorama import init, Fore, Back, Style
import colorama

init(convert=True)
f = open('pscgen.txt', 'a')
print()
print(Fore.WHITE + 'how many codes do you want?: ')
amount = int(input())
fix = 1
while fix <= amount:
  psf = ('').join(random.choices(string.digits, k=16))
  url = "[Generating] PSC: "
  f.write(url + psf + '\n')
  psf_code = url + psf
  print(Fore.WHITE + url + psf)
