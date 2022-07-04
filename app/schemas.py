from pydantic import BaseModel
from typing import Optional, Any

class UssdInfo(BaseModel):
    date:  Any                             #date in UTC format(yyyy-mm-dd HH:mm:ss)
    sessionId: Any 
    serviceCode: Any                      #ussd code
    networkCode: Any                       #(63902 safaricom)  (620903 airtel kenya) (99999 sandbox)
    phoneNumber: Any                        # subscriber phone no
    status: Any                  #incompelete, success,  failed, errorMessage
    cost: Any                     #cost of USSD session
    durationInMillis: Any
    hopsCount: Any                #steps user passedduring ussd session
    input: Any                             #input entered by user separeted by *
    lastAppResponse:Any
    errorMessage: Any
    text: Optional[str]=''                               #textual input