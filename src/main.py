import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QPushButton, QTextEdit, QLineEdit, QFormLayout, QScrollArea, QMessageBox
)
from PyQt5.QtCore import Qt
from tools.toolkit import TOOLS

class ToolWidget(QWidget):
    def __init__(self, tool_name, tool_class):
        super().__init__()
        self.tool_name = tool_name
        self.tool_class = tool_class
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.desc_label = QLabel(f"<b>{self.tool_name}</b><br>{self.tool_class.__doc__ or ''}")
        layout.addWidget(self.desc_label)
        self.param_inputs = {}
        self.form_layout = QFormLayout()
        # 反射获取参数
        import inspect
        method = getattr(self.tool_class, 'execute', None)
        if method:
            sig = inspect.signature(method)
            for name, param in sig.parameters.items():
                if name == 'self':
                    continue
                le = QLineEdit()
                le.setPlaceholderText(f"{name}")
                self.param_inputs[name] = le
                self.form_layout.addRow(name, le)
        layout.addLayout(self.form_layout)
        self.run_btn = QPushButton("执行")
        self.run_btn.clicked.connect(self.run_tool)
        layout.addWidget(self.run_btn)
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)
        self.setLayout(layout)

    def run_tool(self):
        params = {}
        for k, v in self.param_inputs.items():
            val = v.text()
            params[k] = val if val else None
        try:
            tool = self.tool_class()
            result = tool.execute(**params) if params else tool.execute()
            self.output.setText(str(result))
        except Exception as e:
            self.output.setText(f"出错: {e}")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Toolkit App")
        self.resize(900, 600)
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()
        # 工具分类
        self.tool_categories = {
            '文件与目录': [
                '批量文件重命名','重复文件清理','文件夹同步','文件类型分类','大文件查找','临时文件清理','文件加密/解密','PDF合并拆分','图片格式转换','目录树生成','Excel处理','CSV转JSON','Markdown转HTML','数据库浏览','PDF文本提取','图片水印添加','图片压缩','电子书管理','垃圾分类查询'
            ],
            '网络与数据': [
                '网页截图','RSS阅读器','简易爬虫','链接有效性检查','社交媒体下载','邮件自动发送','网络速度测试','IP地理位置查询','端口扫描','种子解析','快递追踪','汇率转换','天气查询','食谱推荐','随机决定','快递追踪','密码强度检测','纪念日倒计时','BMI计算'
            ],
            '多媒体处理': [
                '视频转GIF','音频格式转换','屏幕录制','表情包生成','ASCII艺术生成','照片滤镜','音频剪辑','视频字幕生成','颜色拾取','简谱生成','单词发音','汉字笔顺动画'
            ],
            '自动化与效率': [
                '定时任务调度','剪贴板历史','动作录制','桌面便签','快捷启动','自动填写表单','会议记录生成','代码片段管理','双因素认证','算法可视化','数据可视化仪表盘','日志分析','密码生成'
            ],
            '学习与娱乐': [
                '文字冒险游戏','贪吃蛇游戏','2048游戏','迷宫生成','骰子模拟','密码破解模拟','ASCII游戏集合','股票模拟交易','电子宠物','歌词生成','单词记忆卡片','数学公式生成','编程题评判','历史时间轴','随机知识问答','化学方程式配平'
            ]
        }
        self.tool_name_map = {
            'batch_rename': '批量文件重命名',
            'duplicate_clear': '重复文件清理',
            'folder_sync': '文件夹同步',
            'file_type_classifier': '文件类型分类',
            'large_file_finder': '大文件查找',
            'temp_file_cleaner': '临时文件清理',
            'file_encryptor': '文件加密/解密',
            'pdf_merger_splitter': 'PDF合并拆分',
            'image_format_converter': '图片格式转换',
            'directory_tree_generator': '目录树生成',
            'web_screenshot': '网页截图',
            'rss_reader': 'RSS阅读器',
            'simple_crawler': '简易爬虫',
            'link_checker': '链接有效性检查',
            'social_media_downloader': '社交媒体下载',
            'email_sender': '邮件自动发送',
            'network_speed_tester': '网络速度测试',
            'ip_geo_locator': 'IP地理位置查询',
            'port_scanner': '端口扫描',
            'torrent_info_parser': '种子解析',
            'excel_processor': 'Excel处理',
            'csv_to_json_converter': 'CSV转JSON',
            'data_viz_dashboard': '数据可视化仪表盘',
            'log_analyzer': '日志分析',
            'password_generator': '密码生成',
            'qrcode_generator': '二维码生成',
            'barcode_reader': '条形码识别',
            'markdown_to_html_converter': 'Markdown转HTML',
            'sqlite_browser': '数据库浏览',
            'pdf_text_extractor': 'PDF文本提取',
            'video_to_gif_converter': '视频转GIF',
            'audio_format_converter': '音频格式转换',
            'screen_recorder': '屏幕录制',
            'image_watermarker': '图片水印添加',
            'meme_generator': '表情包生成',
            'ascii_art_generator': 'ASCII艺术生成',
            'photo_filter_applier': '照片滤镜',
            'audio_editor': '音频剪辑',
            'video_subtitle_generator': '视频字幕生成',
            'color_picker': '颜色拾取',
            'task_scheduler': '定时任务调度',
            'clipboard_history_manager': '剪贴板历史',
            'macro_recorder': '动作录制',
            'batch_image_compressor': '图片压缩',
            'desktop_note': '桌面便签',
            'quick_launch_panel': '快捷启动',
            'web_form_auto_filler': '自动填写表单',
            'meeting_note_generator': '会议记录生成',
            'code_snippet_manager': '代码片段管理',
            'two_factor_auth_generator': '双因素认证',
            'text_adventure_engine': '文字冒险游戏',
            'snake_game': '贪吃蛇游戏',
            'game_2048': '2048游戏',
            'maze_generator': '迷宫生成',
            'dice_simulator': '骰子模拟',
            'password_crack_simulator': '密码破解模拟',
            'ascii_game_collection': 'ASCII游戏集合',
            'stock_simulator': '股票模拟交易',
            'virtual_pet': '电子宠物',
            'lyrics_generator': '歌词生成',
            'word_flashcard': '单词记忆卡片',
            'math_formula_generator': '数学公式生成',
            'code_judge': '编程题评判',
            'hanzi_stroke_animator': '汉字笔顺动画',
            'chemical_equation_balancer': '化学方程式配平',
            'simple_score_generator': '简谱生成',
            'english_word_speaker': '单词发音',
            'algorithm_visualizer': '算法可视化',
            'history_timeline': '历史时间轴',
            'random_quiz': '随机知识问答',
            'weather_query': '天气查询',
            'currency_converter': '汇率转换',
            'express_tracker': '快递追踪',
            'recipe_recommender': '食谱推荐',
            'password_strength_checker': '密码强度检测',
            'anniversary_countdown': '纪念日倒计时',
            'bmi_calculator': 'BMI计算',
            'random_decision_maker': '随机决定',
            'ebook_manager': '电子书管理',
            'garbage_sort_query': '垃圾分类查询',
        }
        self.tool_key_map = {v: k for k, v in self.tool_name_map.items()}
        # 分类树形列表
        from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabel('工具分类')
        for cat, tools in self.tool_categories.items():
            cat_item = QTreeWidgetItem([cat])
            for tool in tools:
                tool_item = QTreeWidgetItem([tool])
                cat_item.addChild(tool_item)
            self.tree_widget.addTopLevelItem(cat_item)
        self.tree_widget.expandAll()
        self.tree_widget.itemClicked.connect(self.on_tree_item_clicked)
        main_layout.addWidget(self.tree_widget, 2)
        # 工具详情区
        self.tool_area = QScrollArea()
        self.tool_area.setWidgetResizable(True)
        main_layout.addWidget(self.tool_area, 5)
        self.setLayout(main_layout)

    def on_tree_item_clicked(self, item, column):
        # 只响应叶子节点（工具）
        if item.childCount() == 0:
            zh_name = item.text(0)
            tool_key = self.tool_key_map.get(zh_name, zh_name)
            if tool_key in TOOLS:
                tool_class = TOOLS[tool_key]
                widget = ToolWidget(zh_name, tool_class)
                self.tool_area.setWidget(widget)

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()