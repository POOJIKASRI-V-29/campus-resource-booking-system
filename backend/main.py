from models import Resource, Booking
from database import resources_collection, bookings_collection
from fastapi import FastAPI, HTTPException
from models import Resource
from database import resources_collection

app = FastAPI(title="Campus Resource Booking System")

@app.get("/")
def root():
    return {"message": "Campus Resource Booking System API is running"}

@app.post("/resources")
def create_resource(resource: Resource):
    existing = resources_collection.find_one(
        {"resource_id": resource.resource_id}
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Resource with this ID already exists"
        )

    resources_collection.insert_one(resource.dict())
    return {"message": "Resource created successfully"}
@app.get("/resources")
def get_resources():
    resources = list(resources_collection.find({}, {"_id": 0}))
    return resources

@app.post("/bookings")
def create_booking(booking: Booking):
    
    resource = resources_collection.find_one(
        {"resource_id": booking.resource_id}
    )
    if not resource:
        raise HTTPException(
            status_code=404,
            detail="Resource not found"
        )

    
    conflicts = bookings_collection.find({
        "resource_id": booking.resource_id,
        "date": booking.date,
        "start_time": {"$lt": booking.end_time},
        "end_time": {"$gt": booking.start_time}
    })

    if conflicts.count() > 0:
        raise HTTPException(
            status_code=400,
            detail="Time slot already booked"
        )

    bookings_collection.insert_one(booking.dict())
    return {"message": "Booking confirmed"}
@app.get("/bookings")
def get_bookings():
    bookings = list(bookings_collection.find({}, {"_id": 0}))
    return bookings
