import sys
from urllib.request import urlopen


def fetch_words(txt='http://sixty-north.com/c/t.txt'):
    story = urlopen(txt)
    story_words = []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
