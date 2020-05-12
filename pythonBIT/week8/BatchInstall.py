# BatchInstall.py
import os
libs = {'wheel','numpy', 'matplotlib', 'pillow', 'sklearn', 'requests'}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print('successful')
except:
    print(lib+' installation failed')
