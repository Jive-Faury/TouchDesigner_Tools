target=op('3DScope')
t = op('table1')
t.clear(keepFirstRow=True)
list=[]
print(list)



for pars in target.customPars:
	print(pars)	
	t.appendRow([pars.name])
	list.append(pars.val)
for i in range(t.numRows-1):
	print(i)
	t[i+1,1]=list[i]

	
	