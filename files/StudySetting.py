import os

from datetime import datetime

now = datetime.now()
now = str(now.date())

os.mkdir(now)

f = open(f'{now}/input.txt','w')

f.close()