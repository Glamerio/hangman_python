import random
import json

with open('turkish.json','r') as file:
    data = json.load(file)


x = random.choice(data['sentence_starters'])
x = x.lower()

harf = list(x)

bulunan_harf = ['_']  * len(x) 

def start():
    print(' '.join(bulunan_harf), end='\n\n')

def tahmin():
    i = 10
    while i != 0:
        print(f'Deneme hakki sayiniz : {i}\n')
        n = str(input('Harf alin ya da kelimeyi tahmin edin : ')).lower()
        
        if n == x:
            print(f'\n {x}' , sep=' ',end='\n\n')
            print('Tebrikler !!! ')
            return
        
        elif len(n) == 1 and n in harf:
            for index in range(len(x)):
                if harf[index] == n:
                    bulunan_harf[index] = x[index]

            print(' '.join(bulunan_harf), end='\n\n')

            if '_' not in bulunan_harf:
                print('Tebrikler! Tüm harfleri buldunuz!\n')
                return

        else:
            i = i - 1
            print(' '.join(bulunan_harf), end='\n\n')
            print('Yanlis tahmin :( \n')
    print(f'\nDeneme hakkiniz bitti !!\nCevap = {x}')
            

def main():
    start()
    tahmin()
    
if __name__ == '__main__':
    main()