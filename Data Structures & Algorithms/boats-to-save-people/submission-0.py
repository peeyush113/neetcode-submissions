class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        boats = 0
        l, r = 0, len(people)-1
        while l<=r:
            p = people[l]+people[r] 
            if people[l]+people[r] > limit:
                boats += 1
                r -=1 
            else:
                boats +=1
                r -=1 
                l +=1 
        return boats