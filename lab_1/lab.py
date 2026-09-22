import numpy
import matplotlib.pyplot as plot
from scipy.integrate import odeint  # Ordinary Differential Equation Integrator

volume = 52  # Объем бака
theta_1 = 15  # Температура первого потока (холодная вода)
theta_2 = 55  # Температура второго потока (горячая вода)
g_1 = 4  # Расход первого потока (холодная вода)
g_2 = 3  # Расход второго потока (горячая вода)

T0 = 25

def heat_balance_ode(T, t):
    dT_dt = (g_1 * theta_1 + g_2 * theta_2 - (g_1 + g_2) * T) / volume
    return dT_dt

t = numpy.linspace(0, 60, 600)

T_solution = odeint(heat_balance_ode, T0, t)

T_steady = (g_1 * theta_1 + g_2 * theta_2) / (g_1 + g_2)  # dT_dt = 0
print(f"Установившаяся температура: {T_steady:.2f} градусов")

# Построение графика
plot.figure(figsize=(10, 6))
plot.plot(t, T_solution, 'b-', linewidth=2, label='Температура в баке T(t)')

plot.axhline(y=T_steady, color='g', linewidth=1, linestyle='--', label=f'Установившееся значение ({T_steady:.1f}°)')

plot.title('Моделирование смешивания двух потоков')
plot.xlabel('Время, с')
plot.ylabel('Температура, °С')
plot.legend()
plot.grid(True)

file_name = 'simulation.png'
plot.savefig(file_name, dpi=100)
print(f"График сохранен в файл '{file_name}'")
