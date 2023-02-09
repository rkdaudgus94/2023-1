import os
os.chdir('C:/Users/rkdau/Onition/faces')

file_name = os.listdir()
a=[]
for filename in file_name :
    a.append(os.path.splitext(filename)[0])
    print(os.path.splitext(filename)[0])
    print(a)

print(a[0])