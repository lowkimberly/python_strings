#String reversal
string=raw_input("Enter a string: ")
r=""
while len(string)!=0:
    r=r+string[len(string)-1]
    string=string[0:len(string)-1]
print r

#Palindromes
string=raw_input("Enter a string: ")
h1=""
h2=""
origlen=len(string)
h1=string[0:origlen/2]
if len(string)%2==0:
    while len(string)!=origlen/2:
        h2=h2+string[len(string)-1]
        string=string[0:len(string)-1]
if len(string)%2!=0:
    while len(string)!=(origlen/2)+1:
        h2=h2+string[len(string)-1]
        string=string[0:len(string)-1]
if h1==h2:
    print "This a Palindrome."
else:
    print "This is not a Palindrome."


