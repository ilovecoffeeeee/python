
holiday = {'lee':['0707', '0718', '0815'], 'kim':['0815', '1211', '1215', '1225'], 'park':['0322','0718', '0815', '1225']}

def day_off(person_date):
	
	people = []
	dates = []

	for person, date in person_date.items():
		people.append(person)
		dates = dates + date

	date_person = {}
	
	for date in dates:
		date_person[date] = []
		
	for person in people:
		for date in person_date[person]:
			date_person.setdefault(date, []).append(person)
			date_person[date].sort()
	
	date_person = dict(sorted(date_person.items(), key=lambda  x: x[0]))
	
	return date_person
	
print(day_off(holiday))


