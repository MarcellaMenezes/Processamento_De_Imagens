import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4*np.pi, 0.1)
ySen = np.sin(x)
yCos = np.cos(x)

#print('x:', x[:5])
#print('y:', y[:5])

plt.plot(x,ySen,'r')
plt.plot(x,yCos,'g')

plt.xlabel('valores de 0 a 4pi')
plt.ylabel('sen(x) e cos(x)')
plt.title('Grafico de seno e cos')
plt.legend(['sen[x]', 'cos[x]'])
plt.show()
