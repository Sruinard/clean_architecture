# File containing the API endpoints.
import os

import dotenv
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cabrenter.models.request_models import CabConfiguration
from cabrenter.repositories.cab_finder_repo import MostSuitableCabCosmos
from cabrenter.repositories.driver_workspace_repo import DriverWorkspaceCosmos
from cabrenter.use_cases.driver_workspace import DriverWorkspace
from cabrenter.use_cases.find_optimal_cab import FindMostSuitableCabs

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
    return "Welcome To The Clean Architecture Workshop"

#--------------------#
#     Use Case 1     #
#--------------------#

@app.get("/api/cabs")
def get_cabs_for_user(city: str, max_price: int):
    repo = MostSuitableCabCosmos(
            connection_string=os.getenv("CONNECTION_STRING")
    )
    response = FindMostSuitableCabs(repo=repo).get(
            city=city,
            max_price=max_price
    )
    return response

#--------------------#
#     Use Case 2     #
#--------------------#

@app.post("/api/driver/{driver_id}/cabs")
def create_cab(driver_id: int, cab: CabConfiguration):
    CosmosRepo = DriverWorkspaceCosmos(
                connection_string=os.getenv("CONNECTION_STRING")
            )
    usecase = DriverWorkspace(repo=CosmosRepo)
    response = usecase.add_cab(
        driver_id=driver_id,
        city=cab.city, 
        brand=cab.brand, 
        hourly_price=cab.hourly_price
    )
    return response


@app.get("/api/driver/{driver_id}/cabs")
def get_cabs(driver_id: int):
    CosmosRepo = DriverWorkspaceCosmos(
                connection_string=os.getenv("CONNECTION_STRING")
            )
    usecase = DriverWorkspace(repo=CosmosRepo)
    response = usecase.get_cabs(
        driver_id=driver_id,
    )
    return response

@app.get("/api/driver/{driver_id}/cabs/{cab_id}")
def get_cab(driver_id: int, cab_id: str):
    CosmosRepo = DriverWorkspaceCosmos(
                connection_string=os.getenv("CONNECTION_STRING")
            )
    usecase = DriverWorkspace(repo=CosmosRepo)
    response = usecase.get_cab(
        driver_id, cab_id
    )
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
