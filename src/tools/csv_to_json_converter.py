import os
import csv
import json

class CSVtoJSONConverter:
    """CSV转JSON工具 - 支持将CSV文件批量或单个转换为JSON文件"""
    def execute(self, csv_path=None, json_path=None):
        if not csv_path or not json_path:
            return "请提供csv_path和json_path"
        if not os.path.exists(csv_path):
            return "CSV文件不存在"
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return f"转换完成，已保存到 {json_path}"
        except Exception as e:
            return f"转换失败: {e}"
