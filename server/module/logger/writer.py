from datetime import datetime


class _BinaryColor :
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Writer() :
    
    def __init__(self, path : str):
        super().__init__()
        self.p = path
        with open(f'{path}/twittool_log.txt','w',encoding='utf8') as w_file :
            w_file.write("---------TWITTOOL---------\n")
    
    def write(self, text : str):
        with open(f'{self.p}/twittool_log.txt', 'a', encoding='utf8') as w_file :
            w_file.writelines(text + '\n')
            
    def log(self, context : str, message : str) :
        text = f"[{context}][{datetime.now()}] - {message}"
        self.write(text)
        print(text)
    
    def warn(self, context : str, message : str) :
        text = f"{_BinaryColor.WARNING}[{context}][{datetime.now()}] - {message}{_BinaryColor.ENDC}"
        self.write(text)
        print(text)
        
    def fail(self, context : str, message : str) :
        text = f"{_BinaryColor.FAIL}[{context}][{datetime.now()}] - {message}{_BinaryColor.ENDC}"
        self.write(text)   
        print(text)
    
    def ask(self, context : str, message : str):
        text = f"{_BinaryColor.OKBLUE}[{context}][{datetime.now()}] - {message}{_BinaryColor.ENDC}"
        result = input(text)
        self.write(text + '->' + result)    
        return result