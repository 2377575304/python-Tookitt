class CodeSnippetManager:
    """代码片段管理器 - 分类存储常用代码块（演示）"""
    def execute(self, action=None, snippet=None):
        # 实际可用数据库/文件，这里演示
        if action == 'add':
            return f"已添加代码片段：{snippet or '[空]'}（演示）"
        elif action == 'list':
            return "代码片段列表：print('Hello'), for i in range(10): ...（演示）"
        else:
            return "请指定action参数（add/list）"
