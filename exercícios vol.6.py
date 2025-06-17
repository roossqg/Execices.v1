#verificar se uma frase possui a palavra "silva"
slk=input('digite uma frase: ').lower().strip()

#encontra o valor da primeira letra de "silva",corta o que está atrás em uma lista
#e junta novamente em uma str
sdf=slk.find('silva')
slk21=slk[sdf::].split()
slk2=' '.join(slk21)
print(slk2)

#encontra o primeiro espaço a partir de "silva"
sdf3=slk2[0::].find(' ')
if sdf3==-1:
   #sem espaço(final ou solo)
   sdf2=len(slk2)

    #conta se possui 5 letras até o final,não ultrapassando o silva
   if sdf2==5:
    print(' a frase contém a palavra silva')
    print(sdf2,sdf3)

  #se o espaço estiver na posição 5,significa que possui 5 caracteres(0-4)
if sdf3==5:
 sdf9=len(slk2[:sdf3:])
 if sdf9==5:
  print(' a frase contém a palavra silva')
  print(sdf9,sdf3)
else:
   print('a frase não contém a palavra  silva')
#não testei com "silva " kkkkk

#verificar cidades com iniciais de santo
dig22=input('digite um nome de uma cidade: ')
dig2=dig22.low()
dig=dig2.title()
dg3=dig.find('São')
fg4=dig[dg3::].find(' ')
fcv=len(dig[dg3:fg4:])
if dg3==0 and fcv==3:
   print('a cidade começa com santo')
else:
   print('a cidade não contem santo')


#ler nomes
name=input('digite seu nome: ')
nm2=name.upper()
nm3=name.lower()
tex=name.replace(' ','')
le=len(tex)
nam3=name.find(' ')
if nam3>=0:
 le2=len(name[0:nam3])
else:
   le2=le
print(f'olá,{nm2} ou {nm3},seu nome tem {le} letras e {le2} letras no primeiro nome')

#composição dos números
num1=(input('digite um número: '))
if len(num1)==1:
   print(f'o número {num1[0]} representa {num1[0]} unidade(s)')
elif len(num1)==2:
   print(f'o número {num1[0]} representa {num1[0]}0 ou {[0]} dezenas(s)')
   print(f'o número {num1[1]} representa {num1[1]} unidade(s)')
elif len(num1)==3:
   print(f'o número {num1[2]} representa {num1[2]} unidades')
   print(f'o número {num1[1]} representa {num1[1]}0 ou {num1[1]} dezenas')
   print(f'o número {num1[0]} representa {num1[0]}00 ou {num1[0]} centenas')
else:
   print('o número é muito grande')

























