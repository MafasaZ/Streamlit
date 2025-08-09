# Titanic Survival Predictor

This project is a web application built with Python and Streamlit that predicts the survival of a passenger on the Titanic. The application uses a machine learning model (Random Forest Classifier) trained on the historical Titanic dataset. It features an interactive user interface for making predictions and provides data visualizations for exploration.

## Project Purpose

The primary goal of this project is to demonstrate a full end-to-end machine learning pipeline, from data analysis and model training to deployment. It serves as a practical example of how a trained model can be integrated into an interactive and user-friendly web application, making predictions accessible to a non-technical audience.

## How to Run the App Locally

To run this application on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MafasaZ/Streamlit.git](https://github.com/MafasaZ/Streamlit.git)
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv .venv
    .venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Train the model:**
    Open the Jupyter Notebook `notebooks/model_training.ipynb` and run all the cells. This will preprocess the data, train the model, and save it as `models/titanic_model.pkl`.

5.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

6.  The application will open in your default web browser at `http://localhost:8501`.

   ## Deployed Application

You can access the live version of the application on Streamlit Cloud via the following link:

[Titanic Survival Predictor App](https://mafasaz-streamlit-app-vyip1t.streamlit.app)



