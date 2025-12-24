import time

last_position = 0

while True:
    with open("app.log", "r") as log:
        log.seek(last_position)
        new_lines = log.readlines()
        last_position = log.tell()

        for line in new_lines:
            if "ERROR" in line:
                print("ALERT: New error detected in AWS logs!")

    time.sleep(5)
