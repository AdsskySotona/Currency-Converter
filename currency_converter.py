from urllib import request
import json

link = 'http://api.fixer.io/latest?base=USD'
try:
    data = request.urlopen(link)
except:
    print('Error: The server may not be available or the address is incorrect!!!\nPlease check the internet connection!!!')
try:
    jData = data.read()
except NameError:
    print('Error: Due to an error in the previous step we can not continue please check the internet connection!!!')
try:
    rates = json.loads(jData)['rates']
except NameError:
    print('Error: Due to an error in the previous step we can not continue please check the internet connection!!!')
while True:
    USD = input('Sum> ')
    toCurrensy = input('To currensy> ')
    def Convert(USD,rates):
        return float(USD)*rates
    try:
        print ('{0} USD is {1} {2}\n'.format(USD,Convert(USD,rates[toCurrensy]),toCurrensy))
    except KeyError:
        print('Not a valid currency format, try again!!!\n\n')



