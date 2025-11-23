# Energy Forecasting Webapp 

Cette application Streamlit est une **démo minimale** d’outil de prévision de séries temporelles
appliquée à une production énergétique fictive.

Objectif :
- illustrer la capacité à **concevoir un outil d’aide à la décision**,
- intégrer un modèle simple de forecasting,
- proposer une visualisation et une lecture business.

---

## 1. Fonctionnalités

- Génération d’une série de production quotidienne fictive.
- Ajustement d’un modèle de prévision simple (moyenne mobile).
- Visualisation :
  - historique,
  - prévisions à court terme.
- Message d’interprétation business (tendance, volatilité).

---

## 👩‍💻 Auteure

**Djamila Kamla Fares**  
Master 2 Economic Analysis — CY Cergy / ESSEC  
📧 faresdjamila@gmail.com  
📍 Île-de-France  

---

## 2. Lancer l’application

```bash
pip install streamlit pandas numpy matplotlib
streamlit run app.py
