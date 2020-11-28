import json
# need to manually add quotes around: stats
 
# with open('./output.json','a') as out:
# 	with open('./pokedex_base_file') as f:
# 		while(True):
# 			line = f.readline()
# 			if ('name' in line):
# 				line = line.replace("name", "\"name\"")
# 				out.write('{\n'+ line)
				
# 			elif ('types: ' in line):
# 				line = line[10:-3]
# 				linecut = line.split(',')
# 				index = 1
# 				for type in linecut:
# 					out.write("\t\t\"type{}\": {},\n".format(index, type))
# 					index += 1
# 			elif ('baseStats: ' in line):
# 				line = line[14:-3]
# 				linecut = line.split(',')
# 				for stat in linecut:
# 					out.write("\t\t{},\n".format(stat.strip()))
# 			elif ('abilities: ' in line):
# 				line = line[14:-3]
# 				line = line.replace("0: ", " ").replace("1: ", " ").replace("H: ", " ")
# 				linecut = line.split(',')
# 				index = 1
# 				for ability in linecut:
# 					out.write("\t\t\"ability{}\": {},\n".format(index, ability.strip()))
# 					index += 1
				
# 				out.write("\t\t\"moveset\": \n},\n")

with open('./output.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for item in data:
  print(item)