
import math
v1=(1*15,4*25,10*35,16*45,22*55,25*65,15*75,5*85,2*95)

grouped_aritmetic_ort=sum(v1)/100
print("grouped_aritmetic_ort" ,grouped_aritmetic_ort)

medyan=(((50-31)/(22))*10)+50
print("medyan", medyan)


mod=((3/(3+10))*10)+60
print("mod",mod)
v2=(grouped_aritmetic_ort,medyan,mod)
print(sorted(v2))



v3=(15,25,35,45,55,65,75,85,95)
f=(1,4,10,16,22,25,15,5,2)
standart=0
for i in range(len(v3)):
    for j in range(len(f)):
        standart=standart +(f[j]*((v3[i]-grouped_aritmetic_ort)**2))
standart_sapma=math.sqrt(standart/100)


        
print("standart_sapma",standart_sapma)


standart1=0
for i in range(len(v3)):
    for j in range(len(f)):
        standart1=standart1+(f[j]*((v3[i]-grouped_aritmetic_ort)**3))
carpıklık=standart1/(sum(f)*(standart_sapma)**3)
print("carpıklık",carpıklık)


standart2=0
for i in range(len(v3)):
    for j in range(len(f)):
        standart2=standart2+(f[j]*((v3[i]-grouped_aritmetic_ort)**4))
basıklık_sivrilik=standart2/(sum(f)*(standart_sapma)**4)
print("basıklık,sivrilik",basıklık_sivrilik)


