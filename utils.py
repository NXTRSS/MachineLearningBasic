import os
import io
import pyAesCrypt
import pandas as pd
import pickle
import traitlets
from ipywidgets import widgets
from IPython.display import display


def decrypt_file(file_path, password):
    if password is None or password == '':
        raise ValueError(f'{bcolors.BOLD}{bcolors.FAIL}Please provide password')
        
    bufferSize = 64 * 1024
    encFileSize = os.stat(file_path).st_size

    fIn = open(file_path, 'rb')
    fDec = io.BytesIO()

    pyAesCrypt.decryptStream(fIn, fDec, password, bufferSize, encFileSize)
    
    return fDec


def decrypt_pandas(file_path, password):        
    fDec = decrypt_file(file_path, password)

    s=str(fDec.getvalue(),'utf-8')

    data = io.StringIO(s) 
    return pd.read_table(data, sep=',')


def decrypt_pickle(file_path, password):
    fDec = decrypt_file(file_path, password)

    return pickle.loads(fDec.getvalue())

        
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
