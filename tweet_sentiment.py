import sys
import json

def leer_puntajes(archivo):
    puntajes={}
    for linea in archivo:
        claves=linea.split("\t")
        puntajes[claves[0]]=(claves[1])
    return puntajes
    #return puntajes 

def leer_tweets(archivo):
    tweets = []
    for linea in archivo:
        tweets.append(json.loads(linea))
    return tweets

def calcular_sentimiento(tweets, puntajes):
    pass

def main():
    archivo_tweets=open(sys.argv[1])
    archivo2=open(sys.argv[2])
    tweets=leer_tweets(archivo_tweets)
    puntajes=leer_puntajes(archivo2)
    for palabra in puntajes:
        print((palabra),(puntajes[palabra]))




if __name__ == '__main__' :
    main()
