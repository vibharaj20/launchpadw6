lower, upper, digit, special = 0, 0, 0, 0
s = "Ms123456&"
if (len(s) >= 8 and len(s)<=16): 
    for i in s: 
  
        if (i.islower()): 
            lower+=1            
      
        if (i.isupper()): 
            upper+=1            
       
        if (i.isdigit()): 
            digit+=1            
         
        if(i=='@'or i=='$' or i=='_'): 
            special+=1           
if (lower>=1 and upper>=1 and digit>=1 and special>=1 and lower+upper+digit+special==len(s)): 
    print("Valid Password") 
else: 
    print("Invalid Password") 