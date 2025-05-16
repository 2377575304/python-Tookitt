import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QPushButton, QTextEdit, QLineEdit, QFormLayout, QScrollArea, QMessageBox, QTreeWidget, QTreeWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from tools.toolkit import TOOLS
import inspect
import importlib

class ToolWidget(QWidget):
    def __init__(self, tool_name, tool_class):
        super().__init__()
        self.tool_name = tool_name
        self.tool_class = tool_class
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        # 美化标题和说明，增加日期格式提示
        if self.tool_name == '纪念日倒计时':
            desc = f"<h2 style='color:#2d8cf0'>{self.tool_name}</h2>"
            desc += f"<div style='color:#666'>{self.tool_class.__doc__ or ''}<br>"
            desc += "<span style='color:#888;font-size:12px'>日期格式：2025-12-31、2025/12/31、2025.12.31</span></div>"
        else:
            desc = f"<h2 style='color:#2d8cf0'>{self.tool_name}</h2><div style='color:#666'>{self.tool_class.__doc__ or ''}</div>"
        self.desc_label = QLabel(desc)
        self.desc_label.setWordWrap(True)
        layout.addWidget(self.desc_label)
        self.param_inputs = {}
        self.form_layout = QFormLayout()
        # 反射获取参数
        method = getattr(self.tool_class, 'execute', None)
        if method:
            sig = inspect.signature(method)
            for name, param in sig.parameters.items():
                if name == 'self':
                    continue
                le = QLineEdit()
                le.setPlaceholderText(f"{name}")
                if self.tool_name == '纪念日倒计时' and name == 'target_date':
                    le.setPlaceholderText("如 2025-12-31")
                self.param_inputs[name] = le
                self.form_layout.addRow(name, le)
        layout.addLayout(self.form_layout)
        self.run_btn = QPushButton("执行")
        self.run_btn.setStyleSheet("background:#2d8cf0;color:white;font-weight:bold;height:32px")
        self.run_btn.clicked.connect(self.run_tool)
        layout.addWidget(self.run_btn)
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("background:#f6f8fa;font-size:30px")  # 字体更大
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
        # 分类数据
        self.tool_categories = {
            '文件与目录': [
                '批量文件重命名','重复文件清理','文件夹同步','文件类型分类','大文件查找','临时文件清理','文件加密/解密','PDF合并拆分','图片格式转换','目录树生成',
                'Excel处理','CSV转JSON','Markdown转HTML','数据库浏览','PDF文本提取','图片水印添加','图片压缩','电子书管理','垃圾分类查询'
            ],
            '网络与数据': [
                '网页截图','RSS阅读器','简易爬虫','链接有效性检查','社交媒体下载','邮件自动发送','网络速度测试','IP地理位置查询','端口扫描','种子解析',
                '快递追踪','汇率转换','天气查询','食谱推荐','随机决定','密码强度检测','纪念日倒计时','BMI计算'
            ],
            '多媒体处理': [
                '视频转GIF','音频格式转换','屏幕录制','表情包生成','ASCII艺术生成','照片滤镜','音频剪辑','视频字幕生成','颜色拾取','简谱生成','单词发音','汉字笔顺动画'
            ],
            '自动化与效率': [
                '定时任务调度','剪贴板历史','动作录制','桌面便签','快捷启动','自动填写表单','会议记录生成','代码片段管理','双因素认证','算法可视化',
                '数据可视化仪表盘','日志分析','密码生成'
            ],
            '学习与娱乐': [
                '文字冒险游戏','贪吃蛇游戏','2048游戏','迷宫生成','骰子模拟','密码破解模拟','ASCII游戏集合','股票模拟交易','电子宠物','歌词生成',
                '单词记忆卡片','数学公式生成','编程题评判','历史时间轴','随机知识问答','化学方程式配平'
            ]
        }
        # 中文名到TOOLS key的手动映射，确保所有主界面工具都能正确启动
        self.tool_name_map = {
            '批量文件重命名': 'batch_rename',
            '重复文件清理': 'duplicate_clear',
            '文件夹同步': 'folder_sync',
            '文件类型分类': 'file_type_classifier',
            '大文件查找': 'large_file_finder',
            '临时文件清理': 'temp_file_cleaner',
            '文件加密/解密': 'file_encryptor',
            'PDF合并拆分': 'pdf_merger_splitter',
            '图片格式转换': 'image_format_converter',
            '目录树生成': 'directory_tree_generator',
            'Excel处理': 'excel_processor',
            'CSV转JSON': 'csv_to_json_converter',
            'Markdown转HTML': 'markdown_to_html_converter',
            '数据库浏览': 'sqlite_browser',
            'PDF文本提取': 'pdf_text_extractor',
            '图片水印添加': 'image_watermarker',
            '图片压缩': 'batch_image_compressor',
            '电子书管理': 'ebook_manager',
            '垃圾分类查询': 'garbage_sort_query',
            '网页截图': 'web_screenshot',
            'RSS阅读器': 'rss_reader',
            '简易爬虫': 'simple_crawler',
            '链接有效性检查': 'link_checker',
            '社交媒体下载': 'social_media_downloader',
            '邮件自动发送': 'email_sender',
            '网络速度测试': 'network_speed_tester',
            'IP地理位置查询': 'ip_geo_locator',
            '端口扫描': 'port_scanner',
            '种子解析': 'torrent_info_parser',
            '快递追踪': 'express_tracker',
            '汇率转换': 'currency_converter',
            '天气查询': 'weather_query',
            '食谱推荐': 'recipe_recommender',
            '随机决定': 'random_decision_maker',
            '密码强度检测': 'password_strength_checker',
            '纪念日倒计时': 'anniversary_countdown',
            'BMI计算': 'bmi_calculator',
            '视频转GIF': 'video_to_gif_converter',
            '音频格式转换': 'audio_format_converter',
            '屏幕录制': 'screen_recorder',
            '表情包生成': 'meme_generator',
            'ASCII艺术生成': 'ascii_art_generator',
            '照片滤镜': 'photo_filter_applier',
            '音频剪辑': 'audio_editor',
            '视频字幕生成': 'video_subtitle_generator',
            '颜色拾取': 'color_picker',
            '简谱生成': 'simple_score_generator',
            '单词发音': 'english_word_speaker',
            '汉字笔顺动画': 'hanzi_stroke_animator',
            '定时任务调度': 'task_scheduler',
            '剪贴板历史': 'clipboard_history_manager',
            '动作录制': 'macro_recorder',
            '桌面便签': 'desktop_note',
            '快捷启动': 'quick_launch_panel',
            '自动填写表单': 'web_form_auto_filler',
            '会议记录生成': 'meeting_note_generator',
            '代码片段管理': 'code_snippet_manager',
            '双因素认证': 'two_factor_auth_generator',
            '算法可视化': 'algorithm_visualizer',
            '数据可视化仪表盘': 'data_viz_dashboard',
            '日志分析': 'log_analyzer',
            '密码生成': 'password_generator',
            '文字冒险游戏': 'text_adventure_engine',
            '贪吃蛇游戏': 'snake_game',
            '2048游戏': 'game_2048',
            '迷宫生成': 'maze_generator',
            '骰子模拟': 'dice_simulator',
            '密码破解模拟': 'password_crack_simulator',
            'ASCII游戏集合': 'ascii_game_collection',
            '股票模拟交易': 'stock_simulator',
            '电子宠物': 'virtual_pet',
            '歌词生成': 'lyrics_generator',
            '单词记忆卡片': 'word_flashcard',
            '数学公式生成': 'math_formula_generator',
            '编程题评判': 'code_judge',
            '历史时间轴': 'history_timeline',
            '随机知识问答': 'random_quiz',
            '化学方程式配平': 'chemical_equation_balancer',
        }
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        # 搜索栏放在顶部
        search_layout = QHBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText('🔍 搜索工具名称...')
        self.search_box.setStyleSheet('font-size:16px;padding:6px;border-radius:6px;border:1px solid #d0d0d0;')
        self.search_box.textChanged.connect(self.filter_tools)
        search_layout.addWidget(self.search_box)
        main_layout.addLayout(search_layout)
        # 主体区域（左树右详情）
        content_layout = QHBoxLayout()
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabel('工具分类')
        self.icon_map = {
            '文件与目录': QIcon.fromTheme('folder'),
            '网络与数据': QIcon.fromTheme('network-server'),
            '多媒体处理': QIcon.fromTheme('media-playback-start'),
            '自动化与效率': QIcon.fromTheme('system-run'),
            '学习与娱乐': QIcon.fromTheme('applications-games'),
        }
        for cat, tools in self.tool_categories.items():
            cat_item = QTreeWidgetItem([cat])
            if self.icon_map.get(cat):
                cat_item.setIcon(0, self.icon_map[cat])
            for tool in tools:
                tool_item = QTreeWidgetItem([tool])
                # 可自定义更多图标映射
                if 'PDF' in tool or '文档' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('application-pdf'))
                elif '图片' in tool or '图像' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('image-x-generic'))
                elif '音频' in tool or '音乐' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('audio-x-generic'))
                elif '视频' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('video-x-generic'))
                elif '游戏' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('applications-games'))
                elif '网络' in tool or 'IP' in tool or '端口' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('network-server'))
                elif '加密' in tool or '密码' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('emblem-readonly'))
                elif 'Excel' in tool or 'CSV' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('x-office-spreadsheet'))
                elif '数据库' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('database'))
                elif '二维码' in tool:
                    tool_item.setIcon(0, QIcon.fromTheme('qrcode'))
                cat_item.addChild(tool_item)
            self.tree_widget.addTopLevelItem(cat_item)
        self.tree_widget.expandAll()
        self.tree_widget.itemClicked.connect(self.on_tree_item_clicked)
        content_layout.addWidget(self.tree_widget, 2)
        # 工具详情区
        self.tool_area = QScrollArea()
        self.tool_area.setWidgetResizable(True)
        content_layout.addWidget(self.tool_area, 5)
        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def filter_tools(self, text):
        text = text.strip()
        for i in range(self.tree_widget.topLevelItemCount()):
            cat_item = self.tree_widget.topLevelItem(i)
            show_cat = False
            for j in range(cat_item.childCount()):
                tool_item = cat_item.child(j)
                tool_name = tool_item.text(0)
                match = text in tool_name or not text
                tool_item.setHidden(not match)
                if match:
                    show_cat = True
            cat_item.setHidden(not show_cat)

    def on_tree_item_clicked(self, item, column):
        if item.childCount() == 0:
            zh_name = item.text(0)
            tool_key = self.tool_name_map.get(zh_name)
            if tool_key and tool_key in TOOLS:
                tool_class = TOOLS[tool_key]
                widget = ToolWidget(zh_name, tool_class)
                self.tool_area.setWidget(widget)
            else:
                QMessageBox.warning(self, "工具未找到", f"未找到工具：{zh_name}\n注册名：{tool_key}")

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
