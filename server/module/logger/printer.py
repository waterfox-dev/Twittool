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

class Printer :

    @staticmethod
    def log(context : str, message : str) :
        print(f"[{context}][{datetime.now()}] - {message}")
    
    @staticmethod
    def warn(context : str, message : str) :
        print(f"{_BinaryColor.WARNING}[{context}][{datetime.now()}] - {message}{_BinaryColor.ENDC}")

    @staticmethod
    def fail(context : str, message : str) :
        print(f"{_BinaryColor.FAIL}[{context}][{datetime.now()}] - {message}{_BinaryColor.ENDC}")    
    
    @staticmethod
    def ask(context : str, message : str):
        result = input(f"{_BinaryColor.OKBLUE}[{context}][{datetime.now()}] - {message}{_BinaryColor.ENDC}")    
        return result