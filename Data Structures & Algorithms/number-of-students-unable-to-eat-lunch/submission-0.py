class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        counter = Counter(students)

        for s in sandwiches:
            if counter[s]>0:
                n -= 1
                counter[s] -= 1
            else:
                break
        return n