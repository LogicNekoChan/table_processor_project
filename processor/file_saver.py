def save_file(data, filepath):
    """保存文件"""
    if filepath.endswith('.csv'):
        data.to_csv(filepath, index=False)
    elif filepath.endswith('.xlsx'):
        data.to_excel(filepath, index=False)
    else:
        raise ValueError("不支持的文件格式！")
