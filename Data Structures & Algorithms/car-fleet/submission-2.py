class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        merged = []
        for i in range(len(position)):
            merged.append([position[i], speed[i]])
        merged.sort(reverse=True)

        for p, s in merged:
            t = (target-p)/s
            if fleet and fleet[-1] >= t:
                continue
            fleet.append(t)
        print(fleet)
        return len(fleet)
