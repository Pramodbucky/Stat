from bs4 import BeautifulSoup as bs
import requests as req
from send_email import *

URL = "https://www.worldometers.info/coronavirus/"
r = req.get(URL)
soup = bs(r.content, 'html.parser')
numbers = soup.find_all('div', attrs={'class':'maincounter-number'})
tables = soup.find_all('td')
infected_num = numbers[0].text.strip(' ')
death_num = numbers[1].text.strip(' ')
recover_num = numbers[2].text.strip(' ')
print("COVID-19 Statistics Tracker \n")
print("Number of infected cases: " + infected_num)
print("Number of death cases: " + death_num)
print("Number of recovery cases: " + recover_num)
ratio = int(recover_num.replace(',', ''))/int(death_num.replace(',', ''))
print("Recovery to Death ratio is "+str(round(ratio))+":1")
tab_list = []
for item in tables:
    tab_list.append(item.text)
try:
    Nepal_ind = tab_list.index(' Nepal ')
except ValueError:
    Nepal_ind = tab_list.index('Nepal')
victims_nepal = tables[Nepal_ind+1].text.strip(' ')
recover_nepal = tables[Nepal_ind+5].text.strip(' ')
newcase_Nepal = tables[Nepal_ind+2].text.strip(' ')
if newcase_Nepal:
    pass
else:
    newcase_Nepal = 0
try:
    Australia_ind = tab_list.index(' Australia ')
except ValueError:
    Australia_ind = tab_list.index('Australia')
victims_aus = tables[Australia_ind+1].text.strip(' ')
recover_aus = tables[Australia_ind+5].text.strip(' ')
newcase_aus = tables[Australia_ind+2].text.strip(' ')
if newcase_aus:
    pass
else:
    newcase_aus = 0
Nepal_Demo = "-"*25+"Nepal"+"-"*25
print(Nepal_Demo)
print("New cases in Nepal: " + str(newcase_Nepal))
print("Victims in Nepal: " + victims_nepal)
print("Recovered in Nepal: " + recover_nepal)
Aus_Demo = "-"*25+"Australia"+"-"*25
print(Aus_Demo)
print("New cases in Aus: " + str(newcase_aus))
print("Victims in Aus: " + victims_aus)
print("Recovered in Aus: " + recover_aus)
print("\nSource: Worldometers")
text = 'Source: Worldometers'+'\nNumber of infected cases: ' +str(infected_num)+'\nNumber of death cases: '+str(death_num)+'\nNumber of recovery cases: '+str(recover_num)+'\nRecovery to Death ratio is '+str(round(ratio))+':1'
if int(newcase_Nepal) > 0:
    print("Preparing to send mail for Nepal....")
    text = text + '\n' + Nepal_Demo + '\nVictims in Nepal: ' + str(victims_nepal) + '\nNew cases in Nepal: ' + str(newcase_Nepal)
    N_email = True
else:
    print("No changes in Nepal...So no email sent!!!")
    N_email = False
if int(newcase_aus) > 0:
    print("Preparing to send mail for Aus....")
    text = text + '\n' + Aus_Demo + '\nVictims in Aus: ' + str(victims_aus) + '\nNew cases in Aus: ' + str(newcase_aus)
    A_email = True
else:
    print("No changes in Aus...So no email sent!!!")
    A_email = False
if N_email | A_email == True:
    send_email(text)
else:
    print("Stay Safe!!!")

