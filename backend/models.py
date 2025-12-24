from pydantic import BaseModel

class Resource(BaseModel):
    resource_id: str
    type: str
    capacity: int
class Booking(BaseModel):
    resource_id: str
    date: str          # YYYY-MM-DD
    start_time: str    # HH:MM
    end_time: str      # HH:MM
    booked_by: str
