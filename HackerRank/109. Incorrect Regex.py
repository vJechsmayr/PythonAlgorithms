# Author Aman Shekhar

import re
for _ in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except:
        print('False')