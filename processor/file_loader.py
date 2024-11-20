import pandas as pd

def load_file(filepath):
    """加载文件"""
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        return pd.read_excel(filepath)
    else:
        raise ValueError("不支持的文件格式！仅支持CSV和Excel文件。")

