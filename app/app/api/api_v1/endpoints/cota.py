from multiprocessing import current_process
from fastapi import APIRouter
from typing import Any,List
from app.schemas.cota import Cota
from app.external_services.concrete.imab5 import imab5
from app.external_services.concrete.constants import PAYLOAD
from app.external_services.concrete.quoteGetter import imab5QuoteGetter
from datetime import datetime,timedelta

#"Dt_Ref":"15/09/2022"
router = APIRouter()

@router.get("/",response_model=List[Cota])
def cota_handler()->Any:
    today = (datetime.now() - timedelta(1) ).strftime("%d/%m/%Y")
    PAYLOAD["Dt_Ref"] = today
    imab5Instance = imab5(rt_payload=PAYLOAD)
    imab5QuoteGetterInstance = imab5QuoteGetter()
    r = imab5Instance.make_rt_request()
    quota = imab5QuoteGetterInstance.deserialize_response(r)
    if quota is None:
        return None
    else:
        quoteValue = float(quota.replace(".","").replace(",","."))
        responseElement = Cota(quote=quoteValue,date=today)
        response = []
        response.append(responseElement)
        return response