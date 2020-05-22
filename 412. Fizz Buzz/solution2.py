class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(1, n+1):
            string = ""
            if i % 3 == 0:
                string += "Fizz"
                isAppended = True
            if i % 5 == 0:
                string += "Buzz"
                isAppended = True
            if not string:
                string += str(i)
            ret.append(string)
        return ret