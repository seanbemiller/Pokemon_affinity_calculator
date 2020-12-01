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
	abilList = [('', '')]
	natList = [('', '')]
	conn = sqlite3.connect('pokemon_data.sqlite')
	c = conn.cursor()
	for row in c.execute('SELECT name FROM items '): #populate item list
		itemList.append((row[0], row[0]))
	c.execute('SELECT name FROM Moves ORDER BY name ASC', ) #populate moves list in alphabetical
	data = c.fetchall()
	for i in data:
		moveList.append((i[0], i[0]))
	c.execute('SELECT DISTINCT ability1 FROM pokemon ORDER BY name ASC', ) #populate moves list in alphabetical
	data1 = c.fetchall()
	c.execute('SELECT DISTINCT ability2 FROM pokemon ORDER BY name ASC', ) #populate moves list in alphabetical
	data2 = c.fetchall()
	c.execute('SELECT DISTINCT ability3 FROM pokemon ORDER BY name ASC', ) #populate moves list in alphabetical
	data3 = c.fetchall()
	for i in data1:
		abilList.append((i[0], i[0]))
	for i in data2:
		abilList.append((i[0], i[0]))
	for i in data3:
		abilList.append((i[0], i[0]))
	# for row in c.execute('SELECT name FROM moves '): #populate moves list
	# 	moveList.append((row[0], row[0]))
	conn.commit()
	conn.close()
	natures = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax",
    "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash",
    "Calm", "Gentle", "Sassy", "Careful", "Quirky"]
	for item in natures:
		natList.append((item, item))
	Move1 = forms.ChoiceField(choices=moveList)
	Move2 = forms.ChoiceField(choices=moveList)
	Move3 = forms.ChoiceField(choices=moveList)
	Move4 = forms.ChoiceField(choices=moveList)
	Ability = forms.ChoiceField(choices=abilList)
	Nature = forms.ChoiceField(choices=natList)
	Item = forms.ChoiceField(choices=itemList)