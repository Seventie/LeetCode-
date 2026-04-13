class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        storage = defaultdict(int)
        for x in range(len(numbers)):
            remain = target - numbers[x]
            if remain in storage :
                return [storage[remain]+1,x+1]
            storage[numbers[x]] = x 
            print(storage)
        return []