import json
# BASIC CLEAN UP - WENT BACK AND MANUALLY TOUCHED UP
# with open('./output.json','a') as out:
#   with open('./moves.ts') as f:
#     while(True):
#       line = f.readline()
#       if ('category' in line):
#         out.write('{\n'+ line)
#       elif ('name' in line):
#         out.write(line)
#       elif ('type' in line):
#         out.write(line +'},\n')

with open('./output.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for item in data:
  print(item)