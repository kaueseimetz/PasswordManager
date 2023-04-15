import os
from datetime import date
from datetime import datetime

with open("log.log", "w") as log:
    log.write(f"Started In: {date.today()} as {datetime.now().strftime('%H.%M.%S')}")
def lPrint(message):
    with open("log.log", "r") as log: #criar função para este
        logLeft = log.read()
    with open("log.log", "w", encoding="UTF-8") as log: #criar função para este
        log.write(logLeft + os.linesep + message)
