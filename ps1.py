#!/usr/bin/python

str2 = input(' Enter binary bit data which has to be transmitted.')
print(str2)

sub='1'
print "str2.count(sub) : ", str2.count(sub)


if (str2.count(sub)%2 ==0) :
	str2 = str2 + sub
print "binary bit data with parity bit:",str2


pattern="010"

ind = str2.index(pattern)

print str2.index(pattern)

ind3=ind+3

seq="0"
print str2.join(seq)

#str3 = str2[0:] + str2(ind2)=0 + str2[ind+3:]

print "Modified string received at the other end:",str2

   
    
  





