import json
import opc
import time
import buttonpress
import pygame
pygame.init()
song = pygame.mixer.Sound('Canon D.ogg')
clock = pygame.time.Clock()
song.play()

class Note:
	note = 0
	ledIndex = 0
	
	def __init__(self, note, ledIndex):
		self.note = note
		self.ledIndex = ledIndex
	
	def update(self):
		if(self.note == 0):
			self.ledIndex += 1
			if(self.ledIndex > 6):
				noteList.remove(self)
				return buttonpress.red()
		if(self.note == 1):
			self.ledIndex -= 1
			if(self.ledIndex < 9):
				noteList.remove(self)
				return buttonpress.green()
		if(self.note == 2):
			self.ledIndex += 1
			if(self.ledIndex > 22):
				noteList.remove(self)
				return buttonpress.yellow()
		if(self.note == 3):
			self.ledIndex -= 1
			if(self.ledIndex < 25):
				noteList.remove(self)
				return buttonpress.blue()
		return 0

with open('Canon D.json') as f:
	data = json.load(f)

notes = data["charts"][2]["notes"]
noteList = []
health = 8

lastTimestamp = 0;

numLEDs = 64

client = opc.Client('localhost:7890')

for note in notes:
	pixels = [ (0,0,0) ] * numLEDs
	pixels[7] = (255,0, 0)
	pixels[8] = (0,255, 0)
	pixels[23] = (0,0, 255)
	pixels[24] = (255,255, 0)
	
	nextTimestamp = note[0];
	timeDifference = nextTimestamp - lastTimestamp
	time.sleep(timeDifference)
	lastTimestamp = nextTimestamp
	#print(note[1])
	for ledNote in noteList:
		health += ledNote.update()
		if health > 8:
			health = 8
		if health < 0:
			health = 0
			print 'GAME OVER'
	#After for loop, change number of pixels are purple on right column.
	for i in range(8):
		if i < health:
			pixels[56+i] = (255, 25, 255)
		else:
			pixels[56+i] = (0,0,0)
	for i in range(4):
		if(note[1][i] != '0'):
			if(i == 0):
				n = Note(i,0)
			if(i == 1):
				n = Note(i,15)
			if(i == 2):
				n = Note(i,16)
			if(i == 3):
				n = Note(i,31)
			noteList.append(n)
	for ledNote in noteList:
		if(ledNote.note == 0):
			pixels[ledNote.ledIndex] = (255,0, 0)
		if(ledNote.note == 1):
			pixels[ledNote.ledIndex] = (0,255, 0)
		if(ledNote.note == 2):
			pixels[ledNote.ledIndex] = (0,0, 255)
		if(ledNote.note == 3):
			pixels[ledNote.ledIndex] = (255, 255, 0)
	
	client.put_pixels(pixels)
