from matplotlib import pylab as plt
import numpy as np
import skfuzzy as fuzz

#plt.rcParamas('figre.figsize')=(10.0 ,5.0)

#funcion de universo entrante
servicio =np.arange(0,10.1,0.1)
comida = np.arange (0,10.1,0.1)

#Funcion de la membresia de la entrada
#servicio

servicio_malo = fuzz.gaussmf(servicio , 0,1.5)
servicio_bueno = fuzz.gaussmf(servicio , 5 , 1.5)
servicio_exelente = fuzz.gaussmf(servicio , 10 , 1.5)


comida_mala = fuzz.trapmf(comida , 0,0,1,3)
comida_deliciosa = fuzz.gaussmf(comida ,10,1.5)


#propina

propina = np.arange (0,30,0.1)

propina_poca = fuzz.trimf(propina ,[0,5,10] )
propina_buena =fuzz.trimf(propina ,[0,5,10] )

plt.plot( comida_mala, servicio_malo, servicio_bueno)
plt.show()
