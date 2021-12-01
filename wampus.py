dirs = ["right","left","up","down"]
gm = 1
gn = 1
pm = 3
pn = 0
h = 0
visited = []
w = [[2,0,0,0],[1,2,0,2],[2,0,2,1],[0,0,0,2]]
print(w)
p = [[0,0,4,3],[0,4,3,4],[0,0,4,0],[0,4,3,4]]
print(p)
k = [["","","",""],["","","",""],["","","",""],["","","",""]]
k[pm][pn] = 'S'
print(k)
tl = []
tl2 = []
present = ""
prev = ""
tmp = ""
tv = 1
mypath = []

def getMatrix(msg,m):
	print(msg)
	matrix = []
	for i in range(m):
		rl = []
		tmp = raw_input();
		tmp = tmp.replace(' ', '')
		for i in range(len(tmp)):
			fl =  int(tmp[i])
			rl.append(fl)
		matrix.append(rl)
		rl = []	
	print(matrix)

def setdirections_for(i,j):
	si = str(i)
	sj = str(j)
	r = str(j+1)
	l = str(j-1)
	u = str(i-1)
	d = str(i+1)
	if i is 0 and j is 0:
		dirs[0] = si + r 
		dirs[1] = ""
		dirs[2] = ""
		dirs[3] = d  + sj 
		#print i," ",j,"down right"
	elif i is 0 and j is 3:
		dirs[0] = "" 
		dirs[1] = si + l
		dirs[2] = ""
		dirs[3] = d  + sj 
		#print i," ",j,"left down"
	elif i is 3 and j is 0:
		dirs[0] = si + r 
		dirs[1] = ""
		dirs[2] = u  + sj
		dirs[3] = "" 
		#print i," ",j,"up right"
	elif i is 3 and j is 3:
		dirs[0] = "" 
		dirs[1] = si + l
		dirs[2] = u  + sj
		dirs[3] = "" 
		#print i," ",j,"left up"
	elif i is 0:
		dirs[0] = si + r 
		dirs[1] = si + l
		dirs[2] = ""
		dirs[3] = d  + sj 
		#print i," ",j,"left down right"
	elif i is 3:
		dirs[0] = si + r 
		dirs[1] = si + l
		dirs[2] = u  + sj
		dirs[3] = "" 
		#print i," ",j,"left up right"
	elif j is 0:
		dirs[0] = si + r 
		dirs[1] = ""
		dirs[2] = u  + sj
		dirs[3] = d  + sj 
		#print i," ",j,"up right down"
	elif j is 3:
		dirs[0] = "" 
		dirs[1] = si + l
		dirs[2] = u  + sj
		dirs[3] = d  + sj 
		#print i," ",j,"left up down"
	else:
		dirs[0] = si + r 
		dirs[1] = si + l
		dirs[2] = u  + sj
		dirs[3] = d  + sj 
		#print i," ",j,"left up right down"

def getdiagonals_for(i,j):
	iup 	=	str(i-1)
	idown	=	str(i+1)
	jright 	=	str(j+1)
	jleft	=	str(j-1)
	if i is 0 and j is 0:
		dirs[0] = "" 
		dirs[1] = ""
		dirs[2] = ""
		dirs[3] = idown + jright 
		#print i," ",j,"down right"
	elif i is 0 and j is 3:
		dirs[0] = "" 
		dirs[1] = ""
		dirs[2] = idown + jleft
		dirs[3] = ""
		#print i," ",j,"left down"
	elif i is 3 and j is 0:
		dirs[0] = "" 
		dirs[1] = iup + jright
		dirs[2] = ""
		dirs[3] = ""
		#print i," ",j,"up right"
	elif i is 3 and j is 3:
		dirs[0] = iup + jleft 
		dirs[1] = ""
		dirs[2] = ""
		dirs[3] = ""
		#print i," ",j,"left up"
	elif i is 0:
		dirs[0] = "" 
		dirs[1] = ""
		dirs[2] = idown + jleft
		dirs[3] = idown + jright
		#print i," ",j,"left down right"
	elif i is 3:
		dirs[0] = iup + jleft 
		dirs[1] = iup + jright
		dirs[2] = ""
		dirs[3] = ""
		#print i," ",j,"left up right"
	elif j is 0:
		dirs[0] = "" 
		dirs[1] = iup + jright
		dirs[2] = ""
		dirs[3] = idown + jright
		#print i," ",j,"up right down"
	elif j is 3:
		dirs[0] = iup + jleft 
		dirs[1] = ""
		dirs[2] = idown + jleft
		dirs[3] = ""
		#print i," ",j,"left up down"
	else:
		dirs[0] = iup + jleft 
		dirs[1] = iup + jright
		dirs[2] = idown + jleft
		dirs[3] = idown + jright
		#print i," ",j,"left up right down"
		 
	
def allowedsteps(ls):
	for objs in dirs:
		if objs is not "":
			ls.append(objs)
	return ls

def checkforwumpus(steps):
	if w[int(steps[0])][int(steps[1])] is 1:
		print ("Player got killed")
		print (visited)	
		print (k)
		exit(0)
	elif w[int(steps[0])][int(steps[1])] is 2:
		return '2'
	else:
		return '0'

def checkforpit(steps):
	if p[int(steps[0])][int(steps[1])] is 3:
		print ("Player got killed")
		print (k)
		exit(0)
	elif p[int(steps[0])][int(steps[1])] is 4:
		return '4'
	else:
		return '0'

def getdiagonals(step):
	ls = []
	getdiagonals_for(int(step[0]),int(step[1]))
	ls = allowedsteps(ls)
	return ls

def stepintocell(step):
	ws = checkforwumpus(step)
	pb = checkforpit(step)
	return ws+pb

def applylogic_from_knowledge():
	global tl2,present,tv
	print ("\n\nApplying logic")
	for step in tl:
		print ("_______________thinking for %s_________________"%(step))
		if step in visited:
			print (step,"is visited so avoid thinking about that\n")
			if int(step[0]) is pm and int(step[0]) is pn:
				print( "1")
			elif '2' in k[int(step[0])][int(step[1])]:
				print( "2")
		else:
			setdirections_for(int(step[0]),int(step[1]))
			tl2 = tl2[0:0]
			tl2 = allowedsteps(tl2)
			print ("Connections of",step,"checking for :",tl2)
			#print present
			#print prev
			for st in tl2:
				if st  == present:
					print (st,"is it is present")
				else:
					print( "************************checking :",st)
					#print "Visited :",visited
					#print present,step,start
					dg = getdiagonals(st)
					print ("Diagonals",dg),
					if st in start:
						print( st,"is Start state")
					elif st == present:
						print (st,"is Present state")		
					elif st in visited:
						print (st,"yes it is in visited")
						if (k[int(st[0])][int(st[1])] in ['04','40','02','20']) and (k[int(present[0])][int(present[1])] in ['02','20','04','40']):
								print ("Applying first condition and is true")
								k[int(step[0])][int(step[1])] = 'S'
								print( "Putting Safe State at ",int(step[0]),int(step[1]))
								print ("Visited :",visited)
								return step
								print( "\n")
					else:
						for objs in dg:
							if objs in start:
								print( "Diagonal",objs,"is Start state")
							elif objs == present:
								print ("Diagonal",objs,"is Present state")		
							elif objs in visited:
								tv = 1
								print ("%s is diagonal of %s which is visited"%(objs,st))
								
							else:
								print( objs,"not visited")
						else:
							if tv is not 1:
								print( "here Nothing could be done for",st)
	print( "________________\n")
	return 0		


def whats_nextstep(ws,wp):
	global tl,present,prev,tmp,h
	print ("\nThinking whats_nextstep from",ws,wp),
	print ("\nNow present is :",present),
	print ("Now previous is :",prev)
	setdirections_for(ws,wp)
	tl = tl[0:0]
	tl = allowedsteps(tl)
	if ws == gm and wp == gn:
		h = 1
		if h is 1:
			print ("\nHurray!!Got the Gold"),
		print( "\nPresently in %s returning back to %s"%(present,start))
		#print mypath
		for steps in range(len(mypath),0,-1):
			#print "Stepping into ",mypath[steps-1]
			prev = present
			present = mypath[steps-1]
			#print "Present : ",present,"Previous :",prev
		print( "Now reached to :",present)
		exit(0)	
		#return_to_initial_postition()
	elif k[ws][wp] is "S":
		print( "\nSafe Cell")
		print( "Allowed Steps",tl),
		for step in tl:
			tmp = step
			if step not in visited:
				print (step,"Not visited")
				prev = present
				print ("previous cell :",prev)
				present = step[0]+step[1]
				print ("present cell",present)
				#print "Visited :",visited
				#Theres something wrong here
				k[int(step[0])][int(step[1])] = stepintocell(step)
				print ("\nStepping into ",step[0],step[1])
				mypath.append(step)
				visited.append(step)
				print( visited)
				print( k)
				whats_nextstep(int(step[0]),int(step[1]))
				print()
			else:
				print (step,"already visited"),	
	else:
		print ("\nNot a Safe Cell"),
		print ("\nConnections of ",present,":",tl),
		if ws is 2 and wp is 2:
			print (tl)
			#print "exiting"
			#exit(0)
		l = applylogic_from_knowledge()
		print ("i got here",l)
		if l is 0:
			print ("Stepping Back to",prev,"\n")
			mypath.pop()
			print (prev)
			present = prev
			print (present,prev)
			whats_nextstep(int(prev[0]),int(prev[1]))
		else:
			print( "here I reached********************")
			visited.append(l)
			print( visited)
			prev = tmp
			present = l	
			print (present,prev)
			print ("\nfrom here Stepping into ",l),
			mypath.append(l)
			whats_nextstep(int(l[0]),int(l[1]))
					
if __name__ == "__main__":
	#getMatrix("Enter Matrix",4);
	'''
	for i in range(1,5):
		for j in range(1,5):
			setdirections_for(i,j)
			print "from",i,j,"it can move to",
			allowedcells()
	'''
	prm = pm
	prn = pn
	start = str(pm)+str(pn)
	visited.append(start)
	print (visited)
	print( "Starting from ",pm,pn)
	prev = str(pm)+str(pn)
	present = str(pm)+str(pn)
	mypath.append(start)
	whats_nextstep(pm,pn)
	print (present)
	print (k)
