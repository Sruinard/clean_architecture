from fastapi import FastAPI
from cabrenter.entities.cab import Cab
from cabrenter.use_cases.cab_selector import CabSelector
from cabrenter.repositories.cab_data_repository import CabRepository
from cabrenter.data_structures.request_model import RequestModel
from cabrenter.repositories.database_access_cosmosdb import DataAccessCosmos
from cabrenter.repositories.database_access_sql import DataAccessSQL
import os
import dotenv

dotenv.load_dotenv()
app = FastAPI()

@app.get("/api/cabs")
def get_suitable_cabs(city: str):
    cabs = CabSelector(
        repo=CabRepository(
            database_access=DataAccessCosmos(
                connection_string=os.getenv("CONNECTION_STRING")
            )
        )
    ).process_request(
        RequestModel(city=city)
    )
    return [cab.to_dict() for cab in cabs]

@app.get("/api/cabs/sql")
def get_suitable_cabs(city: str):
        
    cabs = CabSelector(
        repo=CabRepository(
            database_access=DataAccessSQL(
                server=os.getenv("SERVER"),
                database=os.getenv("DATABASE"),
                username=os.getenv("USERNAME"),
                password=os.getenv("PASSWORD")
            )

        )
    ).process_request(
        RequestModel(city=city)
    )
    return [cab.to_dict() for cab in cabs]