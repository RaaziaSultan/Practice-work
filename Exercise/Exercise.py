def print_stars(stars,space):
    x=" "
    for k in range(space-1):
         x=" "+x
    for j in range(stars):
         x=x+"*"
         
    print(x)
          
n=int(input("enter:  "))

for i in range(1,n):
    
     print_stars(i,n-i)
      
      OUTPUT
      enter:  6
     *
    **
   ***
  ****
 *****

<---------------------------------->

def print_stars(stars,space):
    x=" "
    for k in range(space-1):
         x=" "+x
    for j in range(stars):
         x=x+"*"
         
    print(x)
          
n=int(input("enter:  "))

for i in range(1,n):
    
     print_stars(n-i,i)
      
      OUTPUT
      enter:   6
   *****
    ****
     ***
      **
       *
