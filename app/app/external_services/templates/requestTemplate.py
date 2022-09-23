import requests


class RealtimeApiTemplate():

    def __init__(self ,rt_url : str,rt_payload:str,rt_api_type:str = "POST"):
        ## API ARGUMENTS 
        self.rt_api_type = rt_api_type
        self.rt_url = rt_url
        self.rt_payload = rt_payload                

        
    def make_rt_request(self) -> requests.request:        
        return requests.post(self.rt_url,data = self.rt_payload)