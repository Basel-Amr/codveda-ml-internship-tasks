import joblib
import os
from rich.console import Console

console = Console()

def save_scaler(scaler, num_cols, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump((scaler, num_cols), filepath)
    console.print(f"[green]💾 Scaler saved at {filepath}")

def load_scaler(filepath):
    """
    Load a saved scaler and numerical column list from disk.
    
    Args:
        filepath (str): Path to the saved scaler .pkl file.
    
    Returns:
        (scaler, num_cols): The scaler object and list of numerical columns.
    """
    if not os.path.exists(filepath):
        console.print(f"[red]❌ Scaler not found at {filepath}")
        return None, None

    try:
        scaler, num_cols = joblib.load(filepath)
        console.print(f"[green]✅ Scaler loaded from {filepath}")
        console.print(f"[cyan]📦 Scaler type:[/cyan] {type(scaler)}")
        console.print(f"[magenta]🔢 Numerical columns:[/magenta] {num_cols}")
        return scaler, num_cols
    except Exception as e:
        console.print(f"[red]❌ Failed to load scaler: {e}")
        return None, None
