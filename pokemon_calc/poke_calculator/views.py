from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from .forms import selectForm, secondForm, thirdForm, fourthForm, findForm
from django.contrib.messages import get_messages
from django.contrib import messages
import sqlite3
import import_export as inout
import defense_type_chart as typecalc
import team_builder as teamMaker

#example pokemon dictionary 
pokemon = [
	{
		'name': 'pikachu',
		'type1': 'electric',
		'type2': 'NULL',
		'atr1': 'Static',
		'atr2': 'Lightning Rod'
	},
	{
		'name': 'charazard',
		'type1': 'fire',
		'type2': 'flying',
		'atr1': 'Blaze',
		'atr2': 'Solar Power'
	}
]

# Create your views here.
def home(request): 
	Team = []
	newTeam = []
	conn = sqlite3.connect('pokemon_data.sqlite')
	c = conn.cursor()
	for row in c.execute('SELECT * FROM Team '): #populate team list
		Team.append(row)
	if not Team:
		pokemon=''
	for pokemon in Team:
		# print(pokemon)
		tup = inout.importer(pokemon[0])
		newTeam.append({
		'name': tup[0],
		'item': tup[1],
		'nature': tup[2],
		'ability': tup[3],
		'move1': tup[4],
		'move2': tup[5],
		'move3': tup[6],
		'move4': tup[7]
		})
	statList = []
	for p in newTeam:
		c.execute('SELECT hp, atk, def, spa, spd, spe FROM Pokemon WHERE name="{}"'.format(p['name']))
		data = c.fetchone()
		statList.append(data)
	hp = 0
	atk = 0
	defense = 0
	spa = 0
	spd  = 0
	spe = 0

	print(newTeam)

	print(statList)
	if len(statList) > 0:
		for i in statList:
			hp += int(i[0])
			atk += int(i[1])
			defense += int(i[2])
			spa += int(i[3])
			spd += int(i[4])
			spe += int(i[5])
		hp = hp / len(statList)
		atk = atk/ len(statList)
		defense = defense / len(statList)
		spa = spa / len(statList)
		spd = spd / len(statList)
		spe = spe / len(statList)
	statDict = {
		'hp':hp,
		'atk':atk,
		'def':defense,
		'spa':spa,
		'spd':spd,
		'spe':spe
	}
	teamTypeList = []
	finalList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for pokemon in newTeam:
		c.execute('SELECT type1, type2 FROM pokemon WHERE name="{}"'.format(pokemon['name']))
		teamTypeList.append(c.fetchone())
	for pokemon in teamTypeList:
		data = typecalc.def_type_calc(pokemon[0].lower(), pokemon[1].lower())
		for i in range(0,17):
			finalList[i] += data[i]

	typing = {
		'nor':finalList[0],
		'fly':finalList[1],
		'poi':finalList[2],
		'fig':finalList[3],
		'grd':finalList[4],
		'rck':finalList[5],
		'bug':finalList[6],
		'ght':finalList[7],
		'stl':finalList[8],
		'fir':finalList[9],
		'wat':finalList[10],
		'grs':finalList[11],
		'elc':finalList[12],
		'psy':finalList[13],
		'ice':finalList[14],
		'drg':finalList[15],
		'drk':finalList[16],
		'fry':finalList[17]
	}
	conn.close()
	if(request.POST):
		form = selectForm(request.POST)
		context = {
		'pokeselected': True,
		'form': form,
		'pokemonTeam': newTeam,
		'pokedex': pokemon,
		'stats':statDict,
		'typing':typing
		}
		if form.is_valid() == False:
			context['form'] = selectForm()
			return render(request, 'poke_calculator/home.html', context=context)
		
		if 'submit' in request.POST:
			messages.add_message(request, messages.INFO, form.cleaned_data['pokemon'])
			return redirect('Pokemon-Calculator-Select')
		elif 'remove' in request.POST:
			return redirect('Pokemon-Calculator-Remove')
		elif 'find' in request.POST:
			return redirect('Pokemon-Calculator-Find')
		elif 'swap' in request.POST:
			return redirect('Pokemon-Calculator-Swap')
		elif 'buildPOKETEAM' in request.POST:
			print("MAKING TEAM NOW")
			conn = sqlite3.connect('pokemon_data.sqlite')
			c = conn.cursor()
			c.execute('SELECT type1, type2 FROM pokemon WHERE name="{}"'.format(newTeam[0]['name']))
			data = c.fetchone()
			toAdd = teamMaker.buildTeam(data[0].lower(), data[1].lower())
			for poke in toAdd:
				c.execute('INSERT INTO Team VALUES (?)', (poke,))
			conn.commit()
			# # print(toAdd)
			return redirect('Pokemon-Calculator-Home')
			# return render(request,'poke_calculator/home.html')
		elif 'export' in request.POST:
			#example pokemon export string
			# export_example = 'Kyurem-Black @ Leftovers\nAbility: Teravolt\nEVs: 252 Atk / 4 SpA / 252 Spe\nNaive Nature\n- Dragon Dance\n- Icicle Spear\n- Earth Power\n- Fusion Bolt'
			export_string = []
			# CREATE LIST OF STRINGS TO BE EXPORTED HERE
			conn = sqlite3.connect('pokemon_data.sqlite')
			c = conn.cursor()
			for row in c.execute('SELECT * FROM Team '): #populate team list
				export_string.append(row[0])
			for string in export_string:
				messages.add_message(request, messages.INFO, string)
			return redirect('Pokemon-Calculator-Export')

	else:
		form = selectForm()
		context = {
		'pokeselected': False,
		'form': form,
		'pokemonTeam': newTeam,
		'stats':statDict,
		'pokedex': pokemon,
		'typing':typing
		}
	return render(request,'poke_calculator/home.html', context)


def selectPoke(request):
	chosenPoke = ''
	storage = get_messages(request)
	for message in storage:
		chosenPoke = message
	context = {
		'pokeselected': True,
		'selected': chosenPoke
	}
	if(request.POST):
		print('IS A POST')
		sform = secondForm(request.POST)
		context['sform'] = sform
		if sform.is_valid():
			move1 = sform.cleaned_data['Move1']
			move2 = sform.cleaned_data['Move2']
			move3 = sform.cleaned_data['Move3']
			move4 = sform.cleaned_data['Move4']
			item = sform.cleaned_data['Item']
			ability = sform.cleaned_data['Ability']
			nature = sform.cleaned_data['Nature']
			Poke_str = inout.exporter(chosenPoke.__str__(), ability, item, nature, move1, move2, move3, move4)
			conn = sqlite3.connect('pokemon_data.sqlite')
			c = conn.cursor()
			print((Poke_str[:-1],))
			c.execute('INSERT INTO Team VALUES (?)', (Poke_str[:-1],))
			pokemon_data = c.fetchone() #get pokemon data as tuple 
			conn.commit()
			conn.close()
			return redirect('Pokemon-Calculator-Home')
		else:
			print('NOT VALID')
	else:
			conn = sqlite3.connect('pokemon_data.sqlite')
			c = conn.cursor()
			c.execute('SELECT * FROM Pokemon WHERE name="{}"'.format(chosenPoke.__str__()))
			pokemon_data = c.fetchone() #get pokemon data as tuple 
			conn.commit()
			conn.close()
			pokemon_discript = ('name','type1','type2','hp','atk','def','spa','spd','spe','ability1','ability2','ability3','avalible moves')
			combined = []
			for data, discrip in zip(pokemon_data, pokemon_discript):
				combined.append(discrip + ': ' + data.__str__())
			context['pokemon_data'] = combined
			sform = secondForm()
			context['sform'] = sform
			messages.add_message(request, messages.INFO, chosenPoke) #resend pokemon as message
			return render(request,'poke_calculator/selectPoke.html', context)

def removePoke(request):
	context = {}
	if(request.POST):
		tform = thirdForm(request.POST)
		context['tform'] = tform
		if tform.is_valid():
			ToRemove = ''
			ToRemove = tform.cleaned_data['toRemove']
			print(ToRemove)
			conn = sqlite3.connect('pokemon_data.sqlite')
			c = conn.cursor()
			c.execute('DELETE FROM Team WHERE pokemon like "{}%"'.format(ToRemove))
			conn.commit()
			conn.close()
			return redirect('Pokemon-Calculator-Home')
		else:
			print('NOT VALID')
			# return redirect('Pokemon-Calculator-Home')
	else:	
		tform = thirdForm()
		context['tform'] = tform
	return render(request,'poke_calculator/remove.html', context=context)

def swapPoke(request):
	context = {}
	if(request.POST):
		fform = fourthForm(request.POST)
		context['fform'] = fform
		if fform.is_valid():
			ToSwap = ''
			ToSwap = fform.cleaned_data['toSwap']
			newPoke = fform.cleaned_data['replacement']
			conn = sqlite3.connect('pokemon_data.sqlite')
			c = conn.cursor()
			print(ToSwap + " " + newPoke)
			c.execute('UPDATE Team SET pokemon="{}" where pokemon like "{}%"'.format(newPoke, ToSwap))
			conn.commit()
			conn.close()
			return redirect('Pokemon-Calculator-Home')
		else:
			print('NOT VALID')
			# return redirect('Pokemon-Calculator-Home')
	else:	
		fform = fourthForm()
		context['fform'] = fform
	return render(request,'poke_calculator/swap.html', context=context)

def findPoke(request):
	context = {}
	if(request.POST):
		fform = findForm(request.POST)
		context['fform'] = fform
		if fform.is_valid():
			Type1 = fform.cleaned_data['Type1']
			Type2 = fform.cleaned_data['Type2']
			conn = sqlite3.connect('pokemon_data.sqlite')
			c = conn.cursor()
			c.execute('CREATE VIEW v1 AS SELECT name FROM pokemon WHERE type1="{}" OR type2="{}"'.format(Type1, Type1,))
			if Type2 != '':
				c.execute('CREATE VIEW v2 AS SELECT name FROM pokemon WHERE type1="{}" OR type2="{}"'.format(Type2, Type2,))
				c.execute('SELECT * FROM v1 UNION SELECT * FROM v2')
			result = c.fetchall()
			c.execute('DROP VIEW v1')
			c.execute('DROP VIEW v2')
			conn.close()
			toSend = ''
			for i in result:
				toSend += (i[0].__str__() + "\n")
			print(toSend)
			messages.add_message(request, messages.INFO, toSend)
			return redirect('Pokemon-Calculator-Match')
		else:
			print('NOT VALID')
			# return redirect('Pokemon-Calculator-Home')
	else:	
		fform = findForm()
		context['fform'] = fform
	return render(request,'poke_calculator/swap.html', context=context)

def matchPoke(request):
	return render(request,'poke_calculator/match.html')

def export(request):
	return render(request,'poke_calculator/export.html')
