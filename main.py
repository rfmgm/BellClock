from fastapi import FastAPI
from pydantic import BaseModel
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
app = FastAPI()
 
class SetGPIO(BaseModel):
    on: bool
 
@app.get("/fast/{count}")
def fast(count: int):
    gpio = 23
    GPIO.setup(gpio, GPIO.OUT)
    for i in range(0, count):
        GPIO.output(gpio, 1)
        time.sleep(0.1)
        GPIO.output(gpio, 0)
        time.sleep(0.9)
    return

@app.get("/slow/{count}")
def slow(count: int):
    gpio = 23
    GPIO.setup(gpio, GPIO.OUT)
    for i in range(0, count):
        GPIO.output(gpio, 1)
        time.sleep(0.1)
        GPIO.output(gpio, 0)
        time.sleep(1.4)
    return
 

