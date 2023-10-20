# me - this DAT
# panelValue - the PanelValue object that changed
#
# Make sure the corresponding toggle is enabled in the Panel Execute DAT.

def onOffToOn(panelValue):
	s1= op.Engine.op('render1')
	s2= op.Engine.op('render2')
	
	trans = op.Engine.op('trans')
	change = op.Engine.op('change')['chan1']
	speed = op.Engine.op('speed')[0]

	
	target1 = op.Scenes.op('scene'  +str(me.parent().digits)  +'/content/geo*')
	#target2 = op.Engine.op('pathLights')[parent().digits,0]
	
	
	if change == 0:
		s2.par.geometry = target1
		#s2.par.lights= target2
		trans.par.value0 = speed

	else:
		s1.par.geometry = target1
		#s1.par.lights= target2
		trans.par.value0 = -speed
	return

def whileOn(panelValue):
	return

def onOnToOff(panelValue):
	return

def whileOff(panelValue):
	return

def onValueChange(panelValue):
	return
