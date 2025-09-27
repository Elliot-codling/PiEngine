# Debug script to handle outputs to the terminal
# Message format will be in the form:
# [HH/MM/SS.SSS] [ERROR_TYPE] CONTENT
# Useful for debugging and when error occured at what time

# Change this to 'True' when you want to ship your project
# Can help with performance by not outputting to the console
releaseMode = False

# Define console colours
class consoleColors:
    DEFAULT = "\033[39;49m"
    GREY = "\033[90m" # Trace
    MAGENTA = "\033[95m" # Debug
    WHITE = "\033[97m" # Info
    YELLOW = "\033[93m" # Warning
    RED_WARNING = "\033[91m" # Error
    RED_FATAL = "\033[1;101m" # Fatal

class Logger:
    @classmethod
    def trace(cls, content):
        if releaseMode: return
        print(f"{consoleColors.GREY}{getTimeStamp()} [TRACE] {content} {consoleColors.DEFAULT}")

    @classmethod
    def debug(cls, content):
        if releaseMode: return
        print(f"{consoleColors.GREY}{getTimeStamp()} [DEBUG] {content} {consoleColors.DEFAULT}")

    @classmethod
    def info(cls, content):
        if releaseMode: return
        print(f"{consoleColors.GREY}{getTimeStamp()} [INFO] {content} {consoleColors.DEFAULT}")

    @classmethod
    def warning(cls, content):
        if releaseMode: return
        print(f"{consoleColors.GREY}{getTimeStamp()} [WARNING] {content} {consoleColors.DEFAULT}")

    @classmethod
    def error(cls, content):
        if releaseMode: return
        print(f"{consoleColors.GREY}{getTimeStamp()} [ERROR] {content} {consoleColors.DEFAULT}")

    @classmethod
    def fatal(cls, content):
        if releaseMode: return
        print(f"{consoleColors.GREY}{getTimeStamp()} [FATAL] {content} {consoleColors.DEFAULT}")

# Get time stamp
def getTimeStamp() -> str:
    import datetime
    timeNow = datetime.datetime.now()

    return f"[{timeNow.hour}:{timeNow.minute}:{timeNow.second}.{str(timeNow.microsecond)[0:3]}]"