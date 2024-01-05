import tensorflow as tf
import numpy as np
import datetime

# Step 1: Preprocessing
# Convert string dates to datetime objects, then to ordinal form
dates = [
    '2022-04-26', '2022-05-10', '2022-05-30', '2022-06-13', '2022-06-20',
    '2022-07-05', '2022-07-19', '2022-07-28', '2022-08-01', '2022-08-12',
    '2022-08-24', '2022-09-02', '2022-09-16', '2022-09-23', '2022-10-10',
    '2022-10-20', '2022-11-10', '2022-11-21', '2022-12-13', '2022-12-30',
    '2022-01-11', '2022-02-01', '2022-02-21', '2022-03-08', '2022-03-21',
    '2022-04-13', '2022-04-18'
]  # your dates here
dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates]
ord_dates = [date.toordinal() for date in dates]

# Prepare data for the model
X = np.array(ord_dates[:-1])  # Features: all dates except the last
y = np.array(ord_dates[1:])   # Labels: all dates except the first

# Reshape data for the model (assuming LSTM or similar architecture)
X = X.reshape((len(X), 1, 1))  # Reshaping for single feature, single timestep
y = y.reshape((len(y), 1))     # Reshaping labels

# Step 2: Modeling
# Create a simple LSTM model
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(50, activation='relu', input_shape=(1, 1)),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Step 3: Training
model.fit(X, y, epochs=200, verbose=0)

# Step 4: Prediction
# Predict the next date
predicted_next_date_ordinal = model.predict([[ord_dates[-1]]])
predicted_next_date = datetime.date.fromordinal(int(predicted_next_date_ordinal))

print(f"The predicted next date is: {predicted_next_date}")
