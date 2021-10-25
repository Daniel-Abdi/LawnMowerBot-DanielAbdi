import RPi.GPIO as GPIO

class RoboDerby:

	def __init__(self, A1, A2, B1, B2):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup([A1, A2, B1, B2], GPIO.OUT)
		self.m1 = GPIO.PWM(A1, 1000)
		self.m2 = GPIO.PWM(A2, 1000)
		self.m3 = GPIO.PWM(B1, 1000)
		self.m4 = GPIO.PWM(B2, 1000)
		
	def forward(self, dc):
		self.m1.start(dc)
		
		self.m3.start(dc)
		
	def right(self, dc):
		self.m1.start(dc)
		self.m3.start(dc/3)
	def left(self, dc):
		self.m1.start(dc/3)
		self.m3.start(dc)
	def backward(self, dc):
		self.m2.start(dc)
		self.m4.start(dc)
	def stop(self):
		self.m1.ChangeDutyCycle(0)
		self.m2.ChangeDutyCycle(0)
		self.m3.ChangeDutyCycle(0)
		self.m4.ChangeDutyCycle(0)		
	def backright(self,dc):
		self.m2.start(dc)
		self.m4.start(dc/3)
	def backleft(self, dc):
		self.m2.start(dc/3)
		self.m4.start(dc)
