import sys

def wordCount():
    text = sys.stdin.read()
    words = text.split()
    word_count = len(words)
    print 'Word Count: ', word_count

if __name__ == '__main()__' : wordCount()
