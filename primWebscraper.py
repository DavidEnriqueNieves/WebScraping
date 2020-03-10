
import bs4 as bs
import urllib3

import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet("Sheet1",cell_overwrite_ok=True)


# for tr in soup2.table.tbody:
# 	soup2.table.tbody.tr.contents
#THIS SOMEWHAT WORKS DO NOT DELETE
# for child in soup2.table.tbody.tr.children:
# 	for string in soup2.table.tbody.stripped_strings:
# 		print(repr(string))




# for child in soup2.table.tbody.descendants:
# 	for string in soup2.table.tbody.stripped_strings:
# 		print(string)


extra_starlinks = ["https://en.wikipedia.org/wiki/Sun", 
"https://en.wikipedia.org/wiki/Mercury_(planet)"
,"https://en.wikipedia.org/wiki/Venus"
,"https://en.wikipedia.org/wiki/Earth"
,"https://en.wikipedia.org/wiki/Mars"
,"https://en.wikipedia.org/wiki/Jupiter"
,"https://en.wikipedia.org/wiki/Saturn"
,"https://en.wikipedia.org/wiki/Uranus"
,"https://en.wikipedia.org/wiki/Neptune"
,"https://en.wikipedia.org/wiki/Pluto"
,"https://en.wikipedia.org/wiki/Charon_(moon)"]


starlinks = ["https://en.wikipedia.org/wiki/Proxima_Centauri"
,"https://en.wikipedia.org/wiki/Proxima_Centauri_b"
,"https://en.wikipedia.org/wiki/Alpha_Centauri"
,"https://en.wikipedia.org/wiki/Barnard%27s_Star"
,"https://en.wikipedia.org/wiki/Luhman_16"
,"https://en.wikipedia.org/wiki/WISE_0855%E2%88%920714"
,"https://en.wikipedia.org/wiki/Wolf_359"
,"https://en.wikipedia.org/wiki/Lalande_21185"
,"https://en.wikipedia.org/wiki/Sirius"
,"https://en.wikipedia.org/wiki/Luyten_726-8"
,"https://en.wikipedia.org/wiki/Ross_154"
,"https://en.wikipedia.org/wiki/Ross_248"
,"https://en.wikipedia.org/wiki/Epsilon_Eridani"
,"https://en.wikipedia.org/wiki/Epsilon_Eridani_b"
,"https://en.wikipedia.org/wiki/Lacaille_9352"
,"https://en.wikipedia.org/wiki/Ross_128"
,"https://en.wikipedia.org/wiki/Ross_128_b"
,"https://en.wikipedia.org/wiki/EZ_Aquarii"
,"https://en.wikipedia.org/wiki/61_Cygni"
,"https://en.wikipedia.org/wiki/Procyon"
,"https://en.wikipedia.org/wiki/Struve_2398"
,"https://en.wikipedia.org/wiki/Groombridge_34"
,"https://en.wikipedia.org/wiki/Gliese_15_Ab"
,"https://en.wikipedia.org/wiki/DX_Cancri"
,"https://en.wikipedia.org/wiki/Tau_Ceti"
,"https://en.wikipedia.org/wiki/Epsilon_Indi"
,"https://en.wikipedia.org/wiki/Gliese_1061"
,"https://en.wikipedia.org/wiki/YZ_Ceti"
,"https://en.wikipedia.org/wiki/Luyten%27s_Star"
,"https://en.wikipedia.org/wiki/Luyten_b"
,"https://en.wikipedia.org/wiki/Teegarden%27s_Star"
,"https://en.wikipedia.org/wiki/SCR_1845-6357"
,"https://en.wikipedia.org/wiki/Kapteyn%27s_Star"
,"https://en.wikipedia.org/wiki/Kapteyn_b"
,"https://en.wikipedia.org/wiki/Kapteyn_c"
,"https://en.wikipedia.org/wiki/Lacaille_8760"
,"https://en.wikipedia.org/wiki/Kruger_60"
,"https://en.wikipedia.org/wiki/DEN_1048-3956"
,"https://en.wikipedia.org/wiki/Ross_614"
,"https://en.wikipedia.org/wiki/Wolf_1061"
,"https://en.wikipedia.org/wiki/Wolf_1061b"
,"https://en.wikipedia.org/wiki/Wolf_1061_c"
,"https://en.wikipedia.org/wiki/Wolf_1061_d"
,"https://en.wikipedia.org/wiki/Wolf_424"
,"https://en.wikipedia.org/wiki/Van_Maanen_2"
,"https://en.wikipedia.org/wiki/Gliese_1"
,"https://en.wikipedia.org/wiki/L_1159-16"
,"https://en.wikipedia.org/wiki/Gliese_674"
,"https://en.wikipedia.org/wiki/Gliese_687"
,"https://en.wikipedia.org/wiki/LHS_292"
,"https://en.wikipedia.org/wiki/LP_145-141"
,"https://en.wikipedia.org/wiki/GJ_1245"
,"https://en.wikipedia.org/wiki/Gliese_876"
,"https://en.wikipedia.org/wiki/Gliese_876_d"
,"https://en.wikipedia.org/wiki/Gliese_876_c"
,"https://en.wikipedia.org/wiki/Gliese_876_b"
,"https://en.wikipedia.org/wiki/Gliese_876_e"
,"https://en.wikipedia.org/wiki/LHS_288"
,"https://en.wikipedia.org/wiki/GJ_1002"
,"https://en.wikipedia.org/wiki/Groombridge_1618"
,"https://en.wikipedia.org/wiki/DEN_0255-4700"
,"https://en.wikipedia.org/wiki/Gliese_412"
,"https://en.wikipedia.org/wiki/Gliese_832"
,"https://en.wikipedia.org/wiki/Gliese_832_c"
,"https://en.wikipedia.org/wiki/Gliese_832_b"
,"https://en.wikipedia.org/wiki/AD_Leonis"
,"https://en.wikipedia.org/wiki/GJ_1005"
,"https://en.wikipedia.org/wiki/LP_944-20"
,"https://en.wikipedia.org/wiki/40_Eridani"
,"https://en.wikipedia.org/wiki/EV_Lacertae"
,"https://en.wikipedia.org/wiki/Gliese_682"
,"https://en.wikipedia.org/wiki/Gliese_682_c"
,"https://en.wikipedia.org/wiki/70_Ophiuchi"
,"https://en.wikipedia.org/wiki/Altair"
,"https://en.wikipedia.org/wiki/G_9-38"
,"https://en.wikipedia.org/wiki/GJ_3379"
,"https://en.wikipedia.org/wiki/LHS_1723"
,"https://en.wikipedia.org/wiki/2MASS_0939-2448"
,"https://en.wikipedia.org/wiki/Gliese_445"
,"https://en.wikipedia.org/wiki/GJ_526"
,"https://en.wikipedia.org/wiki/Stein_2051"
,"https://en.wikipedia.org/wiki/Gliese_251"
,"https://en.wikipedia.org/wiki/Gliese_205"
,"https://en.wikipedia.org/wiki/LP_816-60"
,"https://en.wikipedia.org/wiki/2MASS_J04151954-0935066"
,"https://en.wikipedia.org/wiki/Sigma_Draconis"
,"https://en.wikipedia.org/wiki/Gliese_299"
,"https://en.wikipedia.org/wiki/Ross_47"
,"https://en.wikipedia.org/wiki/Gliese_693"
,"https://en.wikipedia.org/wiki/Gliese_752"
,"https://en.wikipedia.org/wiki/Gliese_570"
,"https://en.wikipedia.org/wiki/Gliese_588"
,"https://en.wikipedia.org/wiki/Eta_Cassiopeiae"
,"https://en.wikipedia.org/wiki/36_Ophiuchi"
,"https://en.wikipedia.org/wiki/Gliese_908"
,"https://en.wikipedia.org/wiki/YZ_Canis_Minoris"
,"https://en.wikipedia.org/wiki/HR_7703"
,"https://en.wikipedia.org/wiki/82_G._Eridani"
,"https://en.wikipedia.org/wiki/G_240-72"
,"https://en.wikipedia.org/wiki/ADS_7251"
,"https://en.wikipedia.org/wiki/Delta_Pavonis"
,"https://en.wikipedia.org/wiki/Gliese_268"
,"https://en.wikipedia.org/wiki/2MASSI_J0937347%2B293142"
,"https://en.wikipedia.org/wiki/Gliese_784"
,"https://en.wikipedia.org/wiki/Gliese_555"
,"https://en.wikipedia.org/wiki/EQ_Pegasi"
,"https://en.wikipedia.org/wiki/Gliese_581"
,"https://en.wikipedia.org/wiki/Gliese_581_e"
,"https://en.wikipedia.org/wiki/Gliese_581_b"
,"https://en.wikipedia.org/wiki/Gliese_581_c"
,"https://en.wikipedia.org/wiki/Gliese_581_g"
,"https://en.wikipedia.org/wiki/Gliese_581_d"
,"https://en.wikipedia.org/wiki/LHS_2090"
,"https://en.wikipedia.org/wiki/GJ_3737"
,"https://en.wikipedia.org/wiki/Furuhjelm_46"
,"https://en.wikipedia.org/wiki/LP_658-2"
,"https://en.wikipedia.org/wiki/V1054_Ophiuchi"
,"https://en.wikipedia.org/wiki/GJ_625"]



starlinks_with_quotations =list()
print(len(starlinks))

x = list()
def get_infotable(soup):
		for items in soup.table.tbody.find_all("tr")[:-1]:
			print("_____________________________-________")
			for item in items.find_all(['th','td']):
    				print(item.get_text())
    				x.append(item.get_text())
		return x


# def writeinfotocolumn(soup):
#          for i in range(len(starlinks)):
#              http = urllib3.PoolManager(10)
# 			 sauce = http.request('GET', starlinks[i] ).data
# 			 oup = bs.BeautifulSoup(sauce, features="html.parser")
# 			 j=0
# 			 for items in soup.table.tbody.find_all("tr")[:-1]:
# 				 print("_____________________________-________")
# 				 for item in items.find_all(['th','td']):
# 				     j+=1		
#     				 ws.write(j,i,item.get_text())



def writeinfotocolumns():
	for i in range(len(starlinks)):
		http = urllib3.PoolManager(10)
		sauce = http.request('GET', starlinks[i]).data
		soup = bs.BeautifulSoup(sauce, features="html.parser")
		j=0
		for items in soup.table.tbody.find_all("tr")[:-1]:
			print("_____________________________-________")
			print("")
			##PRINT OUT THE NAME OF THE WEBSITE BECAUSE ONE OF THEM MIGHT NOT HAVE A TABLE
			for item in items.find_all(['th', 'td'])[:-1]:
				name = soup.find('h1', id="firstHeading").string
				ws.write(0,i,name)
				ws.write(j+1,i,item.get_text())
				# if(item.get_text=="Right Ascension"):
				# 	print("Right Ascension FOUND")
				# 	ws.write(45,i,item.get_text())
				if(item.get_text()=="Right ascension"):
					print("RIGHT ASCENSION FOOOOUND")
					print(item.get_text())
					print(item.find_next_sibling().get_text())
					print(item.find_next_sibling().find_next_sibling().get_text())
				if(item.get_text()=="Declination"):
					print("DECLINATION FOOOOOUND")
				j+=1
	wb.save("stardata.xls")

writeinfotocolumns()

print("Hello")


# list_of_data_lists = list()



# for i in range(len(starlinks)):
# 	http = urllib3.PoolManager(10)
# 	sauce = http.request('GET', starlinks[i] ).data
# 	soup = bs.BeautifulSoup(sauce, features="html.parser")
	

