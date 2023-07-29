# Created by matthewkight at 7/28/23
class Trie:

    def __init__(self):
        self.alpha = {}

    def insert(self, word: str) -> None:
        word += '*'
        d = self.alpha
        for letter in word:
            if letter not in d:
                d[letter] = {}
            d = d[letter]

    def search(self, word: str) -> bool:
        word += '*'
        d = self.alpha
        for letter in word:
            if letter not in d:
                return False
            d = d[letter]
        return True

    def startsWith(self, prefix: str) -> bool:
        d = self.alpha
        for letter in prefix:
            if letter not in d:
                return False
            d = d[letter]
        return True

if __name__ == '__main__':
    t = Trie()
    t.insert("Apple")
    t.insert("App")
    print(t.search("App"))
    print(t.search("Apple"))
    print(t.search("Appl"))
    print(t.startsWith("Appl"))