import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (2048, 1536)
camera.annotate_text = 'Hello world!'
time.sleep(2)
# Take a picture including the annotation
camera.capture('foo.jpg')
