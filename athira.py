wordcount=0
infile=open('file1.py','r')
content=infile.read()

print("content of the file is:",content)
print("length of file is:")
print(len(content))
wordcount=len(content.split(' '))
splitword=(content.split(' '))
print("No of words in a file:",wordcount)
for word in splitword:
    print(word)
 
