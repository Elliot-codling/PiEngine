# Debug script to handle outputs to the terminal
# Message format will be in the form:
# [HH/MM/SS.SSS] [ERROR_TYPE] CONTENT
# Useful for debugging and when error occured at what time

# Change this to 'True' when you want to ship your project
# Can help with performance by not outputting to the console
releaseMode = False

# Define console colours
class ConsoleColors:
    DEFAULT = "\033[39;49m"
    GREY = "\033[90m" # Trace
    MAGENTA = "\033[95m" # Debug
    WHITE = "\033[97m" # Info
    YELLOW = "\033[93m" # Warning
    RED_WARNING = "\033[91m" # Error
    RED_FATAL = "\033[1;101m" # Fatal


# === Logger ===
class Logger:
    @classmethod
    def trace(cls, process, content):
        if releaseMode: return
        print(f"{ConsoleColors.GREY}{getTimeStamp()} [{process}] [TRACE] {content} {ConsoleColors.DEFAULT}")

    @classmethod
    def debug(cls, process, content):
        if releaseMode: return
        print(f"{ConsoleColors.GREY}{getTimeStamp()} [{process}] [DEBUG] {content} {ConsoleColors.DEFAULT}")

    @classmethod
    def info(cls, process, content):
        if releaseMode: return
        print(f"{ConsoleColors.GREY}{getTimeStamp()} [{process}] [INFO] {content} {ConsoleColors.DEFAULT}")

    @classmethod
    def warn(cls, process, content):
        if releaseMode: return
        print(f"{ConsoleColors.GREY}{getTimeStamp()} [{process}] [WARNING] {content} {ConsoleColors.DEFAULT}")

    @classmethod
    def error(cls, process, content):
        if releaseMode: return
        print(f"{ConsoleColors.GREY}{getTimeStamp()} [{process}] [ERROR] {content} {ConsoleColors.DEFAULT}")

    @classmethod
    def fatal(cls, process, content):
        if releaseMode: return
        print(f"{ConsoleColors.GREY}{getTimeStamp()} [{process}] [FATAL] {content} {ConsoleColors.DEFAULT}")

# === Get time stamp ===
def getTimeStamp() -> str:
    import datetime
    timeNow = datetime.datetime.now()

    return f"[{timeNow.hour}:{timeNow.minute}:{timeNow.second}.{str(timeNow.microsecond)[0:3]}]"