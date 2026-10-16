class WordDictionary:

    def __init__(self):
        self.letter = ""
        self.isWord = False
        self.children = [None] * 26
        
    def addWord(self, word: str) -> None:
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
                letterChild = WordDictionary()
                letterChild.letter = letter
                curr.children[letterChildIdx] = letterChild
            
            # setup for next iteration
            curr = letterChild
            cPtr += 1
        
        # by the time we exit the loop, curr will be the last node in our word, 
        # set the flag
        curr.isWord = True

    def search(self, word: str) -> bool:
        # . can match to any letter
            # will need to check all children whenever . appears
        # must be able to backtrack to ensure we don't miss any other potential paths
        # should intelligently only go down the paths that it needs to
        
        stack = [self]
        seen = set()
        seen.add(None) # just to prevent the alg from traversing to nonexsistent nodes
        cPtr = 0 # ptr to a letter in our current word
        while stack:
            curr = stack[-1]
            print(curr.letter)
            # a check once we have reached the end 
            if cPtr == len(word):
                if curr.isWord: # we have found what we are looking for
                    return True
                else: # go back since we have exceed the length of our word
                    cPtr -= 1
                    seen.add(curr)
                    stack.pop()
                    continue;
            
            print(cPtr) 
            letter = word[cPtr]
            letterIdx = ord(letter) - ord('a')
            if letter == ".":
                notFound = True
                # find a child and traverse down it
                print("Looking for child")
                for child in curr.children:
                    if child not in seen:
                        stack.append(child)
                        cPtr += 1
                        print(f"Incrementing cPtr {cPtr}")
                        notFound = False
                        break
                # all children have been explored, so go back
                if notFound:
                    print("Couldn't find child")
                    seen.add(curr)
                    cPtr -= 1
                    stack.pop()
            else: # an actual letter
                next = curr.children[letterIdx]
                # we cannot go any further so go back
                if next is None or next in seen:
                    stack.pop()
                    seen.add(curr)
                    cPtr -= 1
                else: # drill down 
                    stack.append(next)
                    cPtr += 1
            print(cPtr)
            print()
        return False

                

                
                        














