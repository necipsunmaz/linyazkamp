# -*- uncoding: utf-8 -*-

import operator

otomat = {
    "çay": 2,
    "kahve": 3,
    "çikolata": 5,
    "sigara":7,
    "gazoz":11
}
listcevir = sorted(otomat.items(), key=operator.itemgetter(1))



Nakit =1000
i = len(listcevir) - 1
while Nakit > 0:
    def makina(para, gida, adet=1, fail_silently=False):
        '''Bu fonksiyon parayı ve gıda türünü alır, duruma göre kalan parayı ve gıdayı müşteriye iletir.'''
        kalan = para
        for i in range(adet):
            if gida not in otomat:
                if fail_silently:
                    return i
                raise ValueError("Gıda yok")
            miktar = otomat[gida]
            if miktar > kalan:
                if fail_silently:
                    return i
                raise ValueError("Para yetmedi")
            kalan -= miktar

            # print(sorted_x[i][1], " liraya ", sorted_x[i][0], "satın alındı.")
    if listcevir[i][1] <= Nakit:
        print(makina(Nakit, listcevir[i][0]))
        Nakit -= listcevir[i][1]
        print(listcevir[i][1], " liraya ", listcevir[i][0], "satın alındı." "Kalan Nakit = ", Nakit)

    else:
        i -= 1
#Ekstra metot
"""
para = 100
i = len(sorted_x) - 1
while para > 0:
    if listcevir[i][1] <= para:
        print("Kalan Nakit = ", para)
        para -= listcevir[i][1]

        print(listcevir[i][1], " liraya ", listcevir[i][0], "satın alındı.")
    else: i -= 1
"""
