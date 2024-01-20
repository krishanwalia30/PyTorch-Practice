# def ans(string):
string = "*ba*ck**"
a = [i for i in range(len(string)) if string[i] == "*"]
print(a)
ans = ""
for i in string:
    if (i == "*" and string.index(i)== 0):
        continue
    elif(i == "*" and string[string.index(i) - 1] != "*"):
        ans = ans + string[string.index(i)]
        
# for i in len(a):

