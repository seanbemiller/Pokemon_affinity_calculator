from django import forms
from django.contrib.messages import get_messages
from django.contrib import messages
import sqlite3

class selectForm(forms.Form): # replace with list of pokemon 
	pokeList = []
	conn = sqlite3.connect('pokemon_data.sqlite')
	c = conn.cursor()
	for row in c.execute('SELECT name FROM pokemon '):
		pokeList.append((row[0], row[0]))
	pokemon = forms.ChoiceField(choices=pokeList)
	conn.close()

# class secondForm(forms.Form):
# 	def __init__(self, round_list, *args, **kwargs):
# 		super(secondForm, self).__init__(*args, **kwargs)
# 		self.fields['move1'] = forms.ChoiceField(choices=tuple([(name, name) for name in round_list]))


class secondForm(forms.Form):
	itemList = [('', '')]
	moveList = [('', '')]
	conn = sqlite3.connect('pokemon_data.sqlite')
	c = conn.cursor()
	for row in c.execute('SELECT name FROM items '): #populate item list
		itemList.append((row[0], row[0]))
	c.execute('SELECT name FROM Moves ORDER BY name ASC', )
	data = c.fetchall()
	for i in data:
		moveList.append((i[0], i[0]))
	# for row in c.execute('SELECT name FROM moves '): #populate moves list
	# 	moveList.append((row[0], row[0]))
	conn.commit()
	conn.close()
	Move1 = forms.ChoiceField(choices=moveList)
	Move2 = forms.ChoiceField(choices=moveList)
	Move3 = forms.ChoiceField(choices=moveList)
	Move4 = forms.ChoiceField(choices=moveList)
	Item = forms.ChoiceField(choices=itemList)