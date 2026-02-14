class Logger:
    # variabile statice (de clasa)
    INFO = 1
    WARNING = 2
    ERROR = 3

    level = INFO

    @staticmethod
    def set_level(new_level):
        Logger.level = new_level

    @staticmethod
    def info(msg):
        if Logger.level <= Logger.INFO:
            print(f'[INFO] {msg}')

    @staticmethod
    def warning(msg):
        if Logger.level <= Logger.WARNING:
            print(f'[WARNING] {msg}')

    @staticmethod
    def error(msg):
        if Logger.level <= Logger.ERROR:
            print(f'[ERROR] {msg}')

if __name__ == "__main__":
    Logger.set_level(Logger.ERROR)
    Logger.info('this is an info msg')
    Logger.warning('warning msg')
    Logger.error('error msg')
