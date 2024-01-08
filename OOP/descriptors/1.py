from datetime import datetime


class Time:
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return datetime.utcnow().isoformat()


class Logger:
    current_time = Time()


print(Logger.current_time)
log = Logger()
print(log.current_time)

