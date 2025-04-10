
# Hourly Weather Forecast Dashboard

A Streamlit-based interactive dashboard for hourly weather prediction using machine learning models trained on processed weather data. This project allows users to input a specific date and hour to view 12-hour ahead forecasts of temperature and humidity.

[**Live Demo on Hugging Face Spaces**](https://huggingface.co/spaces/Apil31/weathee-Prediction)

## Project Overview

This project was built entirely on **Google Colab using a smartphone** and leverages a machine learning pipeline to predict **temperature (°C)** and **humidity (%)** on an hourly scale. The predictions are visualized interactively using **Plotly charts** embedded in a Streamlit app.

## Features

- Predict **temperature and humidity** for the next 12 hours.
- Input interface for selecting **date** and **hour**.
- Dynamic and responsive **Plotly visualizations**.
- Real-time forecast simulation (currently using dummy data).
- Mobile-friendly interface.

## Tech Stack

- **Python**
- **Streamlit** – for the interactive dashboard
- **Scikit-learn** – for building ML pipelines
- **Pandas** – for data handling
- **Plotly** – for visualization
- **Google Colab** – development and training environment (mobile)
- **Hugging Face Spaces** – deployment platform

## Model Details

The project uses two separate ML pipelines:

- `pipeline_temp`: Predicts temperature using features like `wind_kph`, `temp_diff`, `hour`, `temp_ma_3`, etc.
- `pipeline_hum`: Predicts humidity using similar and complementary features.

Both pipelines are saved and loaded from a `final_weather_prediction_model.pkl` file, which contains the serialized scikit-learn pipelines.

## How It Works

1. User selects a **date** and **hour**.
2. The app simulates **12-hour future** input data (dummy values or real-time integration if available).
3. Pre-trained models predict the **temperature** and **humidity** for the upcoming hours.
4. Predictions are displayed in both **tabular format** and **interactive Plotly line charts**.

## File Structure

```
.
├── app.py                        # Streamlit app file
├── requirements.txt             # Required Python packages
├── final_weather_prediction_model.pkl  # Trained model pipelines
└── README.md                    # This file
```

## Installation

To run this app locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/weather-dashboard.git
   cd weather-dashboard
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Deployment

The app is deployed at:  
[https://huggingface.co/spaces/Apil31/weathee-Prediction](https://huggingface.co/spaces/Apil31/weathee-Prediction)

## Next Steps

- Integrate real-time weather API (e.g., WeatherAPI or OpenWeatherMap).
- Improve model input by replacing dummy values.
- Add more weather features (rain, cloud cover, etc.)
- Improve UI/UX for mobile users.

## License

This project is open-source under the MIT License.


---

### Project by
**Havilz**

### Contact
- **Email:** havilzlating31@gmail.com  
- **WhatsApp:** +62 813-801-008-65
