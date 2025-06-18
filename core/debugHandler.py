
#define GREEN "\033[92m"
#define MAGENTA "\033[95m"
#define YELLOW "\033[93m"
#define RED "\033[91m"
#define DEFAULT "\033[39;49m"
class consoleColors:
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    DEFAULT = "\033[39;49m"

def printInfo(content: str) -> None:
    print(f"{getDateAndTime()} [{consoleColors.GREEN}INFO{consoleColors.DEFAULT}] {content}")

def printDebugInfo(content: str) -> None:
    print(f"{getDateAndTime()} [{consoleColors.MAGENTA}DEBUG{consoleColors.DEFAULT}] {content}")

def printWarningInfo(content: str) -> None:
    print(f"{getDateAndTime()} [{consoleColors.YELLOW}WARNING{consoleColors.DEFAULT}] {content}")

def printErrorInfo(content: str) -> None:
    print(f"{getDateAndTime()} [{consoleColors.RED}ERROR{consoleColors.DEFAULT}] {content}")

def getDateAndTime() -> str:
    import datetime
    timeNow = datetime.datetime.now()

    return f"[{timeNow.day}/{timeNow.month}/{timeNow.year}] [{timeNow.hour}:{timeNow.minute}:{timeNow.second}.{str(timeNow.microsecond)[0:3]}]"