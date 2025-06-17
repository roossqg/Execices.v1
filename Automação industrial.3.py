#lotes com pressão acima da média
import math
import random
import statistics

def pressao_media(l1,l2,l3,l4,l5):
    lt=[l1,l2,l3,l4,l5]
    mn=statistics.mean(lt)
    return mn

#uma função trabalha com a outra
 
def lotes_acima_da_media(mn,l1,l2,l3,l4,l5):
    lt=[l1,l2,l3,l4,l5]
    ltd2s=sum([1 for y in lt if y>mn])
    ltds=ltd2s
    jk=[y for y in lt if y>mn]
    ds=sum([y for y in lt if y>mn])
    return ltds,jk,ds

lts=pressao_media(112,234,233,167,98)
mc=lotes_acima_da_media(lts,112,234,233,167,98)
print(f'a media é {lts} \n já os elementos acima:{mc}')