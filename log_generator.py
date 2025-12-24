import time
import random

while True:
    level = random.choice(["INFO", "WARNING", "ERROR"])
    with open("app.log", "a") as log:
        log.write(f"{level}: Application running\n")
    time.sleep(5)
