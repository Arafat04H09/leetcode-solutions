[3,1,2,4]
#--- manual calculate
    3,1 3-1
    3,1,2 3-1
    3,1,2,4 4-1
    1,2 2-1
    1,2,4 4-1
    2,4 4-2
    res=3*2+4*3+2*1-(1*5+2*1)=13 
#=== sum(min)
    [x+1 for x in left] = [1,2,1,1]
    [x+1 for x in right] = [1,3,2,1]
    f = [1*1,2*3,1*2,1*1]
    sum(min)= 3 * 1 + 1 * 6 + 2 * 2 + 4 * 1 = 17
#---sum(max)
    f2=[3,1,2,4]
    sum(max)= 9+1+4+16 = 17+13 = 30
#---
  res= sum(max) - sum(min) = 30 -17 = 13