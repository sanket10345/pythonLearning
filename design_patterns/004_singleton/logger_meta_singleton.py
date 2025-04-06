class SingletonMeta(type):
    _instances = {}

    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass = SingletonMeta):
    def __init__(self):
        print('Initializing Logger ...')
        self.logs = []
    def save_logs(self,log):
        self.logs.append(log)
    def get_logs(self):
        return self.logs

class AdvancedLogger(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing AdvancedLogger ...")
        self.logs = []
    def save_logs(self,log):
        self.logs.append(log)
    def get_logs(self):
        return self.logs

log1 = Logger()
log1.save_logs("🔹 First log")

log2 = Logger()
log2.save_logs("🔸 Second log")

aLog1 = AdvancedLogger()
aLog2 = AdvancedLogger()

print("Logs from log2:", log2.get_logs())
print("Logs from aLog2:", aLog2.get_logs())
print("Are log1 and log2 the same?", log1 is log2) # True
print("Are aLog1 and aLog2 the same?", aLog1 is aLog2) # True
print("Are log1 and aLog1 the same?", log1 is aLog1) # False
