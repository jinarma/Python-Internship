
def start_mad_libs():
	print('Jeeves [verb] my [adjective] [noun] out of the [noun] as if he were a vegetarian fishing a [noun] out of his salad.')
	print('Enter one verb, an adjective, and three nouns: ')
	verbs = []
	adjectives = []
	nouns = []
	verbs.append(input('Verb: '))
	adjectives.append(input('Adjective: '))
	for i in range(3):
		nouns.append(input('Noun: '))
	mad_libs(verbs, adjectives, nouns)

def mad_libs(verbs, adjectives, nouns):
	print('Jeeves {} my {} {} out of the {} as if he were a vegetarian fishing a {} out of his salad.'.format(verbs[0], adjectives[0], nouns[0], nouns[1], nouns[2]))

start_mad_libs()
