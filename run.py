import random

def main():
	ss = ""
	for i in range(512):
		isnum = random.randint(0,1)
		if isnum == 1:
			ss += chr(random.randint(48,57))
		else:
			ss += chr(random.randint(97,122))
	ss += "\n"
	print(ss)
	open('run.dat','w').write(ss)
	print("written to run.dat")

if __name__ == "__main__":
	main()
