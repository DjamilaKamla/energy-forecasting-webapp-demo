import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Energy Forecasting – Demo", layout="centered")

st.title("Energy Forecasting Webapp – Demo")
st.write(
    "Cette application illustre un exemple simplifié de prévision de production énergétique."
)

# 1. Génération de données fictives
np.random.seed(42)
n_days = 200
dates = pd.date_range(start="2024-01-01", periods=n_days, freq="D")

trend = np.linspace(50, 70, n_days)              # tendance douce
seasonality = 5 * np.sin(np.linspace(0, 6, n_days))  # pseudo saisonnalité
noise = np.random.normal(0, 3, n_days)

production = trend + seasonality + noise

df = pd.DataFrame({
    "date": dates,
    "production_MWh": production
}).set_index("date")

st.subheader("Série historique - production quotidienne fictive (MWh)")
st.line_chart(df["production_MWh"])

# 2. "Forecast" très simple = moyenne mobile
window = st.slider("Fenêtre de moyenne mobile (jours)", min_value=5, max_value=30, value=14)

df["rolling_mean"] = df["production_MWh"].rolling(window=window).mean()

# Prévision naïve : on prolonge la dernière moyenne
forecast_horizon = st.slider("Horizon de prévision (jours)", min_value=7, max_value=60, value=30)

last_mean = df["rolling_mean"].iloc[-1]
future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=forecast_horizon, freq="D")
future_prod = np.full(shape=forecast_horizon, fill_value=last_mean)

df_future = pd.DataFrame({
    "date": future_dates,
    "forecast_MWh": future_prod
}).set_index("date")

st.subheader("Historique + prévision simple")
fig, ax = plt.subplots()
ax.plot(df.index, df["production_MWh"], label="Historique", alpha=0.6)
ax.plot(df.index, df["rolling_mean"], label=f"Moyenne mobile ({window} j)", linewidth=2)
ax.plot(df_future.index, df_future["forecast_MWh"], label="Prévision", linestyle="--")
ax.set_xlabel("Date")
ax.set_ylabel("Production (MWh)")
ax.legend()
st.pyplot(fig)

st.subheader("Interprétation business (exemple)")

if last_mean > df["production_MWh"].mean():
    msg = (
        "La tendance récente est légèrement **supérieure** à la moyenne historique. "
        "Cela peut refléter une période de bonne disponibilité ou une montée en puissance du parc. "
        "À surveiller pour ajuster les engagements de vente."
    )
else:
    msg = (
        "La tendance récente est **inférieure** à la moyenne historique. "
        "Cela peut signaler une baisse de performance ou des contraintes techniques. "
        "Il est pertinent de revoir les hypothèses utilisées dans les prévisions de vente."
    )

st.write(msg)
