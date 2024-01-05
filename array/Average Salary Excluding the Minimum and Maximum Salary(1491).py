class Solution:
    def average(self, salary: List[int]) -> float:
        sorted_salary = sorted(salary)
        result = 0
        counter = 0

        for i in range(1, len(sorted_salary) - 1):
            result += sorted_salary[i]
            counter += 1

        return result / counter
