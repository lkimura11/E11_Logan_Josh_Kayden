import RPi.GPIO as GPIO
import time
from datetime import datetime

PIN_NUM = 17
count = 0
log_file = "cup_count.txt"

def log_event(event):
    with open(log_file, "a") as f:
        f.write(event + "\n")

def count_num(channel):
    global count
    count += 1
    print('\n ▲ at ' + str(datetime.now())) 
    log_event(f"{datetime.now()} - Pulse detected")
    

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(PIN_NUM, GPIO.FALLING, callback=count_num)

try: 
     while True:
        time.sleep(10) 
        print(f"Counts in the last ten seconds were: {count}")
        log_event(f"{datetime.now()} - Counts in the last ten seconds: {count}")
        count = 0 #reset

  
except KeyboardInterrupt:
    print("\nExiting... Cleaning up GPIO.") 
    GPIO.cleanup()
print("Done!")
