eTof = {
	'bread':'pain','wine':'vin','with':'avec', 'eats':'mange',
    'drinks':'boit', 'John':'Jean', 'Friends':'amis',
	'and':'et', 'of':'du', 'red':'rouge'
}
fToe = {
	'pain':'bread', 'vin':'wine', 'avec':'with', 'mange':'eats','et':'and',
    'du':'of', 'rouge':'red'

}

dicts = {'English to French':eTof, 'French to English':fToe}
def translateWord(word, dictionary):
	if word in dictionary.keys():
		return dictionary[word]
	elif word != '':
		return '""' + word + '""'
	return word


def translate(phrase, dicts, direction):
	UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
	letters = UCLetters + LCLetters	
	dictionary = dicts[direction]
	translation = ''
	word = ''
	for c in phrase:
		if c in letters:
			word = word + c
	 	else:
			translation = translation(word, dctionary) + c
			word = ''
	return translation + '' + translateWord(word, dictionary)

print(translate("John drinks good red wine, and eats bread", dicts, 'English to French'))
print(translate("jean boit du vin rouge", dicts, 'French to English'))

		



'''
def findDivisor(n1, n2):
    """ assumes theat n1 and n2 are positive ints
    returns  tuple containing common divisible of n1 & n2 
   """
    divisor = () # empty tuple
    for i in range(1, min(n1,n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisor = divisor +(i,)
    return divisor

divisors = findDivisor(20,100)
print(divisors)



total = 0 # initial value for 0
for d in divisors:
    total += d
print(total)


'''
