import xml.etree.ElementTree as ET
tree = ET.parse('lab.html')
root = tree.getroot()
tbody= root.find('tbody')
with open('output.txt',mode ='w', encoding="UTF-8") as output:
	for tr in tbody.findall('tr'):
		for i,td in enumerate(tr.findall('td')):
			if i in (0,6):
				output.write(td.text+' , ')
			else:
				a = td.find('a')
				output.write(a.text+' , ')
		output.write('\n')