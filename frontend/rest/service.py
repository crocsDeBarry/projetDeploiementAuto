import httpx
from pydantic import BaseModel
from pydantic_settings import BaseSettings

class KatakanaService(BaseModel):
    """Service pour transformer un texte en katakana"""
    text: str

class LLMClient:
    def __init__(self, root_url: str) -> None:
        self.client = httpx.Client(verify=True)
        self.root_url = root_url

    def _generate_request(self, katakana_service: KatakanaService) -> tuple[dict, dict, str]:
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        body = {"text": katakana_service.text}
        route = f"http://{self.root_url}/convert_to_katakana/"
        return headers, body, route

    def post(self, katakana_service: KatakanaService):
        headers, body, route = self._generate_request(katakana_service=katakana_service)
        try:
            response = self.client.post(url=route, headers=headers, json=body)
            response.raise_for_status()
        except httpx.RequestError as exc:
            print(f"Erreur de requête : {exc}")
            raise
        except httpx.HTTPStatusError as exc:
            print(f"Erreur HTTP : {exc.response.status_code}")
            raise
        return response

class BackendConfig(BaseSettings):
    backend_service_name: str = "0.0.0.0:8000"

cfg = BackendConfig()
client = LLMClient(root_url=cfg.backend_service_name)