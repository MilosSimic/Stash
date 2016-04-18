def before(**items):
	def decor(func):
		def wrapper(*args, **kwargs):
			#do domething with items
			func(*args, **kwargs)
		return wrapper
	return decor

def after(**items):
	def decor(func):
		def wrapper(*args, **kwargs):
			func(*args, **kwargs)
			#do domething with items
		return wrapper
	return decor

def before_and_afer(**args):
	def decor(func):
		def wrapper(*args, **kwargs):
			#do domething with items
			func(*args, **kwargs)
			#do domething with items
		return wrapper
	return decor