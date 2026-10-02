"""Моделирование смешивания двух потоков воды в баке."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint  # интегратор ОДУ

# --- Параметры модели ---
VOLUME = 52  # Объём бака, л
THETA_1 = 15  # Температура первого потока (холодная вода), °C
THETA_2 = 65  # Температура второго потока (горячая вода), °C
G_1 = 4  # Расход первого потока, м^3/с
G_2 = 3  # Расход второго потока, м^3/с
THETA_0 = 25  # Начальная температура воды в баке, °C

# --- Параметры расчёта ---
T_END = 60  # Длительность моделирования, с
NUM_POINTS = 600  # Число точек временной сетки

# --- Оформление графика ---
OUTPUT_FILE = Path(__file__).parent / "simulation.png"  # путь отсчитывается от скрипта
FIGURE_SIZE = (10, 6)  # размер рисунка, дюймы
DPI = 150  # разрешение сохраняемого изображения

def heat_balance_ode(T: float, t: float) -> float:
    """Производная температуры в баке: уравнение теплового баланса."""
    dT_dt = (G_1 * THETA_1 + G_2 * THETA_2 - (G_1 + G_2) * T) / VOLUME
    return dT_dt

def main() -> None:
    t_grid = np.linspace(0, T_END, NUM_POINTS)
    T_numeric = odeint(heat_balance_ode, THETA_0, t_grid)

    final = T_numeric[-1][0]
    print(f"Конечная температура: {final:.2f} градусов")

    plt.figure(figsize=FIGURE_SIZE)
    plt.plot(t_grid, T_numeric, "b-", linewidth=2, label="T(t)")
    plt.title("Моделирование смешивания двух потоков")
    plt.xlabel("Время, с")
    plt.ylabel("Температура, °C")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(OUTPUT_FILE, dpi=DPI)
    print(f"График сохранён в файл '{OUTPUT_FILE.name}'")

if __name__ == "__main__":
    main()
