# your code goes here
"""
@author: Sumit Roy
DSE Project : Parking Lot System
"""

import Vehicle
import sys

class ParkingLot:
	def __init__(self):
		self.capacity = 0
		self.slotid = 0
		self.numOfOccupiedSlots = 0

	def createParkingLot(self,capacity):
		self.slots = [-1] * capacity
		self.capacity = capacity
		return self.capacity

	def getEmptySlot(self):
		for i in range(len(self.slots)):
			if self.slots[i] == -1:
				return i

	def park(self,regno,color):
		if self.numOfOccupiedSlots < self.capacity: 
			slotid = self.getEmptySlot()
			self.slots[slotid] = Vehicle.Car(regno,color)
			self.slotid = self.slotid+1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots + 1
			return slotid+1
		else:
			return -1

	def leave(self,slotid):

		if self.numOfOccupiedSlots > 0 and self.slots[slotid-1] != -1:
			self.slots[slotid-1] = -1
			self.numOfOccupiedSlots = self.numOfOccupiedSlots - 1
			return True
		else:
			return False

	def status(self):
		print("Slot No.\tRegistration No.\tColour")
		for i in range(len(self.slots)):
			if self.slots[i] != -1:
				print(str(i+1) + "\t\t" +str(self.slots[i].regno) + "\t\t" + str(self.slots[i].color))
			else:
				continue

	def getRegNoFromColor(self,color):

		regnos = []
		for i in self.slots:

			if i == -1:
				continue
			if i.color == color:
				regnos.append(i.regno)
		return regnos
			
	def getSlotNoFromRegNo(self,regno):
		
		for i in range(len(self.slots)):
			if self.slots[i].regno == regno:
				return i+1
			else:
				continue
		return -1
			

	def getSlotNoFromColor(self,color):
		
		slotnos = []

		for i in range(len(self.slots)):

			if self.slots[i] == -1:
				continue
			if self.slots[i].color == color:
				slotnos.append(str(i+1))
		return slotnos

	def screen(self,line):
		if line.startswith('create_parking_lot'):
			n = int(line.split(' ')[1])
			res = self.createParkingLot(n)
			print('Created a parking lot with '+str(res)+' slots')

		elif line.startswith('park'):
			regno = line.split(' ')[1]
			color = line.split(' ')[2]
			res = self.park(regno,color)
			if res == -1:
				print("Sorry, parking lot is full")
			else:
				print('Allocated slot number: '+str(res))

		elif line.startswith('leave'):
			leave_slotid = int(line.split(' ')[1])
			status = self.leave(leave_slotid)
			if status:
				print('Slot number '+str(leave_slotid)+' is free')

		elif line.startswith('status'):
			self.status()

		elif line.startswith('registration_numbers_for_cars_with_colour'):
			color = line.split(' ')[1]
			regnos = self.getRegNoFromColor(color)
			print(', '.join(regnos))

		elif line.startswith('slot_numbers_for_cars_with_colour'):
			color = line.split(' ')[1]
			slotnos = self.getSlotNoFromColor(color)
			print(', '.join(slotnos))

		elif line.startswith('slot_number_for_registration_number'):
			x=line.split()
			regno = x[1]
			slotno = self.getSlotNoFromRegNo(regno)
			if slotno == -1:
				print("Not found")
			else:
				print(slotno)
		elif line.startswith('exit'):
			exit(0)

if __name__ == '__main__':
    
	parkinglot = ParkingLot()
    
	print("Welcome to a Car Parking System")
	entry=int(input("\nPress 1 for Manual input\nPress 2 for File input\n"))
    
	if entry==1:        #Manual Input
		n=int(input("Create the total slots available "))
		capacity=parkinglot.createParkingLot(n)
    
        
		while True:
			print("\nPress 1 to park\nPress 2 to leave the Car on particular slot\nPress 3 for Status\nPress 4 for registration numbers for cars with colour\nPress 5 for slot numbers for cars with colour\nPress 6 for slot number for registration number\nPress 7 to Exit")
    
			action=int(input())
				
			if action == 1:     #Park
				getpark=input("Enter Lisence Number and Color of Car \n").split()
				
				parking=parkinglot.park(getpark[0],getpark[1])
				if parking == -1:
					print("Sorry, parking lot is full")
				else:
					print('Allocated slot number: '+str(parking))
                
			elif action == 2:   #Leave
				leave_slotid = int(input("Enter the slot number \n"))
				status = parkinglot.leave(leave_slotid)
				if status:
					print('Slot number '+str(leave_slotid)+' is free')
				 
			elif action == 3:   #Status
				print(parkinglot.status())
				
			elif action == 4:   #regno of car from color
				color=input("Enter the Color of the Car \n")
				regnos = parkinglot.getRegNoFromColor(color)
				print(', '.join(regnos))
                
			elif action == 5:   #slot number of car from color
				color=input("Enter the Color of the Car \n")
				slotnos = parkinglot.getSlotNoFromColor(color)
				print(', '.join(slotnos))
                
			elif action == 6:   #get slot number from regno
				regno=input("Enter the Registration number of the Car \n")
				slotno = parkinglot.getSlotNoFromRegNo(regno)
				if slotno == -1:
					print("Slot number doesnot found for the Car ")
				else:
					print(slotno)
                    
			elif action == 7:   #exit
				break
	elif entry == 2:        #textfile as input
		getentry=input("Enter your file name\n")
		with open(getentry) as f:
			for line in f:
				parkinglot.screen(line)