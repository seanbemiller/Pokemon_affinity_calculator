import json
# need to manually add quotes around: stats
 
with open('./output.json','a') as out:
	with open('./learnsets.ts') as f:
		line = f.readline()
		while(True):
			last = line
			line = f.readline()
			if ('learnset: {' in line):
				out.write('\n' + last.strip())
				while '},' not in line:
					line = f.readline()
					newline = line.split(":")
					out.write(newline[0].strip() + ', ')


# with open('./output.json') as f:
#   data = json.load(f)

# # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# for item in data:
#   print(item)