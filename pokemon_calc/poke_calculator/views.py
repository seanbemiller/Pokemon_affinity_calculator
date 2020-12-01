from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
from .forms import selectForm, secondForm
from django.contrib.messages import get_messages
from django.contrib import messages
import sqlite3


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

#example pokemon export string
export_example = 'Kyurem-Black @ Leftovers\nAbility: Teravolt\nEVs: 252 Atk / 4 SpA / 252 Spe\nNaive Nature\n- Dragon Dance\n- Icicle Spear\n- Earth Power\n- Fusion Bolt'
export_string = [export_example, export_example, export_example, export_example, export_example, export_example ]

# Create your views here.
def home(request): 
	conn = sqlite3.connect('pokemon_data.sqlite')
	c = conn.cursor()
	# GET POKEMON TEAM FROM DB HERE
	# for row in c.execute('SELECT name, type1 FROM pokemon '):
	# 	print(row)
	conn.close()
	if(request.POST):
		form = selectForm(request.POST)
		context = {
		'pokeselected': True,
		'form': form,
		'pokemonTeam': pokemon,
		'pokedex': pokemon
		}
		if form.is_valid() == False:
			context['form'] = selectForm()
			return render(request, 'poke_calculator/home.html', context=context)
		
		if 'submit' in request.POST:
			messages.add_message(request, messages.INFO, form.cleaned_data['pokemon'])
			return redirect('Pokemon-Calculator-Select')
		elif 'export' in request.POST:
			# CREATE LIST OF STRINGS TO BE EXPORTED HERE
			for string in export_string:
				messages.add_message(request, messages.INFO, string)
			return redirect('Pokemon-Calculator-Export')

	else:
		form = selectForm()
		context = {
		'pokeselected': False,
		'form': form,
		'pokemonTeam': pokemon,
		'pokedex': pokemon
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
		sform = secondForm(request.POST)
		context['sform'] = sform
		if sform.is_valid():
			move1 = sform.cleaned_data['Move1']
			move2 = sform.cleaned_data['Move2']
			move3 = sform.cleaned_data['Move3']
			move4 = sform.cleaned_data['Move4']
			item = sform.cleaned_data['Item']

			print(chosenPoke, move1, move2, move3, move4, item)
			# add pokemon + moves to team db here -=-=--=-=-==-=-=-=-=-=-=
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


def export(request):
	return render(request,'poke_calculator/export.html')
