n1=2
class Boss():
    def __init__(self):
        self.life=500
        self.magic=200
        self.active=False
    

    def atacado(self):
        self.life=self.life-20
Bossu=Boss()
while n1!=0:
    print("Escribe 1 para atacar al boss")
    n1=int(input())
    if n1==1:
      Bossu.atacado()
      print("VidaBoss:", Bossu.life)
         
n1=2

