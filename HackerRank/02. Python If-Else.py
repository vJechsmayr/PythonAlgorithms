# Author Aman Shekhar

import math
import os
import random
import re
import sys


num = int(input())

if num%2 == 0:
    if num > 20 or (2 <= num <= 5):
        print("Not Weird")
    elif 6 <= num <= 20:
        print("Weird")
else:
    print("Weird")
