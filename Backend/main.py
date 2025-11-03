# main.py
from fastapi import FastAPI, Query
from clase import DroneController

app = FastAPI()
drone = DroneController()

@app.on_event("startup")
def startup_event():
    drone.connect()

@app.post("/start")
def start_drone():
    drone.start()
    return {"status": "Dron iniciado"}

@app.post("/stop")
def stop_drone():
    drone.stop()
    return {"status": "Dron detenido"}

@app.post("/move")
def move_drone(direction: str = Query(..., description="up, down, , right")):
    drone.move(direction)
    return {"status": f"Movimiento {direction} ejecutado"}
