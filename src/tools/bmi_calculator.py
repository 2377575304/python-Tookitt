class BMICalculator:
    """BMI计算器 - 身高体重健康指数"""
    def execute(self, height=None, weight=None):
        try:
            h = float(height) / 100 if float(height) > 10 else float(height)
            w = float(weight)
            bmi = w / (h * h)
            if bmi < 18.5:
                level = "偏瘦"
            elif bmi < 24:
                level = "正常"
            elif bmi < 28:
                level = "超重"
            else:
                level = "肥胖"
            return f"BMI={bmi:.2f}，{level}"
        except Exception:
            return "请输入正确的身高（cm）和体重（kg）"
