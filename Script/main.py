def info():
    print(
        colored(' [*] Your PC/exec. Informations:', 'dark_grey'),

f'''
    Platform:\t\t {platform.system()} - {platform.architecture()[0]}
    Py. Version:\t Python {platform.python_version()[0]}
    
    --termcolor = \"{version('termcolor')
}\".\n''')

def check(file):
    try:
        os.listdir(file)
        return '<dir>'
    
    except NotADirectoryError:
        pathAux, extension = os.path.splitext(file)
        return extension
    
def size(self, path):
    def convert(num):
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    try:
        if os.path.isfile(path):
            info = os.stat(path)
        return convert(info.st_size)
    
    except UnboundLocalError:
        size = 0
        for path, dirs, files in os.walk(path):
            for file in files:
                fp = os.path.join(path, file)
                size = os.path.getsize(fp)

        return convert(size)

def entry(self):
    self.dirs, self.arqs, self.error = 0, 0, 0

    self.path = input(' [*] Path Address To Scan: ').lower()
    self.folder = os.fsencode(self.path)

    try: os.listdir(self.folder)
    except FileNotFoundError as err:
        print(colored(f'\n [-] {type(err).__name__}: {err}.', 'red')); return False
    return True

def main(self):
    '''    
    ** MADE WITH/FOR:
        Platform:\t Windows
        Py. Version:\t Python 3

        --termcolor = "2.2.0"

    ** FORMATS:
        Last modified; Created; File type; File Size; File name.

    FUNCTION: Show The Descriptions About The Files in The Specified Path.

    --"Last modified:" And "Created:" In Default Format Of <ctime>:
        Weekday (Abbreviated);
        Month   (Abbreviated);
        Day     (Not Decimal);
        Hour    (24 Hour Clock);
        Year    (Decimal Number).
    
    ** OUTPUT SUBJECT TO EXTENSION ERROS BY THE "splitext".
    '''

    def Print():
        print(
            f'''  {    modified
                }\t  { created
                }\t  { checking
                }{     ' ' * ((len(checking) - 10) if (len(checking) not in (3, 4, 5)) else len(checking))
                }\t  [{self.size(file_path)
                }] {   ' ' * ((len(aux) - len(self.size(file_path))) + len('File name:'))
                }  {   filename
            }'''
        )

    info()
    if not self.entry(): return False
    
    for file in os.listdir(self.folder):
        filename = os.fsdecode(file)
        file_path = r"{}{}".format(self.path, filename)

        if len(filename) > 50:
            filename = filename[0:50] + colored('(...)', 'dark_grey')

        try:
            modified = ctime(os.path.getmtime(file_path))            
            created = ctime(os.path.getctime(file_path))

        except FileNotFoundError as err:
            print(colored(f'\n [-] {type(err).__name__}: {err}.', 'red')); return False

        try:
            checking = check(file_path)
            if '<dir>' != checking: self.arqs += 1
            else: self.dirs += 1
        except PermissionError as err:
            self.error += 1
            print(colored(f'  [-] {type(err).__name__}: {err}.', 'red')); continue

        try:
            aux
            Print()
        
        except NameError:
            aux = max([self.size(f'{self.path}/{os.fsdecode(file)}') for file in os.listdir(self.folder)], key=len)

            print(
            f'''\n Last modified:\t\t\t Created:\t\t\t File type:\t File Size:{' ' * (len(aux)+4)} File name:
            '''); Print()
    
    print(f'\n [+] Found {self.dirs} \"<dir(s)>\" And {self.arqs} \".file(s)" with {colored(f"{self.error} Error(s).", ("red" if self.error > 0 else None))}')

import os, platform

from time import ctime
from os import system
from termcolor import colored
from importlib.metadata import version

obj = type('Obj', (object, ), {'entry': entry, 'size': size, 'main': main})
start = obj()

try:
    while True: system('cls'); help(obj.main); start.main(); input()
except KeyboardInterrupt: exit(0)
except Exception as err: input(colored(f'\n {type(err).__name__}: {err}.', 'red'))