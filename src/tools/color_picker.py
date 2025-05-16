class ColorPicker:
    """颜色拾取器 - 从屏幕取色并显示HEX值"""
    def execute(self, position=None):
        print(f"[ColorPicker] 取色: 位置={position}")
        return "#FF5733"
