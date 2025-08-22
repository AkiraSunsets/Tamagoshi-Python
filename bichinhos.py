from tamagoshi import Tamagoshi

class Hamster(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.energia_rodar = 100  
        self.nivel_fofura = True 
   
    def rodar(self):
        if self.energia_rodar > 0:
            print(f"{self.nome} está rodando na rodinha!")
            self.energia_rodar -= 10
        else:
            print(f"{self.nome} está sem energia para brincar na rodinha.")
   
    def fazer_fofura(self):
        if self.nivel_fofura:
            print(f"{self.nome} está sendo fofo!")
        else:
            print(f"{self.nome} não consegue fazer fofuras.")
   
    def descansar(self):
        print(f"{self.nome} está descansando e recuperou energia.")
        self.energia_rodar = 100
 
 
class Cachorro(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.nivel_lealdade = 50   
        self.energia_corrida = 100 
   
    def latir(self):
        print(f"{self.nome} está latindo: Au Au!")
   
    def correr(self):
        if self.energia_corrida > 0:
            print(f"{self.nome} está correndo feliz!")
            self.energia_corrida -= 20
        else:
            print(f"{self.nome} está cansado e precisa descansar.")
   
    def receber_carinho(self):
        print(f"{self.nome} está recebendo carinho")
        self.nivel_lealdade += 10
 
 
class Gato(Tamagoshi):
    def __init__(self, nome):
        super().__init__(nome)
        self.nivel_preguica = 50   # antes era self.preguica
        self.nivel_misterio = 70   # antes era self.misterio
   
    def miar(self):
        print(f"{self.nome} está miando: Miau!")
   
    def dormir(self):
        print(f"{self.nome} tirou uma soneca...")
        self.nivel_preguica -= 10
   
    def arranhar(self):
        print(f"{self.nome} arranhou o sofá!")
        self.nivel_misterio += 5
