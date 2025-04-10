import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pickle
from datetime import datetime

# Load model
with open('final_weather_prediction_model.pkl', 'rb') as f:
    model_dict = pickle.load(f)

pipeline_temp = model_dict['pipeline_temp']
pipeline_hum = model_dict['pipeline_hum']

st.set_page_config(layout="wide")
st.title("Hourly Weather Forecast Dashboard")

# Input tanggal dan waktu
col1, col2 = st.columns(2)
with col1:
    selected_date = st.date_input("Pilih tanggal", datetime.now())
with col2:
    selected_hour = st.slider("Pilih jam (24H)", 0, 23, datetime.now().hour)

# Deteksi fitur input dari pipeline model
features_temp = list(pipeline_temp.feature_names_in_)
features_hum = list(pipeline_hum.feature_names_in_)
all_features = sorted(set(features_temp + features_hum))  # union fitur

# Dummy input untuk simulasi
n = 12  # prediksi 12 jam ke depan
input_data = {f: [] for f in all_features}
for h in range(selected_hour, selected_hour + n):
    hour_val = h % 24
    for f in all_features:
        if f == 'hour':
            input_data[f].append(hour_val)
        else:
            input_data[f].append(0)  # ganti dengan data real bila ada

df_input = pd.DataFrame(input_data)

# Prediksi
X_temp = df_input[features_temp]
X_hum = df_input[features_hum]
pred_temp = pipeline_temp.predict(X_temp)
pred_hum = pipeline_hum.predict(X_hum)

# Gabungkan ke dataframe untuk visualisasi
df_pred = pd.DataFrame({
    'Hour': df_input['hour'],
    'Predicted Temperature (°C)': pred_temp,
    'Predicted Humidity (%)': pred_hum
})

# Tampilkan informasi waktu prediksi
st.markdown(f"### Prediksi Cuaca Mulai {selected_date.strftime('%d %B %Y')} Jam {selected_hour:02d}:00")

# Tampilkan tabel hasil prediksi
st.subheader("Tabel Hasil Prediksi")
st.dataframe(df_pred.style.format({
    'Predicted Temperature (°C)': '{:.2f}',
    'Predicted Humidity (%)': '{:.2f}'
}), use_container_width=True)

# Fungsi plotting
def plot_weather_trends(df):
    fig_temp = go.Figure()
    fig_temp.add_trace(go.Scatter(
        x=df['Hour'], y=df['Predicted Temperature (°C)'],
        mode='lines+markers', line=dict(color='orange'),
        name='Temperature'
    ))
    fig_temp.update_layout(
        title='Temperature Trend',
        xaxis_title='Hour',
        yaxis_title='Temperature (°C)',
        template='plotly_white'
    )

    fig_hum = go.Figure()
    fig_hum.add_trace(go.Scatter(
        x=df['Hour'], y=df['Predicted Humidity (%)'],
        mode='lines+markers', line=dict(color='blue'),
        name='Humidity'
    ))
    fig_hum.update_layout(
        title='Humidity Trend',
        xaxis_title='Hour',
        yaxis_title='Humidity (%)',
        template='plotly_white'
    )

    st.plotly_chart(fig_temp, use_container_width=True)
    st.plotly_chart(fig_hum, use_container_width=True)

# Tampilkan grafik
plot_weather_trends(df_pred)

# Catatan tambahan
st.caption("Note: Saat ini menggunakan data dummy. Hubungkan ke data real-time untuk hasil lebih akurat.")