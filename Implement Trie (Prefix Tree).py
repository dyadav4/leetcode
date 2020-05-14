class Trie:

    def __init__(self, arr=None):
        """
        Initialize your data structure here.
        """
        self.arr = []
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.arr.append(word)        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.arr
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ispresent = False
        for i in self.arr:
            if i.startswith(prefix):
                ispresent = True
                break
        
        return ispresent
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
