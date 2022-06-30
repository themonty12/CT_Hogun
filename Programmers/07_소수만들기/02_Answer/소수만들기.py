def test(n):
    for i in range(2, n):
        if n % i == 0:
            return False 
        return True
temp = 0
answer = -1
li = [1,2,3,5,7,4]

#a = [i for i in li if i % 2 == 0]
#b = [i for i in li if i % 2 != 0]

for i in range(len(li)):    
    #for j in li(a+1,len(li)+1):
    for j in range(i + 1, len(li)):
        #print("i = " + li[i] + ", j = " + li[j])
        print("i = {}, j = {}".format(li[i], li[j])
        #print("i = {0}, j = {1}".format(li[i], li[j])