def hanoi(n,origen,destino,auxiliar):
    lista=[]
    while (n>1):
          lista.append([n,origen,destino,auxiliar])
          (n, origen,destino,auxiliar)=(n-1, origen, auxiliar, destino) 
    print("Se teletransporta disco desde la torre", origen, "hasta la torre", destino)
    while (len(lista)):
          n,origen,destino,auxiliar=lista.pop()
          print("Se teletransporta disco desde la torre", origen, "hasta la torre", destino)
          (n,origen,destino,auxiliar)=(n-1, auxiliar, destino,origen)                   
          while (n>1):
              lista.append([n, origen, destino, auxiliar])
              (n, origen,destino,auxiliar)=(n-1, origen, auxiliar, destino)
          print("Se teletransporta disco desde la torre", origen, "hasta la torre", destino)

hanoi(3,1,3,2)
