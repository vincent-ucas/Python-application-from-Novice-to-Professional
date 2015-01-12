import sys

def wordcount():
    """

    :rtype : counting the words in file: **.txt
    """
    text = sys.stdin.read()
    words = text.split()
    word_count = len(words)
    print 'Word Count: ', word_count

def readfiles_fun():
    f = open('words.txt')
    for i in range(5):
        print str(i) + ': ' + f.readline()

    f.close()


if __name__ == '__main__' : wordcount()
