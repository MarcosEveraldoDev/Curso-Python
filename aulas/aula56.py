x = 10

def escopo():
   
   x = 25
   def outro_escopo():
      
      x = 200
      y = 2
      print(x,y)
    
   outro_escopo()
   print(x)
   
escopo()