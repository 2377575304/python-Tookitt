class GarbageSortQuery:
    """垃圾分类查询 - 输入物品返回分类结果（演示）"""
    def execute(self, item=None):
        if not item:
            return "请提供物品名称"
        if '电池' in item:
            return "有害垃圾"
        if '纸' in item or '瓶' in item:
            return "可回收物"
        if '果皮' in item or '剩饭' in item:
            return "厨余垃圾"
        return "其他垃圾"
