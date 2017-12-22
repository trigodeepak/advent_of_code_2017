with open('input.txt') as f:
   lines = f.readline()
   s = lines.strip()
   count = 0
   res = 0
   i = 0
   n = len(s)
   gar = 0
   while(i<n):
      if s[i] == '{':
         count+=1
      elif s[i] == '<':
         gar-=1
         while(s[i]!='>'):
            if s[i] == '!':
               gar-=1
               i+=1
            i+=1
            gar+=1
      elif s[i] == '}':
         res+=count
         count-=1
      i+=1
   print res,gar
   
