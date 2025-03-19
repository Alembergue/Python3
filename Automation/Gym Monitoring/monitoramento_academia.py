import pandas as pd
from datetime import datetime
from sklearn.linear_model import LinearRegression
import joblib
import os
from flask import Flask, jsonify, request, render_template

# Configuração do Flask
app = Flask(__name__)

# Variáveis globais
MODEL_PATH = "gym_occupancy_model.pkl"
DATA_PATH = "gym_access_log.csv"

# Carregar ou criar o log de acessos
def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH, parse_dates=['timestamp'])
    else:
        return pd.DataFrame(columns=['timestamp', 'cpf'])

def save_data(df):
    df.to_csv(DATA_PATH, index=False)

def register_access(cpf):
    df = load_data()
    new_entry = pd.DataFrame({'timestamp': [datetime.now()], 'cpf': [cpf]})
    df = pd.concat([df, new_entry], ignore_index=True)
    save_data(df)

def train_model():
    df = load_data()
    df['hour'] = df['timestamp'].dt.hour
    df['dayofweek'] = df['timestamp'].dt.dayofweek
    df['count'] = df.groupby(['timestamp']).transform('count')['cpf']
    df = df.drop_duplicates(subset=['timestamp'])
    
    X = df[['hour', 'dayofweek']]
    y = df['count']
    
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)

def predict_peak_hours():
    if not os.path.exists(MODEL_PATH):
        return "Modelo ainda não treinado"
    
    model = joblib.load(MODEL_PATH)
    future_hours = pd.DataFrame({
        'hour': list(range(24)),
        'dayofweek': [datetime.now().weekday()] * 24
    })
    predictions = model.predict(future_hours)
    busiest_hour = future_hours.iloc[predictions.argmax()]['hour']
    least_busy_hour = future_hours.iloc[predictions.argmin()]['hour']
    return busiest_hour, least_busy_hour

@app.route('/')
def home():
    df = load_data()
    current_count = df[df['timestamp'].dt.date == datetime.today().date()].shape[0]
    busiest_hour, least_busy_hour = predict_peak_hours()
    return render_template('index.html', current_count=current_count, busiest_hour=busiest_hour, least_busy_hour=least_busy_hour)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if 'cpf' in data:
        register_access(data['cpf'])
        return jsonify({"message": "Check-in registrado com sucesso!"}), 200
    return jsonify({"error": "CPF não fornecido"}), 400

@app.route('/status')
def status():
    df = load_data()
    current_count = df[df['timestamp'].dt.date == datetime.today().date()].shape[0]
    return jsonify({"current_count": current_count})

if __name__ == "__main__":
    app.run(debug=True)