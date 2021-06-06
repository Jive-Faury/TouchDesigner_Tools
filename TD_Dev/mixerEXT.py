
class mixerEXT:
	"""
	mixer description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.metaItems = ['length', 'sample_rate']
		self.currentSlot = 'slotA'

	def addItem(self):
		"""
		add playlist item in the playlist DAT
		"""
		for row in iop.MediaDat.rows('*')[1:]:
			items = self.getMeta(row)
			debug(items)
			iop.playlist.appendRow(row + items)

	def getMeta(seld, mediaRow):
		"""
		return a mete list of media data for the specified media row
		"""
		iop.MetaTop.par.file = mediaRow[1]
		iop.MetaTop.par.reload.pulse()
		items = []
		for item in self.metaItems:
			items.append(iop.MetaChop[item].eval())
		return items

	def clearPlayList(self):
		"""
		clear playlistDat table
		"""
		iop.playlistDat.clear()

	def onSelectRow(self,info):
		"""
		handles the onSelectRow callback for the lister
		"""
		nextSlot = 'slotB' if self.currentSlot == 'slotA' else 'slotA'
		player = getattr(iop, self.currentSlot)
		mediaPath = info['rowData']['rowObject'][1]
		player.par.file = mediaPath
		player.par.reload.pulse()
		self.cross()
		self.currentSlot = nextSlot

	def onClick(self, info):
		if info['colName'] == 'Delete'
		debug(info)

	def cross(self):
		self.ownerComp.Mixab = True if self.currentSlot == 'slotB' else False
