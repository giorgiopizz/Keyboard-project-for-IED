import json
import random

def create_melody(note):
    #può avere una lunghezza che varia da minimo 3 note fino ad un max di 10
    sequenza=[]
    lenght=random.randint(3,10)
    for i in range(lenght):
        sequenza.append(note[random.randint(0,len(note)-1)])
    return sequenza

#le note corrispondono ai tasti a,b,c,d,e,f,g,h,i,l,m,n
note=['la','si','do','re','mi','fa','sol','do#','re#','fa#','sol#','la#']
print(len(note))
#note=['do','do#','re','re#','mi','fa','fa#','sol','sol#','la','la#','si']

#questo dizionario è per la conversione che ci servirà dopo
corrisp={'la':'a','si':'b','do':'c','re':'d','mi':'e','fa':'f','sol':'g','do#':'h','re#':'i','fa#':'l','sol#':'m','la#':'n'}

#creo 15 melodie a caso, a cui associo un numero identificativo, un file a caso e una sequenza di note
#la sequenza di note corrispondente ad ogni melodia è di lunghezza casuale e ha note a caso
melodie=[]
for i in range(12):
    melodia={}
    melodia['id']=i
    file_name = '/Users/giorgio/Desktop/melodie/melody_'+str(i)+'.wav'
    melodia['file']=file_name
    melodia['sequenza']=create_melody(note)
    melodie.append(melodia)

print(json.dumps(melodie))

with open('data.json','w') as json_file:
    json.dump(melodie, json_file)



# Struttura file data.json
# [
#     {
#         "id": 0,
#         "file":"/Users/giorgio/",
#         "sequenza":["mi","la"
#
#         ]
#     }
# ]
