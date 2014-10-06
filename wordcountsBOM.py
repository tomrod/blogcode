import urllib2

def word_count(message):
	words = message.split()
	counts = {}
	for word in words:
		try:
			counts[word] += 1
		except KeyError:
			counts[word] = 1
	return counts

exclude = ['.',',','?','!',':',';','-','0','1','2','3','4','5','6','7','8','9',u'\xef',u'\xbb',u'\xbf']
words = urllib2.urlopen('http://www.gutenberg.org/cache/epub/17/pg17.txt').read()
words2 = ''.join(ch.lower()*(ch not in exclude) + ' '*(ch in exclude) for ch in words)
counts = word_count(words2)
