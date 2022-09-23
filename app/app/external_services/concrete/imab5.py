from app.external_services.templates.requestTemplate import RealtimeApiTemplate
from app.external_services.concrete.constants import URL


class imab5(RealtimeApiTemplate):
    def __init__(self, rt_payload: str,rt_url: str = URL,  rt_api_type: str = "POST"):
        super().__init__(rt_url, rt_payload, rt_api_type)