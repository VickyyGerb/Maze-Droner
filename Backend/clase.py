# clase.py
from djitellopy import Tello
import time

class DroneController:
    def __init__(self):
        self.tello = Tello()
        self.start_time = None
        self.running = False

    def connect(self):
        self.tello.connect()
        print(f"Nivel de batería: {self.tello.get_battery()}%")

    def start(self):
        """Despega el dron y empieza el cronómetro"""
        self.tello.takeoff()
        self.start_time = time.time()
        self.running = True
        print("Dron iniciado y cronómetro corriendo")

    def stop(self):
        """Aterriza el dron y detiene el cronómetro"""
        self.tello.land()
        self.running = False
        if self.start_time:
            elapsed = time.time() - self.start_time
            print(f"Tiempo total de vuelo: {elapsed:.2f} segundos")
        print("Dron detenido")

    def move(self, direction: str):
        """Ejecuta movimiento según la dirección"""
        if not self.running:
            print("⚠️ El dron no está en vuelo. Presiona Start primero.")
            return

        distance = 50  # cm
        if direction == "up":
            self.tello.move_forward(distance)
        elif direction == "down":
            self.tello.move_back(distance)
        elif direction == "left":
            self.tello.move_left(distance)
        elif direction == "right":
            self.tello.move_right(distance)
        else:
            print("Dirección inválida")
