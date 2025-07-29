try:
 file=open("file.txt","r+")
 read=file.read()
 print(read)
 file.close()

except(FileNotFoundError):
   print("File not found")
finally:
  print('end')