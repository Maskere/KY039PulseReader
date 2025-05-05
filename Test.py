import explorerhat
import time

while True:
    analog_value = explorerhat.analog.one.read()
    scaled_value = int(analog_value * 1023)
    print(f"Heartbeat: {scaled_value}")
    time.sleep(1)
