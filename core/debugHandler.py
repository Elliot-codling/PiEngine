# Debug script to handle outputs to the terminal
# Message format will be in the form:
# [DD/MM/YYYY][HH/MM/SS.SSS] [ERROR_TYPE] CONTENT
# Useful for debugging and when error occured at what time

# Change this to 'True' when you want to ship your project
# Can help with performance by not outputting to the console
releaseMode = False

# Define console colours
class consoleColors:
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    DEFAULT = "\033[39;49m"

# Used for general info like creating windows
def printInfo(content: str) -> None:
    if releaseMode: return
    print(f"{getDateAndTime()} [{consoleColors.GREEN}INFO{consoleColors.DEFAULT}] {content}")

# Used by the user from 'mainScript.py' instead of the engine
def printDebugInfo(content: str) -> None:
    if releaseMode: return
    print(f"{getDateAndTime()} [{consoleColors.MAGENTA}DEBUG{consoleColors.DEFAULT}] {content}")

# When an object cannot be initialised or causes something not to work correctly
# Only used when the program can still run but not as intended
def printWarningInfo(content: str) -> None:
    if releaseMode: return
    print(f"{getDateAndTime()} [{consoleColors.YELLOW}WARNING{consoleColors.DEFAULT}] {content}")

# Used for when game crashes occur
# Outputs to the terminal before a crash to alert the user of the error
def printErrorInfo(content: str) -> None:
    if releaseMode: return
    print(f"{getDateAndTime()} [{consoleColors.RED}ERROR{consoleColors.DEFAULT}] {content}")

# Get date and time stamps
def getDateAndTime() -> str:
    import datetime
    timeNow = datetime.datetime.now()

    return f"[{timeNow.day}/{timeNow.month}/{timeNow.year}] [{timeNow.hour}:{timeNow.minute}:{timeNow.second}.{str(timeNow.microsecond)[0:3]}]"