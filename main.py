import json
def convert_letter_to_number(letter):
    if(ord(letter)<=105):
        return ord(letter)-ord('a')
    else:
        return ord(letter)-ord('a')-2

def load_melody(letter):
    with open('data.json') as json_file:
        melodie = json.load(json_file)
    #carico la melodia corrispondente alla lettera('a' corrisponde alla melodia 0 e così via)
    id=convert_letter_to_number(letter)
    print("È stata selezionata la melodia numero "+str(id)+" corrispondente al file "+melodie[id]['file']+"\n Inizia il gioco!\n")
    numero_nota = 0
    #tabella per convertire le note in tasti
    corrisp={'la':'a','si':'b','do':'c','re':'d','mi':'e','fa':'f','sol':'g','do#':'h','re#':'i','fa#':'l','sol#':'m','la#':'n'}
    while(numero_nota<len(melodie[id]['sequenza'])):

        print("Si illumina il tasto della lettera '"+corrisp[melodie[id]['sequenza'][numero_nota]]+"'\n")
        l=input()
        while(l!=corrisp[melodie[id]['sequenza'][numero_nota]]):
            print("Suono di errore, non era il tasto giusto")
            print("Si illumina il tasto della lettera '"+corrisp[melodie[id]['sequenza'][numero_nota]]+"'\n")
            l=input()
        print("Suona la nota "+melodie[id]['sequenza'][numero_nota]+". Hai premuto il tasto corretto!")
        numero_nota+=1
    print("\nHai completato la melodia numero "+str(id)+".\nViene riprodotta nelle casse da capo...\nBella vero?\n\n")

def game():
    while(True):
        message="Per favore premere un tasto(da 'a' ad 'n') per selezionare una melodia.\nPremere invio per confermare\n(Premere q ed invio per uscire)"
        print(message)
        l=input()
        while(l not in 'abcdefghilmnq'):
            print("Errore, il tasto premuto non è tra 'a' ed 'n', controllare il CAPS-LOCK!")
            l=input()
        if(l=='q'):
            return
        else:
            load_melody(l)


print("\nBenvenuto nell'emulatore della tastiera!\n\n")
game()
