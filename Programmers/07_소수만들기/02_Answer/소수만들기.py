def test(n):
    for i in range(2, n):
        if n % i == 0:
            return False 
        return True

temp = 0
answer = -1
li = [1,2,3,5,7,4]

 a = [i for i in li if i % 2 == 0]
 b = [i for i in li if i % 2 != 0]
