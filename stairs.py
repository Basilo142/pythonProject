import sys
digit_string = sys.argv[1]
nom=int(digit_string)
denom=1
while nom > 0:
   #s=" "*(nom-1)+'#'*(denom)
   print(' '*(nom-1),'#'*(denom), sep='')
   nom-=1
   denom+=1
   #print(s)