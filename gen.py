#DREW DORMAN

import random

from runJob import *

genInfo = 11
constLoc = 9
objLoc = 10
gen_amount = 15
traits = 5
mutation = 1.5

def breed(p1,p2,traits,mut):
	ch = [0] * traits
	
	for i in range(0,traits):
		r = random.randint(0,1)
		
		if(r == 0):
			r2 = random.randint(0,1)
			if(r2 == 0):
				ch[i] = p1[i] + p1[i]*random.uniform(-mut,mut) 
			else:
				ch[i] = p1[i] + p2[i]*random.uniform(-mut,mut) 
			
		else:
			r2 = random.randint(0,1)
			if(r2 == 0):
				ch[i] = p2[i] + p2[i]*random.uniform(-mut,mut) 
			else:
				ch[i] = p2[i] + p1[i]*random.uniform(-mut,mut) 
				
	return ch
	
#Sorts a 2D array (alist) by whichever column (by) [lowest to highest]
def mergeSort(alist,by):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf,by)
        mergeSort(righthalf,by)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][by] < righthalf[j][by]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
			
def rePop(alist,traits,mut,gen):
	nPop = [[0]* genInfo] * 10
	
	for i in range(4):
		nPop[i] = alist[i]
	
	count = 4
	for i in range(4):
		for j in range(3-i):
			ch = breed(alist[i],alist[j],traits,mut)
			ch[0] = int(ch[0])
			if(ch[0]%2 == 1):
				ch[0] = ch[0] + 1
			
			#results = [1, 2, 3, 4, 5, 6] #replace with ABQ job
			jobName = 'Gen-'+str(gen)+'-'+str(count)
			results = runJob(ch,jobName)
			results[len(results)-1] = results[len(results)-1] + ch[1]
			nPop[count] = ch + results
			count = count + 1
	return nPop

print '----------------'

iPop = [[26, 0.252708411040439, 0.165236791401838, 7.61894792524065, 2.55927813542684], 
	[20, 0.102133425393359, 0.189768586175493, 9.70435941525047, 3.35646762053668], 
	[22, 0.14379345775579, 0.164874266982347, 14.9220069203759, 2.67340273158064], 
	[28, 0.131926391329823, 0.153338793001328, 16.2881843455297, 2.9965554520435], 
	[30, 0.210429752161047, 0.15853751442186, 18.899622465156, 3.07305977884691], 
	[26, 0.194232411547827, 0.170053597033765, 12.8541908822269, 3.27660238908358], 
	[24, 0.290169909909836, 0.179271392905397, 17.6623252166148, 3.19858084858244], 
	[26, 0.264893209891699, 0.198254962437407, 5.14683605239976, 3.40986745810041], 
	[24, 0.175104249799487, 0.181020601713064, 8.46872928457871, 2.80906041009087], 
	[24, 0.175104249799487, 0.181020601713064, 8.46872928457871, 2.80906041009087]]
	


for i in range(0,gen_amount):
	gen = i
	print gen
	
	# if(i%5 == 0):
		# mutation = mutation*0.75
	
	DataFile = open('Gen-'+str(gen)+'.txt','w')
	DataFile.write('GEN: %d\n' % (gen))
	DataFile.write('row, th, r2, r4, l, maxRf, maxLE, maxS, avgS, crimp, obj\n')
	DataFile.close()
	
	if(i == 0):
		for j in range(10):
			results = [1, 2, 3, 4, 5, 6] #replace with ABQ job
			jobName = 'Gen-0-'+str(j)
			results = runJob(iPop[j],jobName)
			results[len(results)-1] = results[len(results)-1] + iPop[j][1]
			iPop[j] = iPop[j] + results
		Pop = iPop

	for j in range(10):
		a = Pop[j]
		DataFile = open('Gen-'+str(gen)+'.txt','a')
		DataFile.write('%f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f\n' % (a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10]))
		DataFile.close()
	
	mergeSort(Pop,objLoc)
	Pop = rePop(Pop,traits,mutation,gen)
	
	mutation = mutation*0.75
	
	
	
print 'DONE'




