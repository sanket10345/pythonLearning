class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = cls._instance = super().__new__(cls)
            return cls._instance
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            print("Initializing only once")
            self.logs = []
            Logger._initialized = True

    def save_logs(self,log):
        self.logs.append(log)
    def get_logs(self):
        return self.logs

l1 = Logger()
l1.save_logs("🔹 First log")

l2 = Logger()
l2.save_logs("🔸 Second log")

print("Logs from l2:", l2.get_logs())
print("Are l1 and l2 the same?", l1 is l2)