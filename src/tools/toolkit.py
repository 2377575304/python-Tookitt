from .batch_rename import BatchRenameTool
from .folder_sync import FolderSyncTool
from .file_type_classifier import FileTypeClassifier
from .large_file_finder import LargeFileFinder
from .temp_file_cleaner import TempFileCleaner
from .file_encryptor import FileEncryptor
from .pdf_merger_splitter import PDFMergerSplitter
from .image_format_converter import ImageFormatConverter
from .directory_tree_generator import DirectoryTreeGenerator
from .web_screenshot import WebScreenshotTool
from .rss_reader import RSSReader
from .simple_crawler import SimpleCrawler
from .link_checker import LinkChecker
from .social_media_downloader import SocialMediaDownloader
from .email_sender import EmailSender
from .network_speed_tester import NetworkSpeedTester
from .ip_geo_locator import IPGeoLocator
from .port_scanner import PortScanner
from .torrent_info_parser import TorrentInfoParser
from .excel_processor import ExcelProcessor
from .csv_to_json_converter import CSVtoJSONConverter
from .data_viz_dashboard import DataVizDashboard
from .log_analyzer import LogAnalyzer
from .password_generator import PasswordGenerator
from .qrcode_generator import QRCodeGenerator
from .barcode_reader import BarcodeReader
from .markdown_to_html_converter import MarkdownToHTMLConverter
from .sqlite_browser import SQLiteBrowser
from .pdf_text_extractor import PDFTextExtractor
from .video_to_gif_converter import VideoToGIFConverter
# from .audio_format_converter import AudioFormatConverter
# from .audio_editor import AudioEditor
from .screen_recorder import ScreenRecorder
from .image_watermarker import ImageWatermarker
from .meme_generator import MemeGenerator
from .ascii_art_generator import ASCIIArtGenerator
from .photo_filter_applier import PhotoFilterApplier
from .video_subtitle_generator import VideoSubtitleGenerator
from .color_picker import ColorPicker
from .task_scheduler import TaskScheduler
from .clipboard_history_manager import ClipboardHistoryManager
from .macro_recorder import MacroRecorder
from .batch_image_compressor import BatchImageCompressor
from .desktop_note import DesktopNote
from .quick_launch_panel import QuickLaunchPanel
from .web_form_auto_filler import WebFormAutoFiller
from .meeting_note_generator import MeetingNoteGenerator
from .code_snippet_manager import CodeSnippetManager
from .two_factor_auth_generator import TwoFactorAuthGenerator
from .text_adventure_engine import TextAdventureEngine
from .snake_game import SnakeGame
from .game_2048 import Game2048
from .maze_generator import MazeGenerator
from .dice_simulator import DiceSimulator
from .password_crack_simulator import PasswordCrackSimulator
from .ascii_game_collection import ASCIIGameCollection
from .stock_simulator import StockSimulator
from .virtual_pet import VirtualPet
from .lyrics_generator import LyricsGenerator
from .word_flashcard import WordFlashcard
from .math_formula_generator import MathFormulaGenerator
from .code_judge import CodeJudge
from .hanzi_stroke_animator import HanziStrokeAnimator
from .chemical_equation_balancer import ChemicalEquationBalancer
from .simple_score_generator import SimpleScoreGenerator
from .english_word_speaker import EnglishWordSpeaker
from .algorithm_visualizer import AlgorithmVisualizer
from .history_timeline import HistoryTimeline
from .random_quiz import RandomQuiz
from .weather_query import WeatherQuery
from .currency_converter import CurrencyConverter
from .express_tracker import ExpressTracker
from .recipe_recommender import RecipeRecommender
from .password_strength_checker import PasswordStrengthChecker
from .anniversary_countdown import AnniversaryCountdown
from .bmi_calculator import BMICalculator
from .random_decision_maker import RandomDecisionMaker
from .ebook_manager import EbookManager
from .garbage_sort_query import GarbageSortQuery

class ToolA:
    def execute(self):
        return "ToolA is executing."

class ToolB:
    def run(self):
        return "ToolB is running."

# 工具注册表，便于统一管理和调用
TOOLS = {
    'batch_rename': BatchRenameTool,
    'duplicate_clear': ToolA,  # 假设ToolA为重复文件清理器
    'folder_sync': FolderSyncTool,
    'file_type_classifier': FileTypeClassifier,
    'large_file_finder': LargeFileFinder,
    'temp_file_cleaner': TempFileCleaner,
    'file_encryptor': FileEncryptor,
    'pdf_merger_splitter': PDFMergerSplitter,
    'image_format_converter': ImageFormatConverter,
    'directory_tree_generator': DirectoryTreeGenerator,
    'web_screenshot': WebScreenshotTool,
    'rss_reader': RSSReader,
    'simple_crawler': SimpleCrawler,
    'link_checker': LinkChecker,
    'social_media_downloader': SocialMediaDownloader,
    'email_sender': EmailSender,
    'network_speed_tester': NetworkSpeedTester,
    'ip_geo_locator': IPGeoLocator,
    'port_scanner': PortScanner,
    'torrent_info_parser': TorrentInfoParser,
}

TOOLS.update({
    'excel_processor': ExcelProcessor,
    'csv_to_json_converter': CSVtoJSONConverter,
    'data_viz_dashboard': DataVizDashboard,
    'log_analyzer': LogAnalyzer,
    'password_generator': PasswordGenerator,
    'qrcode_generator': QRCodeGenerator,
    'barcode_reader': BarcodeReader,
    'markdown_to_html_converter': MarkdownToHTMLConverter,
    'sqlite_browser': SQLiteBrowser,
    'pdf_text_extractor': PDFTextExtractor,
    'video_to_gif_converter': VideoToGIFConverter,
    # 'audio_format_converter': AudioFormatConverter,
    # 'audio_editor': AudioEditor,
    'screen_recorder': ScreenRecorder,
    'image_watermarker': ImageWatermarker,
    'meme_generator': MemeGenerator,
    'ascii_art_generator': ASCIIArtGenerator,
    'photo_filter_applier': PhotoFilterApplier,
    'video_subtitle_generator': VideoSubtitleGenerator,
    'color_picker': ColorPicker,
    'task_scheduler': TaskScheduler,
    'clipboard_history_manager': ClipboardHistoryManager,
    'macro_recorder': MacroRecorder,
    'batch_image_compressor': BatchImageCompressor,
    'desktop_note': DesktopNote,
    'quick_launch_panel': QuickLaunchPanel,
    'web_form_auto_filler': WebFormAutoFiller,
    'meeting_note_generator': MeetingNoteGenerator,
    'code_snippet_manager': CodeSnippetManager,
    'two_factor_auth_generator': TwoFactorAuthGenerator,
    'text_adventure_engine': TextAdventureEngine,
    'snake_game': SnakeGame,
    'game_2048': Game2048,
    'maze_generator': MazeGenerator,
    'dice_simulator': DiceSimulator,
    'password_crack_simulator': PasswordCrackSimulator,
    'ascii_game_collection': ASCIIGameCollection,
    'stock_simulator': StockSimulator,
    'virtual_pet': VirtualPet,
    'lyrics_generator': LyricsGenerator,
    'word_flashcard': WordFlashcard,
    'math_formula_generator': MathFormulaGenerator,
    'code_judge': CodeJudge,
    'hanzi_stroke_animator': HanziStrokeAnimator,
    'chemical_equation_balancer': ChemicalEquationBalancer,
    'simple_score_generator': SimpleScoreGenerator,
    'english_word_speaker': EnglishWordSpeaker,
    'algorithm_visualizer': AlgorithmVisualizer,
    'history_timeline': HistoryTimeline,
    'random_quiz': RandomQuiz,
    'weather_query': WeatherQuery,
    'currency_converter': CurrencyConverter,
    'express_tracker': ExpressTracker,
    'recipe_recommender': RecipeRecommender,
    'password_strength_checker': PasswordStrengthChecker,
    'anniversary_countdown': AnniversaryCountdown,
    'bmi_calculator': BMICalculator,
    'random_decision_maker': RandomDecisionMaker,
    'ebook_manager': EbookManager,
    'garbage_sort_query': GarbageSortQuery,
})