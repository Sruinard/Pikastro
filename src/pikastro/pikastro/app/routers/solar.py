from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class SolarPanel(BaseModel):
    panel_id: str
    manufacturer: str
    capacity_kw: float
    is_operational: bool


# Sample data as an in-memory database
solar_panels_db = [
    SolarPanel(
        panel_id="1",
        manufacturer="Manufacturer A",
        capacity_kw=10.5,
        is_operational=True,
    ),
    SolarPanel(
        panel_id="2",
        manufacturer="Manufacturer B",
        capacity_kw=8.2,
        is_operational=False,
    ),
    SolarPanel(
        panel_id="3",
        manufacturer="Manufacturer C",
        capacity_kw=12.0,
        is_operational=True,
    ),
    SolarPanel(
        panel_id="4",
        manufacturer="Manufacturer A",
        capacity_kw=15.3,
        is_operational=False,
    ),
    SolarPanel(
        panel_id="5",
        manufacturer="Manufacturer B",
        capacity_kw=9.8,
        is_operational=True,
    ),
]


@router.post("/solar-panels", response_model=SolarPanel)
async def create_solar_panel(panel: SolarPanel):
    # Create a new solar panel
    solar_panels_db.append(panel)
    return panel


@router.get("/solar-panels/{panel_id}", response_model=SolarPanel)
async def read_solar_panel(panel_id: str):
    # Retrieve a solar panel by panel_id
    for panel in solar_panels_db:
        if panel.panel_id == panel_id:
            return panel
    raise HTTPException(status_code=404, detail="Solar panel not found")


@router.put("/solar-panels/{panel_id}", response_model=SolarPanel)
async def update_solar_panel(panel_id: str, updated_panel: SolarPanel):
    # Update a solar panel by panel_id
    for i, panel in enumerate(solar_panels_db):
        if panel.panel_id == panel_id:
            solar_panels_db[i] = updated_panel
            return updated_panel
    raise HTTPException(status_code=404, detail="Solar panel not found")


@router.delete("/solar-panels/{panel_id}", response_model=SolarPanel)
async def delete_solar_panel(panel_id: str):
    # Delete a solar panel by panel_id
    for i, panel in enumerate(solar_panels_db):
        if panel.panel_id == panel_id:
            deleted_panel = solar_panels_db.pop(i)
            return deleted_panel
    raise HTTPException(status_code=404, detail="Solar panel not found")
