from fastapi import FastAPI
from typing import Any
from scalar_fastapi import get_scalar_api_reference 
app=FastAPI()
shipments={
    2021:{"Contact no":"030803",
    "Name ":"MUHAMMAD ABUBAKAR",
    "Address":"Faisalabad",},
    2022:{"Contact no":"03123456789",
    "Name ":"ALI KHAN",
    "Address":"Lahore",},
    2023:{"Contact no":"03219876543",
    "Name ":"SARA BIBI",
    "Address":"Karachi",},
    2024:{"Contact no":"03330001122",
    "Name ":"OMAR RAHMAN",
    "Address":"Islamabad",},
    2025:{"Contact no":"03441234567",
    "Name ":"AYESHA NOOR",
    "Address":"Peshawar",},
}
@app.get("/shipment/latest")
def GetShipment_latest()->dict[str,Any]:
    id=max(shipments.keys())
    return shipments[id]
@app.get("/shipment/{id}")
def GetShipment(id: int|float)->dict[str,Any]:
    if id  not in shipments:
        return {"error":"Shipment not found"}
    return shipments[id]


@app.get("/scalar")
def get_Scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar Api",
    )