from itertools import cycle
tabula_recta = dict()
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in alpha:
	row = list()
	pos = alpha.index(i)
	while True:
		if(len(row)==26):
			break
		else:
			row.append(alpha[pos])
			pos = (pos + 1)%len(alpha)
	tabula_recta[i]=row

def decrypt(ciphertext):
	fd1 = open("wordlist.txt","r")
	for a in fd1:
		plaintext = list()
		key = list()
		a = a.rstrip()
		pad = cycle(a)
		for i in pad:
			if(len(key)<=len(ciphertext)):
				key.append(i)
				continue
			else:
				break
		for x,z in zip(key,ciphertext):
			plaintext.append(alpha[tabula_recta[x].index(z)])
		guess = ''.join(a for a in plaintext)
		print "Guess:",a,guess
		
def main():
	ciphertext = list()
	fd = open("ciphertext.txt","r")
	for i in fd:
		i = i.rstrip()
		for j in i:
			ciphertext.append(j)
	decrypt(ciphertext)
main()
		
