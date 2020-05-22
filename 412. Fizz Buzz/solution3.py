class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        mDict = {3: "Fizz", 5: "Buzz"}
        ret = []
        for i in range(1, n+1):
            string = ""
            for key, value in mDict.items():
                if i % key == 0:
                    string += value
            if not string:
                string += str(i)
            ret.append(string)
        return ret