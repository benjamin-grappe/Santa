#! /usr/bin/python
# _*_coding:utf8_*_

print "     ***** ORDERING INPUT *****"

f = open("input.txt", 'r')
data = [e for e in f.read().split('\n') if e != ""]

taskNames = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ante = {tn:[] for tn in taskNames}
for iDat, vDat in enumerate(data):
	ante[ vDat[36] ].append( vDat[5] )

print "     ***** PART ONE *****"

tasks = taskNames
order = ""
while len(tasks) > 0:
	for tn in tasks:
		if len(set(ante[tn])-set(order)) > 0: continue #If any pretask undone,skip
		order += tn
		tasks = tasks.replace(tn, '')
		break		
print "(i) %s"%order

print "     ***** PART TWO *****"

baseDelay = 60    # Common base time for every tasks
tasks = taskNames # List of tasks to complete
done = ""         # List of complete tasks
time = -1         # initial time
nPara = 5         # Max number of parallel tasks
ongoing = ""      # String of 5 char. max containing ongoing tasks' name
remaining = []    # List of 5 int max ; seconds needed to achieve respective tasks

while len(done) < len(taskNames):

	time += 1
	nCurrent = len(ongoing)

	# Just in case...
	assert nCurrent <= 5
	assert len(remaining) == nCurrent

	# Decrementing remaining time
	for iCur in range(nCurrent):
		remaining[iCur] -= 1

	# Looking for finished tasks (reverse order because finished tasks are poped).
	for iCur in range(nCurrent)[::-1]:
		if remaining[iCur] > 0: continue
		done += ongoing[iCur]
		ongoing = ongoing.replace(done[-1], '')
		remaining.pop(iCur)

	# Assigning new jobs if possible
	stillLooking = True # initialize flag "possibly some tasks ready to start".
	while len(ongoing)<nPara and len(tasks)>0 and stillLooking:
		stillLooking = False # If no task found ready, assume there's none!
		for tn in tasks:
			# Is every pre-tasks done?
			if len( set(ante[tn]) - set(done) ) > 0: continue
			ongoing += tn
			remaining.append(baseDelay+1+taskNames.index(tn))
			tasks = tasks.replace(tn, '')
			stillLooking = True # There could be other tasks ready to start.
			break

	# Inform the user
	print "(i) %4is %5s %s"%(time, ongoing, done)

print "(i) Needed %i seconds to complete."%time

print "See you, space cowboy."
#CFGHAEMNBPRDISVWQUZJYTKLOX & 828
