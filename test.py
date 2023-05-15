import os

def sum(from: int, to: int) -> int:
    sum = 0
    for i in range(from, to + 1):
        sum += i
    return sum
  
def test_sum():
    assert sum(int(os.environ["SUM_INPUT_FROM"]),int(os.environ["SUM_INPUT_FROM"]))==5050
