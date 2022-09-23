from abc import ABC, abstractmethod
import requests

class InformationHandler(ABC):    
    
    @abstractmethod
    def deserialize_response(self,response:requests.request)->str:
        pass
