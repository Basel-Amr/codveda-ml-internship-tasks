import joblib
import os
from rich.console import Console
import sqlite3
from datetime import datetime
import pandas as pd
console = Console()

def save_model(model, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)
    console.print(f"[green]💾 Model saved at {filepath}")

def load_model(filepath):
    """
    Load a trained ML model from disk.
    
    Args:
        filepath (str): Path to the saved model .pkl file.
    
    Returns:
        model: The loaded model object or None if failed.
    """
    if not os.path.exists(filepath):
        console.print(f"[red]❌ Model not found at {filepath}")
        return None

    try:
        model = joblib.load(filepath)
        console.print(f"[green]✅ Model loaded from {filepath}")
        console.print(f"[cyan]📦 Model type:[/cyan] {type(model)}")
        return model
    except Exception as e:
        console.print(f"[red]❌ Failed to load model: {e}")
        return None

def save_prediction(sepal_length, sepal_width, petal_length, petal_width, predicted_class):
    conn = sqlite3.connect("models/iris_history.db")
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sepal_length REAL NOT NULL,
        sepal_width REAL NOT NULL,
        petal_length REAL NOT NULL,
        petal_width REAL NOT NULL,
        predicted_class TEXT NOT NULL,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Insert the new prediction
    cursor.execute("""
    INSERT INTO predictions (sepal_length, sepal_width, petal_length, petal_width, predicted_class)
    VALUES (?, ?, ?, ?, ?)
    """, (sepal_length, sepal_width, petal_length, petal_width, predicted_class))
    
    conn.commit()
    conn.close()

def get_prediction_history(limit=100):
    """
    Fetch the latest prediction history from the database.
    :param limit: number of records to fetch
    :return: pandas DataFrame
    """
    conn = sqlite3.connect("models/iris_history.db")
    cursor = conn.cursor()
    
    cursor.execute(f"""
        SELECT sepal_length, sepal_width, petal_length, petal_width, predicted_class, timestamp
        FROM predictions
        ORDER BY timestamp DESC
        LIMIT {limit}
    """)
    
    rows = cursor.fetchall()
    conn.close()
    
    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=[
        "Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Predicted Class", "Timestamp"
    ])
    return df
