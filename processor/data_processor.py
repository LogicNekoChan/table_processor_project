def process_data(data):
    """处理数据：自定义数据逻辑"""
    if data is not None:
        # 示例：删除空值，按某列排序
        data.dropna(inplace=True)
        if 'column_name' in data.columns:  # 替换为实际列名
            data.sort_values(by='column_name', inplace=True)
    return data

