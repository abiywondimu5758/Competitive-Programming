class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        divisors = {3:"Fizz", 5:"Buzz"}
        return [''.join([divisors[j] for j in divisors if i%j == 0]) or str(i) for i in range (1,n+1)]
