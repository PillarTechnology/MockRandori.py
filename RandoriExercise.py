# Randori Exercise

# Using the code below
# Write a test that fakes the response from Pants.pull
# Write a test that fakes the response from Moon.shoot
# Write a test that mocks the constructor of Moon, replacing Moon with a Mock
# Write a test that detects the arguments of Mathy.add
# Write a test that fakes the response of Mathy.add for any call
# Write a test that fakes the response of Mathy.add for a specific call (say 2+2 = 5)
# Write a test that fakes the response of Mathy.add to throw and exception
# Write a test that fakes the response of Mathy.add for more than one set of arguments (say 2+2=5, 3+3=9, 4+4=14)


class Service(object):

	def __init__(self):
		self.moon = Moon()

	def pull_pants(self):
		return Pants().pull()

	def shoot_moon(self):
		return self.moon.shoot()

	def do_math(self, num1, num2):
		return Mathy().add(num1, num2)

class Moon(object):

	def shoot(self):
		return "With what do you propose I shoot the moon?"

class Pants(object):

	def pull(self):
		return "Ouch!"

class Mathy(object):

	def add(self, num1, num2):
		return num1 + num2

service = Service()
print(service.pull_pants())
print(service.shoot_moon())
print(service.do_math(2,2))