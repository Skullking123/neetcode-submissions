class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Given an arr asteroids of integers representing asteroids in a row
        # The index represents the pos of the asteriod in the row
        # For abs(asteroids[i]) = the size of asteroid i
        # The sign of the asteroids[i] represents the direction the asteroid is moving
            # pos = moving right
            # neg = moving left
            # each asteroid moves at the same speed
        # Find out the state of the asteroids after all collisions
        # If two asteroids meet, the smaller one explodes
        # If both are the same size, both will explode
        # Two asteroids moving in the same direction will never meet
        LEFT = True
        RIGHT = False
        stack = [] 

        for asteroid in asteroids:
            curr_size = abs(asteroid)
            curr_dir = LEFT if asteroid < 0 else RIGHT
            # bool to check if asteroid survived all the collisions (if any)
            # with previous asteroids we have seen
            survive = True

            # check if any of the asteroids we have seen previously 
            # collide with our current one
            while stack:
                prev_size = abs(stack[-1])
                prev_dir = LEFT if stack[-1] < 0 else RIGHT

                # Check if a collision is not possible
                if not (curr_dir == LEFT and prev_dir == RIGHT):
                    break
                
                # See who survives
                if curr_size > prev_size:
                    stack.pop() # destroy prev
                elif curr_size == prev_size:
                    stack.pop() # destroy prev
                    survive = False # destroy curr
                    break
                else: # curr_size < prev_size
                    survive = False # destryo curr
                    break
            
            if survive:
                stack.append(asteroid)


        return stack














