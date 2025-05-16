class AlgorithmVisualizer:
    """算法可视化工具 - 展示排序/搜索过程"""
    def execute(self, algorithm=None, data=None):
        # 支持冒泡排序、插入排序、选择排序三种算法的可视化文本演示
        if not algorithm or not data:
            return "请提供算法名（bubble/insert/select）和数据（如1,3,2,5）"
        try:
            arr = [int(x) for x in str(data).replace('，', ',').split(',') if x.strip()]
        except Exception:
            return "数据格式错误，应为逗号分隔的数字，如1,2,3"
        steps = []
        if algorithm.lower() == 'bubble':
            steps.append(f"初始: {arr}")
            n = len(arr)
            for i in range(n):
                for j in range(0, n-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        steps.append(f"交换第{j+1}和{j+2}位: {arr}")
            steps.append(f"结果: {arr}")
        elif algorithm.lower() == 'insert':
            steps.append(f"初始: {arr}")
            for i in range(1, len(arr)):
                key = arr[i]
                j = i-1
                while j >= 0 and arr[j] > key:
                    arr[j+1] = arr[j]
                    j -= 1
                arr[j+1] = key
                steps.append(f"插入第{i+1}位: {arr}")
            steps.append(f"结果: {arr}")
        elif algorithm.lower() == 'select':
            steps.append(f"初始: {arr}")
            n = len(arr)
            for i in range(n):
                min_idx = i
                for j in range(i+1, n):
                    if arr[j] < arr[min_idx]:
                        min_idx = j
                if min_idx != i:
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]
                    steps.append(f"交换第{i+1}和{min_idx+1}位: {arr}")
            steps.append(f"结果: {arr}")
        else:
            return "暂仅支持 bubble/insert/select 三种排序算法"
        return '\n'.join(steps)
