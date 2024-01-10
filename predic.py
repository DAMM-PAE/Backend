import tensorflow as tf
import numpy as np
from datetime import datetime

# Fechas en formato de cadena
dates_str = [
     '2022-01-11', '2022-02-01', '2022-02-21', '2022-03-08', '2022-03-21',
    '2022-04-13', '2022-04-18', '2022-04-26', '2022-05-10', '2022-05-30',
    '2022-06-13', '2022-06-20', '2022-07-05', '2022-07-19', '2022-07-28',
    '2022-08-01', '2022-08-12', '2022-08-24', '2022-09-02', '2022-09-16',
    '2022-09-23', '2022-10-10', '2022-10-20', '2022-11-10', '2022-11-21',
    '2022-12-13', '2022-12-30'
]

# Convertir las fechas a números ordinales y normalizar
dates = [datetime.strptime(d, '%Y-%m-%d').toordinal() for d in dates_str]
print(dates)
max_date = 1
normalized_dates = [d / max_date for d in dates]

# Datos de entrenamiento (todas menos la última fecha)
train_dates = normalized_dates[:-1]
train_labels = normalized_dates[1:]

# Modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compilar el modelo
model.compile(optimizer='adam', loss='mse')

# Entrenar el modelo
model.fit(train_dates, train_labels, epochs=1000, verbose=0)

# Predecir la siguiente fecha
last_date_normalized = datetime.strptime('2024-01-12', '%Y-%m-%d').toordinal()
predicted_next_date_normalized = model.predict([last_date_normalized])[0][0]
predicted_next_date = datetime.fromordinal(int(predicted_next_date_normalized * max_date))

print(f'Fecha predicha para la próxima entrega: {predicted_next_date.strftime("%Y-%m-%d")}')
