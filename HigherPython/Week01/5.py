print('Plz input according to the instruction and you have 3 chance')
trytimes=0
while trytimes<3:
    name=input('name:')
    passwd=input('passwd:')
    if name=='zjc' and passwd=='buaasem':
        break
    else:
        print('login faliure')
        print('You still have %d chances' %(2-trytimes))
        trytimes+=1
if trytimes<3:
    print('successful login')
else:
    print('Your chances is run out,Plz login later')

