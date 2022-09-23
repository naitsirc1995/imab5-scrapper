from app.external_services.templates.responseHandler import InformationHandler
from app.external_services.concrete.constants import REGEX
import requests
import re

class imab5QuoteGetter(InformationHandler):
    def deserialize_response(self, response: requests.request) -> str:
        reCompiled = re.compile(REGEX)
        try:            
            responseText = response.content.decode("utf-8",errors="ignore")            
        except Exception as e:            
            return None

        resultRegex = re.search(reCompiled,responseText)

        if resultRegex is not None:
            return resultRegex.group(1)
        else:
            return None