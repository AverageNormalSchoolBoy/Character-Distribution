"""
distribution.py
Author: Brendan
Credit: Mr. Dennison, Stackoverflow

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
inn=('i'*(i))
jn=('j'*(j))
kn=('k'*(k))
ln=('l'*(l))
mn=('m'*(m))
nn=('n'*(n))
on=('o'*(o))
pn=('p'*(p))
qn=('q'*(q))
rn=('r'*(r))
sn=('s'*(s))
tn=('t'*(t))
un=('u'*(u))
vn=('v'*(v))
wn=('w'*(w))
xn=('x'*(x))
yn=('y'*(y))
zn=('z'*(z))
lst1=[a*100+1, b*100+2, c*100+3, d*100+4, e*100+5, f*100+6, g*100+7, h*100+8, i*100+9, j*100+10, k*100+11, l*100+12, m*100+13, n*100+14, o*100+15, p*100+16, q*100+17, r*100+18, s*100+19, t*100+20, u*100+21, v*100+22, w*100+23, x*100+24, y*100+25, z*100+26]
lst=[an, bn, cn, dn, en, fn, gn, hn, inn, jn, kn, ln, mn, nn, on, pn, qn, rn, sn, tn, wn, xn, yn, zn]
lst2=zip(lst, lst1)
lst3=sorted(lst2, key=lambda x: x[1], reverse=True)
lst, lst1 = zip(*lst3)
print("\n" .join(lst))
