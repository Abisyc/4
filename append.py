a=input("Write what to write in file \n")
with open("output.txt","w") as file:
 file.write(a)
print("text written")
b=input("Write additional text to write in file \n")
with open("output.txt","a") as file:
 file.write(b)
print("text written ")
with open("output.txt","r") as file:
 file=file.read()
print("the final text in file is ")
print(file)
