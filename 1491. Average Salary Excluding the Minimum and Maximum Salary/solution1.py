class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = maxSalary = salary[0]
        totalSalary = 0
        
        for s in salary:
            if s > maxSalary:
                maxSalary = s
            elif s < minSalary:
                minSalary = s
            totalSalary += s
        
        return (totalSalary - minSalary - maxSalary) / (len(salary) - 2)