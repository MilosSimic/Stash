def before(driver, priority, **items):
	def decor(func):
		def wrapper(*args, **kwargs):
			#do domething with items
			func(*args, **kwargs)
		return wrapper
	return decor

def after(driver, priority, **items):
	def decor(func):
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
			#do domething with items
		return wrapper
	return decor

def before_and_afer(driver, priority, **args):
	def decor(func):
		def wrapper(*args, **kwargs):
			#do domething with items
			func(*args, **kwargs)
			#do domething with items
		return wrapper
	return decor