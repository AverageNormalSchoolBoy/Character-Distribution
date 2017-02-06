"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
string = input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "{0}" is: '.format(string))
string.lower()
a = string.count('a')
b= string.count('b')
c= string.count('c')
d= string.count('d')
e= string.count('e')
f= string.count('f')
g= string.count('g')
h= string.count('h')
i= string.count('i')
j= string.count('j')
k= string.count('k')
l= string.count('l')
m= string.count('m')
n= string.count('n')
o= string.count('o')
p= string.count('p')
q= string.count('q')
r= string.count('r')
s= string.count('s')
t= string.count('t')
u= string.count('u')
v= string.count('v')
x= string.count('x')
y= string.count('y')
z= string.count('z')
w= string.count('w')

an=('a'*(a))
bn=('b'*(b))
cn=('c'*(c))
dn=('d'*(d))
en=('e'*(e))
fn=('f'*(f))
gn=('g'*(g))
hn=('h'*(h))
inn=('i'*(i+1))
jn=('j'*(j+1))
kn=('k'*(k+1))
ln=('l'*(l+1))
mn=('m'*(m+1))
nn=('n'*(n+1))
on=('o'*(o+1))
pn=('p'*(p+1))
qn=('q'*(q+1))
rn=('r'*(r+1))
sn=('s'*(s+1))
tn=('t'*(t+1))
un=('u'*(u+1))
vn=('v'*(v+1))
wn=('w'*(w+1))
xn=('x'*(x+1))
yn=('y'*(y+1))
zn=('z'*(z+1))
lst=[a, b]
lst1=[an, bn]
lst2=zip(lst, lst1)
lst.sort()
print(list(lst2))
