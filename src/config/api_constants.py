from dataclasses import dataclass
from dotenv import load_dotenv
import os


load_dotenv()
class EnvConfig:
    USERNAME = os.getenv('API_USERNAME')
    PASSWORD = os.getenv('API_PASSWORD')


@dataclass(frozen=True)
class APIConstants:
    BASE_URL = 'https://www.saucedemo.com'

api_config = APIConstants()
