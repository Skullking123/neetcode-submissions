class PrefixTree:

    def __init__(self):
        self.isWord = False
        self.children = [None] * 26
        
    def insert(self, word: str) -> None:
        cPtr = 0 # ptr to a letter in our current word
        curr = self

        # keep iterating until we reach the end of the letter, creating a node for each individual letter 
        # in the word. Only creating new nodes where they are missing
        while cPtr < len(word):
            # grab the curr's child that corresponds to the letter that cPtr is pointing at 
            letter = word[cPtr]
            letterChildIdx = ord(letter) - ord('a')
            letterChild = curr.children[letterChildIdx]

            # add the child if it doesn't exist
            if letterChild is None:
                letterChild = PrefixTree()
                curr.children[letterChildIdx] = letterChild
            
            # setup for next iteration
            curr = letterChild
            cPtr += 1
        
        # by the time we exit the loop, curr will be the last node in our word, 
        # set the flag
        curr.isWord = True

    def search(self, word: str) -> bool:
        cPtr = 0 # ptr to a letter in our current word
        curr = self

        # keep iterating until we reach the end of the word. If we find a letter missing at any point, return false
        while cPtr < len(word):
            # grab the curr's child that corresponds to the letter that cPtr is pointing at 
            letter = word[cPtr]
            letterChildIdx = ord(letter) - ord('a')
            letterChild = curr.children[letterChildIdx]

            if letterChild is None:
                return False
            
            curr = letterChild
            cPtr += 1
        
        # check to see if the word was actually inserted in and
        # doesn't just happen to be a prefix to a word already inserted before
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        cPtr = 0 # ptr to a letter in our current prefix
        curr = self

        # keep iterating until we reach the end of the word. If we find a letter missing at any point, return false
        while cPtr < len(prefix):
            # grab the curr's child that corresponds to the letter that cPtr is pointing at 
            letter = prefix[cPtr]
            letterChildIdx = ord(letter) - ord('a')
            letterChild = curr.children[letterChildIdx]

            if letterChild is None:
                return False
            
            curr = letterChild
            cPtr += 1
        
        # if we reach here, then there must be words in the tree that has our prefix
        return True
        
        