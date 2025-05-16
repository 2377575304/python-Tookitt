class GarbageSortQuery:
    """垃圾分类查询 - 输入物品返回分类结果"""
    def execute(self, item=None):
        print(f"[GarbageSortQuery] 垃圾分类: {item}")
        return "可回收物"
