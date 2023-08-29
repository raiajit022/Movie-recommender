import datetime
import os


def write_log(message: object) -> object:
    # create Logs folder if it does not exist
    if not os.path.exists("Logs"):
        os.mkdir("Logs")
    # get the current date and time
    now = datetime.datetime.now()
    date = now.strftime("%d:%m:%Y")
    time = now.strftime("%I:%M %p")
    # create a log file with the date as the name
    file_name = "Logs/" + date + ".txt"
    # open the file in append mode
    with open(file_name, "a") as f:
        # write the message with the time
        f.write(time + " - " + message + "\n")
