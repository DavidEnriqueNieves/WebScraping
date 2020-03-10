import certifi
import unicodedata
import math
import re
import bs4 as bs
import urllib3

starlinks = ["https://en.wikipedia.org/wiki/Ross_248"
# ,"https://en.wikipedia.org/wiki/Alpha_Centauri"
# ,"https://en.wikipedia.org/wiki/Barnard%27s_Star"
# ,"https://en.wikipedia.org/wiki/Luhman_16"
# ,"https://en.wikipedia.org/wiki/WISE_0855%E2%88%920714"
# ,"https://en.wikipedia.org/wiki/Wolf_359"
# ,"https://en.wikipedia.org/wiki/Lalande_21185"
# ,"https://en.wikipedia.org/wiki/Sirius"
# ,"https://en.wikipedia.org/wiki/Luyten_726-8"
# ,"https://en.wikipedia.org/wiki/Ross_154"
# ,"https://en.wikipedia.org/wiki/Ross_248"
# ,"https://en.wikipedia.org/wiki/Epsilon_Eridani"
# ,"https://en.wikipedia.org/wiki/Epsilon_Eridani_b"
# ,"https://en.wikipedia.org/wiki/Lacaille_9352"
# ,"https://en.wikipedia.org/wiki/Ross_128"
# ,"https://en.wikipedia.org/wiki/Ross_128_b"
# ,"https://en.wikipedia.org/wiki/EZ_Aquarii"
# ,"https://en.wikipedia.org/wiki/61_Cygni"
# ,"https://en.wikipedia.org/wiki/Procyon"
# ,"https://en.wikipedia.org/wiki/Struve_2398"
# ,"https://en.wikipedia.org/wiki/Groombridge_34"
# ,"https://en.wikipedia.org/wiki/Gliese_15_Ab"
# ,"https://en.wikipedia.org/wiki/DX_Cancri"
# ,"https://en.wikipedia.org/wiki/Tau_Ceti"
# ,"https://en.wikipedia.org/wiki/Epsilon_Indi"
# ,"https://en.wikipedia.org/wiki/Gliese_1061"
# ,"https://en.wikipedia.org/wiki/YZ_Ceti"
# ,"https://en.wikipedia.org/wiki/Luyten%27s_Star"
# ,"https://en.wikipedia.org/wiki/Luyten_b"
# ,"https://en.wikipedia.org/wiki/Teegarden%27s_Star"
# ,"https://en.wikipedia.org/wiki/SCR_1845-6357"
# ,"https://en.wikipedia.org/wiki/Kapteyn%27s_Star"
# ,"https://en.wikipedia.org/wiki/Kapteyn_b"
# ,"https://en.wikipedia.org/wiki/Kapteyn_c"
# ,"https://en.wikipedia.org/wiki/Lacaille_8760"
# ,"https://en.wikipedia.org/wiki/Kruger_60"
# ,"https://en.wikipedia.org/wiki/DEN_1048-3956"
# ,"https://en.wikipedia.org/wiki/Ross_614"
# ,"https://en.wikipedia.org/wiki/Wolf_1061"
# ,"https://en.wikipedia.org/wiki/Wolf_1061b"
# ,"https://en.wikipedia.org/wiki/Wolf_1061_c"
# ,"https://en.wikipedia.org/wiki/Wolf_1061_d"
# ,"https://en.wikipedia.org/wiki/Wolf_424"
# ,"https://en.wikipedia.org/wiki/Van_Maanen_2"
# ,"https://en.wikipedia.org/wiki/Gliese_1"
# ,"https://en.wikipedia.org/wiki/L_1159-16"
# ,"https://en.wikipedia.org/wiki/Gliese_674"
# ,"https://en.wikipedia.org/wiki/Gliese_687"
# ,"https://en.wikipedia.org/wiki/LHS_292"
# ,"https://en.wikipedia.org/wiki/LP_145-141"
# ,"https://en.wikipedia.org/wiki/GJ_1245"
# ,"https://en.wikipedia.org/wiki/Gliese_876"
# ,"https://en.wikipedia.org/wiki/Gliese_876_d"
# ,"https://en.wikipedia.org/wiki/Gliese_876_c"
# ,"https://en.wikipedia.org/wiki/Gliese_876_b"
# ,"https://en.wikipedia.org/wiki/Gliese_876_e"
# ,"https://en.wikipedia.org/wiki/LHS_288"
# ,"https://en.wikipedia.org/wiki/GJ_1002"
# ,"https://en.wikipedia.org/wiki/Groombridge_1618"
# ,"https://en.wikipedia.org/wiki/DEN_0255-4700"
# ,"https://en.wikipedia.org/wiki/Gliese_412"
# ,"https://en.wikipedia.org/wiki/Gliese_832"
# ,"https://en.wikipedia.org/wiki/Gliese_832_c"
# ,"https://en.wikipedia.org/wiki/Gliese_832_b"
# ,"https://en.wikipedia.org/wiki/AD_Leonis"
# ,"https://en.wikipedia.org/wiki/GJ_1005"
# ,"https://en.wikipedia.org/wiki/LP_944-20"
# ,"https://en.wikipedia.org/wiki/40_Eridani"
# ,"https://en.wikipedia.org/wiki/EV_Lacertae"
# ,"https://en.wikipedia.org/wiki/Gliese_682"
# ,"https://en.wikipedia.org/wiki/Gliese_682_c"
# ,"https://en.wikipedia.org/wiki/70_Ophiuchi"
# ,"https://en.wikipedia.org/wiki/Altair"
# ,"https://en.wikipedia.org/wiki/G_9-38"
# ,"https://en.wikipedia.org/wiki/GJ_3379"
# ,"https://en.wikipedia.org/wiki/LHS_1723"
# ,"https://en.wikipedia.org/wiki/2MASS_0939-2448"
# ,"https://en.wikipedia.org/wiki/Gliese_445"
# ,"https://en.wikipedia.org/wiki/GJ_526"
# ,"https://en.wikipedia.org/wiki/Stein_2051"
# ,"https://en.wikipedia.org/wiki/Gliese_251"
# ,"https://en.wikipedia.org/wiki/Gliese_205"
# ,"https://en.wikipedia.org/wiki/LP_816-60"
# ,"https://en.wikipedia.org/wiki/2MASS_J04151954-0935066"
# ,"https://en.wikipedia.org/wiki/Sigma_Draconis"
# ,"https://en.wikipedia.org/wiki/Gliese_299"
# ,"https://en.wikipedia.org/wiki/Ross_47"
# ,"https://en.wikipedia.org/wiki/Gliese_693"
# ,"https://en.wikipedia.org/wiki/Gliese_752"
# ,"https://en.wikipedia.org/wiki/Gliese_570"
# ,"https://en.wikipedia.org/wiki/Gliese_588"
# ,"https://en.wikipedia.org/wiki/Eta_Cassiopeiae"
# ,"https://en.wikipedia.org/wiki/36_Ophiuchi"
# ,"https://en.wikipedia.org/wiki/Gliese_908"
# ,"https://en.wikipedia.org/wiki/YZ_Canis_Minoris"
# ,"https://en.wikipedia.org/wiki/HR_7703"
# ,"https://en.wikipedia.org/wiki/82_G._Eridani"
# ,"https://en.wikipedia.org/wiki/G_240-72"
# ,"https://en.wikipedia.org/wiki/ADS_7251"
# ,"https://en.wikipedia.org/wiki/Delta_Pavonis"
# ,"https://en.wikipedia.org/wiki/Gliese_268"
# ,"https://en.wikipedia.org/wiki/2MASSI_J0937347%2B293142"
# ,"https://en.wikipedia.org/wiki/Gliese_784"
# ,"https://en.wikipedia.org/wiki/Gliese_555"
# ,"https://en.wikipedia.org/wiki/EQ_Pegasi"
# ,"https://en.wikipedia.org/wiki/Gliese_581"
# ,"https://en.wikipedia.org/wiki/Gliese_581_e"
# ,"https://en.wikipedia.org/wiki/Gliese_581_b"
# ,"https://en.wikipedia.org/wiki/Gliese_581_c"
# ,"https://en.wikipedia.org/wiki/Gliese_581_g"
# ,"https://en.wikipedia.org/wiki/Gliese_581_d"
# ,"https://en.wikipedia.org/wiki/LHS_2090"
# ,"https://en.wikipedia.org/wiki/GJ_3737"
# ,"https://en.wikipedia.org/wiki/Furuhjelm_46"
# ,"https://en.wikipedia.org/wiki/LP_658-2"
# ,"https://en.wikipedia.org/wiki/V1054_Ophiuchi"
]

# http = urllib3.PoolManager(10)
# sauce = http.request('GET', starlinks[0]).data
# soup = bs.BeautifulSoup(sauce, features="html.parser")

# stardata=list()


def gothroughurls(urllist):
	mult_star_data=list()
	for i in range(len(urllist)):
		numberFails=0
		mult_star_data.append([])
		http = urllib3.PoolManager(10, cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
		sauce = http.request('GET', urllist[i-1]).data
		soup = bs.BeautifulSoup(sauce, features="html.parser")
		name = soup.find('h1', id="firstHeading").string
		Data = get_RA_DEC_DIST(soup)
		if(Data==None):
			numberFails+=1
			continue
		mult_star_data[i].append(RAToRadians(Data))
		mult_star_data[i].append(DECToRadians(Data))
		mult_star_data[i].append(GetDistance(Data))
		mult_star_data[i].append(name)
		print(mult_star_data[::-1])
	print("")
	print("{##########################}")
	print("Number of Fails", numberFails)
	print("{##########################}")
	# for j in range(len(mult_star_data)-1):
	# 	print("------------------------------")
	# 	u=0
	# 	for u in range(4):
	# 		print(mult_star_data[j][u])










def get_RA_DEC_DIST(soup):
	print("GETTING DATA")
	stardata=list()
	name = soup.find('h1', id="firstHeading").string
	if(soup.table.tbody.find(string=re.compile("Right ascension")).parent.parent.parent.parent.find('td')==None):
		print("NoneType Found for", name)
		return None
####MAKE IT SO THAT YOU SEARCH FOR THE RA AND THE DEC USING THE SUMBOLS OR THE \xa0 SYMBOLS IN UNICODE USING
####STRING=re.compile("\Xa0")
	print(soup.table.tbody.find(string=re.compile("Right ascension")))
	print(soup.table.tbody.find(string=re.compile("Right ascension")).parent.parent.parent.parent.find('td').get_text())
	stardata.append(soup.table.tbody.find(string=re.compile("Right ascension")).parent.parent.parent.parent.find('td').get_text())
	print(soup.table.tbody.find(string=re.compile("Declination")))
	if(soup.table.tbody.find(string=re.compile("Declination")).parent.parent.parent.find('td')==None):
		print("NoneType Found for", name)
		return None
	stardata.append(soup.table.tbody.find(string=re.compile("Declination")).parent.parent.parent.find('td').get_text())
	print(soup.table.tbody.find(string=re.compile("Distance")))
	print(soup.table.tbody.find(string=re.compile("Distance")).parent.parent.parent.next_sibling.get_text())
	if(soup.table.tbody.find(string=re.compile("Distance")).parent.parent.parent.next_sibling==None):
		print("NoneType Found for", name)
		return None
	stardata.append(soup.table.tbody.find(string=re.compile("Distance")).parent.parent.parent.next_sibling.get_text())
	AsciiData=list()
	AsciiData.append(ascii(stardata[0]))
	AsciiData.append(ascii(stardata[1]))
	AsciiData.append(ascii(stardata[2]))
	AsciiData.append(name)
	print("Name",name)
	print("Right Ascension", AsciiData[0])
	print("Declination", AsciiData[1])
	print("Distance", AsciiData[2])
	return AsciiData


# print("|||||||||||||||||||||||||||||||||||||||")
# print(soup.table.tbody.find(string=re.compile("Right ascension")))
# print(soup.table.tbody.find(string=re.compile("Right ascension")).parent.parent.parent.parent.find('td').get_text())
# stardata.append(soup.table.tbody.find(string=re.compile("Right ascension")).parent.parent.parent.parent.find('td').get_text())
# print(soup.table.tbody.find(string=re.compile("Declination")))
# stardata.append(soup.table.tbody.find(string=re.compile("Declination")).parent.parent.parent.find('td').get_text())
# print(soup.table.tbody.find(string=re.compile("Distance")))
# print(soup.table.tbody.find(string=re.compile("Distance")).parent.parent.parent.next_sibling.get_text())
# stardata.append(soup.table.tbody.find(string=re.compile("Distance")).parent.parent.parent.next_sibling.get_text())

# print(stardata[0])
# print("STRIPPED")
# print(ascii(stardata[0]).strip("\\xao"))
# AsciiData=list()
# AsciiData.append(ascii(stardata[0]))
# AsciiData.append(ascii(stardata[1]))
# AsciiData.append(ascii(stardata[2]))


def RAToRadians(AsciiData):
	hours=float(AsciiData[0][1:3])
	print("Hours", hours)
	minutes=float(AsciiData[0][8:10])
	print("Minutes", minutes)
	seconds = float(AsciiData[0][15:20])
	print("Seconds", seconds)
	print(((hours)*(math.pi/12))+(minutes*(math.pi/(720)))+(seconds*(math.pi/(43200))))
	return (((hours)*(math.pi/12))+(minutes*(math.pi/(720)))+(seconds*(math.pi/(43200))))

def DECToRadians(AsciiData):
	# if (AsciiData[1][1]=='-'):
	if(AsciiData[1][1]=='\\'):
		print("HAS A NEGATIVE SIGN")
		Degrees=float(AsciiData[1][7:9])
		print("Degrees", Degrees)
		Minutes=float(AsciiData[1][17:19])
		print("Minutes",Minutes)
		Seconds=float(AsciiData[1][29:31])
		print("Seconds",Seconds)
		print((((Degrees)*(math.pi/180))+(Minutes*(math.pi/(720)))+(Seconds*(math.pi/(43200))))*(-1))
		return ((((Degrees)*(math.pi/180))+(Minutes*(math.pi/(720)))+(Seconds*(math.pi/(43200))))*(-1))
	Degrees=float(AsciiData[1][2:4])
	print(Degrees)
	Minutes=float(AsciiData[1][12:14])
	print(Minutes)
	Seconds=float(AsciiData[1][24:28])
	print(Seconds)
	print((((Degrees)*(math.pi/180))+(Minutes*(math.pi/(720)))+(Seconds*(math.pi/(43200)))))
	return (((Degrees)*(math.pi/180))+(Minutes*(math.pi/(720)))+(Seconds*(math.pi/(43200))))

def GetDistance(AsciiData):
	x=0
	distanceNum=""
	while(AsciiData[2][x]!="\\"):
		distanceNum=AsciiData[2][x]+distanceNum
		x+=1
	result=distanceNum[::-1]
	result=result.strip("'")
	if(result[0]=="'"):
		result = str.lstrip(result)
	result=float(result)
	print("Distance in Light Years",result)
	return result

print("Index for list is" )
print("0 - Right Ascension")
print("1 - Declination")
print("2 - Distance")
print("4 - Name")

gothroughurls(starlinks)