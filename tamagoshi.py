class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
   
    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100)
   
    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade / 100)

            self.saude -= quantidade * 0.2

        if self.saude < 0:
            self.saude = 0
            
        if(self.saude > 30):
            print(f"{self.nome} brincou e está mais feliz!")

        
        
    def getHumor(self):
        return 100 - ((self.fome + self.tedio)/2)
   
    def vida(self):
        if ((self.fome > 50 and self.fome <= 60)) or ((self.tedio > 50 and self.tedio <= 60)) or ((self.saude > 50 and self.saude <= 60)):
            self.saude -= 10
        elif ((self.fome > 60 and self.fome <= 80)) or ((self.tedio > 60 and self.tedio <= 80))  or ((self.saude > 50 and self.saude <= 60)):
            self.saude -= 30
        elif ((self.fome > 80 and self.fome <= 90)) or ((self.tedio > 80 and self.tedio <= 90))  or ((self.saude > 50 and self.saude <= 49)):
            print("Minha saúde está baixando...")
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90)  or (self.saude <= 30):
            print("Estou morrendo.... AAAAAAAAH")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0
            print("Seu bichinho morreu T_T")
   
    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5
 

    def exibir_status(self):
        print(f"\n📊 Status de {self.nome}:")
        print(f"Idade: {round(self.idade,1)} anos")
        print(f"Saúde: {round(self.saude,1)} / 100")
        print(f"Fome: {round(self.fome,1)} / 100")
        print(f"Tédio: {round(self.tedio,1)} / 100")
        print(f"Humor: {round(self.getHumor(),1)} / 100")