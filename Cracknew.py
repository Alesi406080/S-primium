import os, platform
try:
   import requests
except:
   os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from libnk import __main_apikey__
    __main_apikey__()
elif bit == '32bit':
    from libnk import __main_apikey__
    __main_apikey__()
