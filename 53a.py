class Helikopter(object):
    def __init__(self, tip_helikopter,namena, brzina, dostrel):
        print(tip_helikopter,namena,"brzina",brzina,"dostrel",dostrel,"km")

class  Aérospatiale(Helikopter): #co zagradi povikucanje na glavnata klasa objekt
   def __init__(self):
    super().__init__('sa- 342 Gazela','izviduvacki',230,365)

class Mil(Helikopter):
   def __init__(self):
      super().__init__('mi-8', 'transporten', 250, 450)
class Bell(Helikopter):
  def __init__(self):
       super().__init__('bell-212','poveknamenski',190,450)
class Westland(Helikopter):
    def __init__(self):
       super().__init__('WS -55','transporten', 175, 538)

helio1=Aérospatiale()
hellio2=Mil()
helio3=Bell()
helio4=Westland()
