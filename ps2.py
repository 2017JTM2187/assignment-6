###### this is the second .py file ###########

board = [0,1,2,
         3,4,5,
          6,7,8]

odd=[1,3,5,7]
even=[2,4,6,8]


def show():



	print board[0],'|' ,board[1],'|',board[2]
print '--------------------'

print board[3],'|' ,board[4],'|',board[5]
print '--------------------'

print board[6],'|' ,board[7],'|',board[8]



print "Welcome to the Game!"

print "whether it is Player 1  or Player 2 chance."




pos =input("select the position ")
num= input("select the number")
while true:
	if ( board[input]!='1' and board [input]!='2' and board [input]!='3' and board [input]!='4' and board [input]!='5' and board [input]!='6' and board [input]!='7' and board [input]!='8' 		and board [input]!='0') :

	board [input]='I' or board [input]='III' or board [input]='V' or board [input]='VII' 
	
	finding=true

while finding:
   random.seed()
opponent = random.randint(0,8)

if ( board[opponent]!='1' and board [opponent]!='2' and board [opponent]!='3' and board [opponent]!='4' and board [opponent]!='5' and board [opponent]!='6' and board [opponent]!='7' and board [opponent]!='8' and board [opponent]!='0') :

board [input]='0' or board [input]='II' or board [input]='IV' or board [input]='VI'

finding=false

else:
print "Try again"


#if board[input]!= [1,3,5,7] and board[input]!=[2,4,6,8]
#board[input]=[1,3,5,7]


