import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1, 10)  # иксы от 1 до 10
plt.plot(x, x**2, color='red', marker='o', markevery=5)  # x^2 красным, точки кружочками
plt.plot(x, np.exp(x), color='blue', marker='x', markevery=5)  # e^x синим, целые точки крестиками
plt.plot(x, np.log(x), color='green', marker='+', markevery=5)  # ln(x) зелёным, целые точки плюсиками
plt.plot(x, x**3, color='purple', marker='^', markevery=5)  # x^3 фиолетовым, целые точки треугольничками
plt.yscale('log')  # логарифмическая шкала чтобы все функции было видно
plt.show()  # выводит график