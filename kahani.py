kahani = " "
while True:
   data = input("enter a story=>") 
   if len(data) == 0:
      print("the end!")
      break
   kahani += data + "\n"

with open('story.txt','w') as file: #print('The real story), print(kahani)
   file.write(kahani)