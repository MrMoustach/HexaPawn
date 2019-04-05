file1 = open("accounts.txt","r")
x = file1.readlines();
file1.close()
t = []
m = t
for line in x:
    t.append(line.split())
# for one in t[0]:
#     m.append(one.split(":"))
for one in t[0]:
    print(one.split(":"))
