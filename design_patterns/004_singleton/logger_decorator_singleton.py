def singleton(cls):
    instances ={}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(f"Creating new instance for {cls.__name__}")
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Logger:
    def __init__(self):
        print("Logger Initialized")
        self.logs = []

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
        