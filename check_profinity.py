import urllib

def read_text():
    quotes = open('movie_quotes.txt')
    content = quotes.read()
    print(content)
    quotes.close()
    check_profinity(content)

def check_profinity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    print (output)
    connection.close()

read_text()