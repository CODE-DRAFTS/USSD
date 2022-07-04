from  fastapi import FastAPI
from .schemas import UssdInfo
app = FastAPI()

@app.get('/')
def home():
    return 'home page'


@app.post('/app')
def home(ussd_info: UssdInfo):
    response =''

    if ussd_info.text == '':
        response ='CON welcome to airtime pay \n'
        response +='1. buy airtime for my number \n'
        response +='2.buy airtime for another number \n'
        response +='3.buy mobile data for my number \n'
        response +='4.buy mobile data another number \n'

    if ussd_info.text == '1*1':
        response ='CON enter number to make payment \n'
        response +='1. use this number'
    
    if ussd_info.text == '1*2':
        response ='CON enter number'

    if ussd_info.text == '1*3':
        response ='CON enter  number to make payment \n'
        response +='1. use this number'

    if ussd_info.text == '1*4':
        response ='CON enter number \n'
    
    return response