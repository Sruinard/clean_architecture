from fastapi import FastAPI
from cabrenter.use_cases.cab_selector import CabSelector
from cabrenter.repositories.cab_data_repository import CabRepository
from cabrenter.data_structures.request_model import RequestModel, CabModel
from cabrenter.repositories.database_access_cosmosdb import DataAccessCosmos
from cabrenter.repositories.database_access_sql import DataAccessSQL
import os
import dotenv
from fastapi.middleware.cors import CORSMiddleware

dotenv.load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()


@app.get("/")
def welcome():
    return "Hello Clean Architecture World"
    

@app.get("/healthz")
def healthz():
    return "Healthy"

@app.get("/api/cabs")
def get_suitable_cabs(city: str):
    cabs = CabSelector(
        repo=CabRepository(
            database_access=DataAccessCosmos(
                connection_string=os.getenv("CONNECTION_STRING")
            )
        )
    ).get(
        RequestModel(city=city)
    )
    return [cab.to_dict() for cab in cabs]

@app.get("/api/cabs/sql")
def get_suitable_cabs(city: str):
        
    cabs = CabSelector(
        repo=CabRepository(
            database_access=DataAccessSQL(
                server=os.getenv("SQL_SERVER"),
                database=os.getenv("SQL_DATABASE"),
                username=os.getenv("SQL_ADMIN"),
                password=os.getenv("SQL_PASSWORD")
            )

        )
    ).get(
        RequestModel(city=city)
    )
    return [cab.to_dict() for cab in cabs]

@app.post("/api/cabs/sql")
def add_cab(cab: CabModel):
    cab = CabSelector(
        repo=CabRepository(
            database_access=DataAccessSQL(
                server=os.getenv("SQL_SERVER"),
                database=os.getenv("SQL_DATABASE"),
                username=os.getenv("SQL_ADMIN"),
                password=os.getenv("SQL_PASSWORD")
            )
        )
    ).post(
        request_object=cab
    )
    return cab

@app.post("/api/cabs")
def add_cab(cab: CabModel):
    cab = CabSelector(
        repo=CabRepository(
            database_access=DataAccessCosmos(
                connection_string=os.getenv("CONNECTION_STRING")
            )
        )
    ).post(
        request_object=cab
    )
    return cab
