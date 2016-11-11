import json

res = []

with open("emoji.json") as f:
	# x = f.read()
	emojis = json.load(f)
	# print (x)
	print (len(emojis))
	
	# print emojis[0]
	for emoji in emojis:
		dic = []
		dic.append(emoji["aliases"][0]+"\t"+emoji["emoji"])
		dic.append(emoji["emoji"])
		res.append(dic)
with open("me.json","w") as f:
	json.dump(res,f)