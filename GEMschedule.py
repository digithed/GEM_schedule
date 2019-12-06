import os
if ModuleNotFoundError() == True:
	os.system('pip3 install icalendar datetime pytz')

from datetime import datetime, timedelta
from icalendar import Calendar, Event
import os
from pytz import timezone


cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')
eastern = timezone('US/Eastern')
event = Event()
event2 = Event()
event3 = Event()
event4 = Event()
event5 = Event()
event6 = Event()
event7 = Event()
event8 = Event()

class Week():

<<<<<<< HEAD
	def __init__(self, date, strain, injtype, investigator_name):
		self.date = date
		self.strain = strain
		self.injtype = injtype
		self.investigator_name = investigator_name
		self.execute()


	def execute(self):
		if self.strain == '1':
			mouse_strain = 'B6'
			female_number = '15'

			if self.injtype == "1":
				CRISPR_type = input('Guide-test (1) or experiment (2)? ')
				if CRISPR_type == '1':
					CRISPR = self.CRISPR(False, False, mouse_strain, female_number)
					if CRISPR:
						os.system("open CRISPR.ics")
				
				elif CRISPR_type == '2':
					CRISPR = self.CRISPR(True, True, mouse_strain, female_number)
					if CRISPR:
						os.system("open crispr.ics")
			
				
			if self.injtype == "2":
				ESC = self.ESC(mouse_strain)
				if ESC:
					os.system("open ESC.ics")
				
		elif self.strain == '2':
			mouse_strain = 'BDF'
			female_number = '6'

			if self.injtype == "1":
				CRISPR_type = input('Guide-test (1) or experiment (2)? ')
				if CRISPR_type == '1':
					CRISPR = self.CRISPR(False, False, mouse_strain, female_number)
					if CRISPR:
						os.system("open CRISPR.ics")
				
				elif CRISPR_type == '2':
					CRISPR = self.CRISPR(True, True, mouse_strain, female_number)
					if CRISPR:
						os.system("open crispr.ics")
			
				
			if self.injtype == "2":
				ESC = self.ESC(mouse_strain)
				if ESC:
					os.system("open ESC.ics")
			
		elif self.strain == '3':
			mouse_strain = 'CD1'
			female_number = '15'

			if self.injtype == "1":
				CRISPR_type = input('Guide-test (1) or experiment (2)? ')
				if CRISPR_type == '1':
					CRISPR = self.CRISPR(False, False, mouse_strain, female_number)
					if CRISPR:
						os.system("open CRISPR.ics")
				
				elif CRISPR_type == '2':
					CRISPR = self.CRISPR(True, True, mouse_strain, female_number)
					if CRISPR:
						os.system("open crispr.ics")
			
				
			if self.injtype == "2":
				ESC = self.ESC(mouse_strain)
				if ESC:
					os.system("open ESC.ics")
=======
	def __init__(self, date, injtype, investigator_name):
		self.date = date
		self.injtype = injtype
		self.investigator_name = investigator_name

		if input('Enter mouse strain (B6:1, BDF:2, CD1:3) ') == '1':
			mouse_strain = 'B6'
			female_number = '15'
				
		elif '2':
			mouse_strain = 'BDF'
			female_number = '6'
			
		elif '3':
			mouse_strain = 'CD1'
			female_number = '15'

                if self.injtype == "1":
                        CRISPR_type = input('Guide-test (1) or experiment (2)? ')
                        if CRISPR_type == '1':
                                CRISPR = self.CRISPR(False, False, mouse_strain, female_number)
                                if CRISPR:
                                        os.system("open CRISPR.ics")

				
			elif CRISPR_type == '2':
				CRISPR = self.CRISPR(True, True, mouse_strain, female_number)
				if CRISPR:
					os.system("open crispr.ics")
			
				
		if self.injtype == "2":
			ESC = self.ESC()
			if ESC:
				os.system("open ESC.ics")
>>>>>>> 8caa6c9b7625619c9b78132e2aa8c9097f9dbc82

		

	def CRISPR(self, ET_value, pseudos, mouse_strain, female_number):
	

		date = datetime.strptime(self.date, '%m/%d/%Y')
		PMS = date - timedelta(days=3)
		HCG = date - timedelta(days=1)
		plugs = date
		tear = date
		ET = date

		splitPMS = PMS.strftime('%m/%d/%Y').split('/')
		splitHCG = HCG.strftime('%m/%d/%Y').split('/')
		splitPlugs = plugs.strftime('%m/%d/%Y').split('/')
		splitTear = tear.strftime('%m/%d/%Y').split('/')
		splitET = ET.strftime('%m/%d/%Y').split('/')
		splitInjection = date.strftime('%m/%d/%Y').split('/')

		event.add('summary', f'PMS {female_number} {mouse_strain} mice - RF')
		event.add('dtstart', datetime(int(splitPMS[2]),int(splitPMS[0]),int(splitPMS[1]),14,0,0,tzinfo=eastern))
		event.add('dtend', datetime(int(splitPMS[2]),int(splitPMS[0]),int(splitPMS[1]),15,0,0,tzinfo=eastern))
		cal.add_component(event)

		event2.add('summary', f'HCG + mate {female_number} {mouse_strain} mice - RF')
		event2.add('dtstart', datetime(int(splitHCG[2]),int(splitHCG[0]),int(splitHCG[1]),13,0,0,tzinfo=eastern))
		event2.add('dtend', datetime(int(splitHCG[2]),int(splitHCG[0]),int(splitHCG[1]),14,0,0,tzinfo=eastern))
		cal.add_component(event2)

		event3.add('summary', f'Check {mouse_strain} plugs - RF')
		event3.add('dtstart', datetime(int(splitPlugs[2]),int(splitPlugs[0]),int(splitPlugs[1]),8,0,0,tzinfo=eastern))
		event3.add('dtend', datetime(int(splitPlugs[2]),int(splitPlugs[0]),int(splitPlugs[1]),9,0,0,tzinfo=eastern))
		cal.add_component(event3)

		event4.add('summary', f'Tear {mouse_strain} embryos - ZH/NR')
		event4.add('dtstart', datetime(int(splitTear[2]),int(splitTear[0]),int(splitTear[1]),9,0,0,tzinfo=eastern))
		event4.add('dtend', datetime(int(splitTear[2]),int(splitTear[0]),int(splitTear[1]),10,0,0,tzinfo=eastern))
		cal.add_component(event4)

		if pseudos == True:
			event5.add('summary', 'Set pseudos - RF')
			event5.add('dtstart', datetime(int(splitHCG[2]),int(splitHCG[0]),int(splitHCG[1]),14,0,0,tzinfo=eastern))
			event5.add('dtend', datetime(int(splitHCG[2]),int(splitHCG[0]),int(splitHCG[1]),15,0,0,tzinfo=eastern))
			cal.add_component(event5)

			event6.add('summary', 'Check pseudos - RF')
			event6.add('dtstart', datetime(int(splitTear[2]),int(splitTear[0]),int(splitTear[1]),9,0,0,tzinfo=eastern))
			event6.add('dtend', datetime(int(splitTear[2]),int(splitTear[0]),int(splitTear[1]),10,0,0,tzinfo=eastern))
			cal.add_component(event6)

		if ET_value == True:
			event7.add('summary', f'e0.5 transfer for {self.investigator_name}')
			event7.add('dtstart', datetime(int(splitET[2]),int(splitET[0]),int(splitET[1]),13,0,0,tzinfo=eastern))
			event7.add('dtend', datetime(int(splitET[2]),int(splitET[0]),int(splitET[1]),15,0,0,tzinfo=eastern))
			cal.add_component(event7)
		
			crispr_name = f'CRISPR for {self.investigator_name}'
		else:
                        crispr_name = f'Guide-test for {self.investigator_name}'

		event8.add('summary', crispr_name)
		event8.add('dtstart', datetime(int(splitInjection[2]),int(splitInjection[0]),int(splitInjection[1]),10,0,0,tzinfo=eastern))
		event8.add('dtend', datetime(int(splitInjection[2]),int(splitInjection[0]),int(splitInjection[1]),12,0,0,tzinfo=eastern))
		cal.add_component(event8)

		f = open(os.path.join('./', 'crispr.ics'), 'wb')
		f.write(cal.to_ical())
		f.close()
		return True

	
<<<<<<< HEAD
	def ESC(self, strain):
=======
	def ESC(self):
>>>>>>> 8caa6c9b7625619c9b78132e2aa8c9097f9dbc82
		ESC = False
		inj_name = ''

		date = datetime.strptime(self.date, '%m/%d/%Y')
		PMS = date - timedelta(days=5)
		HCG = date - timedelta(days=3)
		plugs = date - timedelta(days=2)
		flush = date - timedelta(days=1)
		ET = date + timedelta(days=1)
		pseudos = date - timedelta(days=2)

		if input('8-cell (1) or blast (2) injection? ') == '2':

			inj_name = 'Blast'
			ET = date
			pseudos = date - timedelta(days=3)
			plugs = date - timedelta(days=3)
			HCG = date - timedelta(days=4)
			PMS = date - timedelta(days=6)
			flush = date - timedelta(days=2)

		elif '1':
			
			inj_name = '8-cell'
			pass

		splitPMS = PMS.strftime('%m/%d/%Y').split('/')
		splitHCG = HCG.strftime('%m/%d/%Y').split('/')
		splitPlugs = plugs.strftime('%m/%d/%Y').split('/')
		splitFlush = flush.strftime('%m/%d/%Y').split('/')
		splitET = ET.strftime('%m/%d/%Y').split('/')
		splitInjection = date.strftime('%m/%d/%Y').split('/')
		splitPsuedos = pseudos.strftime('%m/%d/%Y').split('/')

<<<<<<< HEAD
		event.add('summary', f'PMS {strain} mice')
=======
		event.add('summary', 'PMS CD1 mice')
>>>>>>> 8caa6c9b7625619c9b78132e2aa8c9097f9dbc82
		event.add('dtstart', datetime(int(splitPMS[2]),int(splitPMS[0]),int(splitPMS[1]),14,0,0,tzinfo=eastern))
		event.add('dtend', datetime(int(splitPMS[2]),int(splitPMS[0]),int(splitPMS[1]),15,0,0,tzinfo=eastern))
		cal.add_component(event)

<<<<<<< HEAD
		event2.add('summary', f'HCG + mate {strain} mice')
=======
		event2.add('summary', 'HCG + mate CD1 mice')
>>>>>>> 8caa6c9b7625619c9b78132e2aa8c9097f9dbc82
		event2.add('dtstart', datetime(int(splitHCG[2]),int(splitHCG[0]),int(splitHCG[1]),13,0,0,tzinfo=eastern))
		event2.add('dtend', datetime(int(splitHCG[2]),int(splitHCG[0]),int(splitHCG[1]),14,0,0,tzinfo=eastern))
		cal.add_component(event2)

<<<<<<< HEAD
		event3.add('summary', f'Check {strain} plugs')
=======
		event3.add('summary', 'Check CD1 plugs')
>>>>>>> 8caa6c9b7625619c9b78132e2aa8c9097f9dbc82
		event3.add('dtstart', datetime(int(splitPlugs[2]),int(splitPlugs[0]),int(splitPlugs[1]),8,0,0,tzinfo=eastern))
		event3.add('dtend', datetime(int(splitPlugs[2]),int(splitPlugs[0]),int(splitPlugs[1]),9,0,0,tzinfo=eastern))
		cal.add_component(event3)

<<<<<<< HEAD
		event4.add('summary', f'Flush {strain} two-cell embryos')
=======
		event4.add('summary', 'Flush CD1 two-cell embryos')
>>>>>>> 8caa6c9b7625619c9b78132e2aa8c9097f9dbc82
		event4.add('dtstart', datetime(int(splitFlush[2]),int(splitFlush[0]),int(splitFlush[1]),9,0,0,tzinfo=eastern))
		event4.add('dtend', datetime(int(splitFlush[2]),int(splitFlush[0]),int(splitFlush[1]),10,0,0,tzinfo=eastern))
		cal.add_component(event4)

		event5.add('summary', 'Set pseudos')
		event5.add('dtstart', datetime(int(splitPsuedos[2]),int(splitPsuedos[0]),int(splitPsuedos[1]),14,0,0,tzinfo=eastern))
		event5.add('dtend', datetime(int(splitPsuedos[2]),int(splitPsuedos[0]),int(splitPsuedos[1]),15,0,0,tzinfo=eastern))
		cal.add_component(event5)

		event6.add('summary', 'Check pseudos')
		event6.add('dtstart', datetime(int(splitFlush[2]),int(splitFlush[0]),int(splitFlush[1]),9,0,0,tzinfo=eastern))
		event6.add('dtend', datetime(int(splitFlush[2]),int(splitFlush[0]),int(splitFlush[1]),10,0,0,tzinfo=eastern))
		cal.add_component(event6)

		event7.add('summary', 'e2.5 blast transfer')
		event7.add('dtstart', datetime(int(splitET[2]),int(splitET[0]),int(splitET[1]),13,0,0,tzinfo=eastern))
		event7.add('dtend', datetime(int(splitET[2]),int(splitET[0]),int(splitET[1]),15,0,0,tzinfo=eastern))
		cal.add_component(event7)

		event8.add('summary', f'{inj_name} injection for {self.investigator_name}')
		event8.add('dtstart', datetime(int(splitInjection[2]),int(splitInjection[0]),int(splitInjection[1]),10,0,0,tzinfo=eastern))
		event8.add('dtend', datetime(int(splitInjection[2]),int(splitInjection[0]),int(splitInjection[1]),12,0,0,tzinfo=eastern))
		cal.add_component(event8)

		f = open(os.path.join('./', 'ESC.ics'), 'wb')
		f.write(cal.to_ical())
		f.close()

		return True

	

user_date = input("Input injection date ")
<<<<<<< HEAD
strain = input('Enter mouse strain (B6:1, BDF:2, CD1:3) ')
user_inj = input("Input injection type\n1 = CRISPR\n2 = ESC ")
user_investigator = input("Input name of investigator for injection ")
w = Week(user_date, strain, user_inj, user_investigator)
=======
user_inj = input("Input injection type\n1 = CRISPR\n2 = ESC ")
user_investigator = input("Input name of investigator for injection ")
w = Week(user_date, user_inj, user_investigator)
>>>>>>> 8caa6c9b7625619c9b78132e2aa8c9097f9dbc82

