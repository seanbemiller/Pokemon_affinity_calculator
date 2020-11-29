import json
# # BASIC CLEAN UP - WENT BACK AND MANUALLY TOUCHED UP
# with open('./output.json','a') as out:
#   with open('./items.ts') as f:
#     while(True):
#       line = f.readline()
#       if ('name: ' in line):
#         out.write('{\n'+ line + '},\n')

with open('./output.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for item in data:
  print(item)