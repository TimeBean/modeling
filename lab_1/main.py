import math
from pathlib import Path
from typing import Callable

# --- Параметры модели ---
# Физические константы
GRAVITATIONAL_ACCELERATION = 9.81  # м/с^2

ROAD_GRADE_PERCENT = 5.0  # Уклон дороги в % (5% = подъем 5 м на 100 м)
ROAD_INCLINATION_ANGLE = math.atan(ROAD_GRADE_PERCENT / 100.0)

# Константы модели
MASS = 1000.0  # Масса автомобиля, кг
TRACTION_GAIN_COEFFICIENT = 2500.0
WIND_RESISTANCE_COEFFICIENT = 20.0
ROLLING_FRICTION_COEFFICIENT = 0.015
HEADWIND_VELOCITY = 5.0  # Скорость встречного ветра, м/с

# --- Оформление графика ---
OUTPUT_FILE = Path(__file__).parent / "simulation.png"  # путь отсчитывается от скрипта
FIGURE_SIZE = (10, 6)  # размер рисунка, дюймы
DPI = 150  # разрешение сохраняемого изображения


def velocity_ode(t: float, v: float, u: Callable[[float], float]) -> float:
    """Вычисляет производную скорости dv/dt (ускорение) автомобиля."""
    current_u = u(t)

    traction_acceleration = (TRACTION_GAIN_COEFFICIENT * current_u) / MASS

    gravity_resistance = GRAVITATIONAL_ACCELERATION * (
            math.sin(ROAD_INCLINATION_ANGLE) +
            ROLLING_FRICTION_COEFFICIENT * math.cos(ROAD_INCLINATION_ANGLE)
    )

    wind_resistance = (WIND_RESISTANCE_COEFFICIENT * HEADWIND_VELOCITY) / MASS

    return traction_acceleration - gravity_resistance - wind_resistance  # dv/dt


if __name__ == "__main__":
    print('sim')
