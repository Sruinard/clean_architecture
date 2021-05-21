from fastapi import FastAPI
from cabrenter.entities.cab import Cab
from cabrenter.use_cases.cab_selector import CabSelector
from cabrenter.repositories.cab_data_repository import CabRepository
from cabrenter.repositories.cab_data_repository_sql import CabRepositorySQL
from cabrenter.data_structures.request_model import RequestModel
import os
import dotenv

dotenv.load_dotenv()
app = FastAPI()

@app.get("/api/cabs")
def get_suitable_cabs(city: str):
    cabs = CabSelector(
        repo=CabRepository(
            connection_string=os.getenv("CONNECTION_STRING")
        )
    ).process_request(
        RequestModel(city=city)
    )
    return [cab.to_dict() for cab in cabs]

@app.get("/api/cabs/sql")
def get_suitable_cabs(city: str):
        
    cabs = CabSelector(
        repo=CabRepositorySQL(
            server=os.getenv("SERVER"),
            database=os.getenv("DATABASE"),
            username=os.getenv("USERNAME"),
            password=os.getenv("PASSWORD")
        )
    ).process_request(
        RequestModel(city=city)
    )
    return [cab.to_dict() for cab in cabs]