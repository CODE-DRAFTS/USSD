from pydantic import BaseModel
from typing import Optional

class UssdInfo(BaseModel):
    date:  str                              #date in UTC format(yyyy-mm-dd HH:mm:ss)
    sessionId: str 
    serviceCode: str                        #ussd code
    networkCode: str                        #(63902 safaricom)  (620903 airtel kenya) (99999 sandbox)
    phoneNumber: str                        # subscriber phone no
    status: Optional[str]                   #incompelete, success,  failed, errorMessage
    cost: Optional[str]                     #cost of USSD session
    durationInMillis: Optional[str]
    hopsCount: Optional[str]                #steps user passedduring ussd session
    input: str                              #input entered by user separeted by *
    lastAppResponse: Optional[str]
    errorMessage: Optional[str]
    text:str                                #textual input