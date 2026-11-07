#Star Pyramid Pattern:
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

n = int(input("Enter a value:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= n-i:
            print(" ",end="")
        else:
            print("*",end=" ")
    print()


     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''
n = int(input("Enter a value:"))
for i in range(1,n+1):
    print(" "*(n-i) + "* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i) + "* "*i)
