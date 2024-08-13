Sadik = {
    'ad':'Sadik Turan',
    'hesapNo':'165782053',
    'bakiye': 3000,
    'ekhesap': 2000 
}

Ali = {
    'ad':'Ali Turan',
    'hesapNo':'16575673',
    'bakiye': 12000,
    'ekhesap': 100000 
}
def paracek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paraniz cebinizde olacak')
        parasorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']

        if toplam >= miktar:
            ekhkull = input("ek hesap kullanma izin verir mesin? faiz orani %2 (e\h)")

            if ekhkull == "e" :
                ekhesapkullan = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekhesap'] = ekhesapkullan
                print("paranizi alabilirsiniz")
                
                parasorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesapta {hesap['bakiye']} bulunmaktadir")
        else:
            print("uzginyuz bakiye yetersizdir")
            parasorgula(hesap)

            
def parasorgula(hesap):
    print(f"{hesap['hesapno']} lu hesabinizda {hesap['bakiye']} TL bulunmaktadir. Ek hesap limitiniz ise {hesap['ekhesap']}  TL dir.")

paracek(Sadik, 10000)        