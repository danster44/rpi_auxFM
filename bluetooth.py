import random
import time
from rpi_lcd import LCD
import RPi.GPIO as GPIO
import subprocess

lcd = LCD()

def rand_message():
    message_library = {
        1: "Broadcasting at",
        2: "Hijacking",
        3: "New Station at",
        4: "Fuck the FCC!",
        5: "Piracy at",
        6: "Go listen to",
        7: "You're on air,",
        8: "Now playing at",
    }

    random_message = random.choice(list(message_library.values()))
    lcd.text(f"{random_message}", 1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    freq = 100.3
    loop_active = True
    while loop_active:
        lcd.text("Frequency: ", 1)
        lcd.text(f"{freq:.1f} MHz", 2)

        if GPIO.input(20) == False:
            freq = min(108.0, freq + 0.2)
            time.sleep(0.1)
            lcd.text(f"{freq:.1f} MHz", 2)

        if GPIO.input(21) == False:
            freq = max(88.1, freq - 0.2)
            time.sleep(0.1)
            lcd.text(f"{freq:.1f} MHz", 2)

        if GPIO.input(16) == False:
            loop_active = False

    # Handling after exiting loop
    rand_message()
    lcd.text(f"{freq:.1f} FM", 2)
    command = f"arecord -c 1 -d 0 -r 22050 -f S16_LE | sudo ./fm_transmitter/fm_transmitter -f {freq} - "
    subprocess.run(command, shell=True, check=True)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    time.sleep(1)
