import os

dirs = ['executables','io','staticfiles','submittedcodes','media']

def main():
	# create executables directory
	BASE_DIR = os.getcwd()
	execdir = os.path.join(BASE_DIR,'executables')
	if not os.path.exists(execdir):
		try:
			os.makedirs(execdir)
		except:
			print('Error occured when creating directory \'executables\'')
			raise
	for d in dirs:
		dirpath = os.path.join(BASE_DIR, d)
		if not os.path.exists(dirpath):
			print('{} directory could not be found'.format(d))
			raise
	print('everything is good')	
		

if __name__ == '__main__':
	main()
