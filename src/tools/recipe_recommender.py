class RecipeRecommender:
    """食谱推荐系统 - 根据食材推荐菜谱（演示）"""
    def execute(self, ingredients=None):
        if not ingredients:
            return "请提供食材，多个用逗号分隔"
        # 演示推荐
        ings = [x.strip() for x in str(ingredients).replace('，', ',').split(',') if x.strip()]
        if '鸡蛋' in ings:
            return "推荐：西红柿炒鸡蛋、鸡蛋羹、蛋炒饭"
        if '土豆' in ings:
            return "推荐：土豆炖牛肉、土豆丝、薯条"
        return f"推荐：{ings[0]}炒饭、{ings[0]}汤（演示）"
