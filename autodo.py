import pyautogui as gui
import time
def fPress(key):
	#gui.press(key)
	fHold(key,0.000001)
def fHold(key,hold_time):
	gui.keyDown(key)
	time.sleep(hold_time)
	gui.keyUp(key)
def fHold2(key,hold_time):
	start=time.time()
	while time.time()-start<hold_time:
		gui.press(key)
if __name__=="__main__":
	filename=input("请输入脚本文件:")
	file=open(filename,'r')
	#read file
	x=file.read().replace("\t","").split()
	mod=len(x)
	times=[0]*len(x)
	hold=[0]*len(x)
	stop=[0]*len(x)
	keys=[10]*len(x)
	goto=[(i+1)%mod for i in range(len(x))]
	stk=[]
	for i in range(len(x)):
		if(x[i]=='{'):
			stk.append(i)
		elif('}' in x[i]):
			keys[i]=11
			goto[i]=stk.pop()
			times[i]=int(x[i][1:])
		else:
			keys[i]=x[i][0]
			if('(' in x[i]):
				hold[i]=0 if x[i][2:-1].split(':')[0]=="" else float(x[i][2:-1].split(':')[0])
				stop[i]=0 if x[i][2:-1].split(':')[1]=="" else float(x[i][2:-1].split(':')[1])
	now=0
	ntimes=[0]*len(x)
	print("start in 3 second")
	time.sleep(3)
	print("start")
	while now<mod:
		if keys[now]==11:# }
			if ntimes[now]+1==times[now]:
				ntimes[now]=0
				now=now+1
			else:
				ntimes[now]+=1
				now=goto[now]
		else:
			if keys[now]!=10:
				if(hold[now]==0):
					print(now)
					fPress(keys[now])
				else:
					fHold(keys[now],hold[now])
				time.sleep(stop[now])
			now=goto[now]
	print("done")
