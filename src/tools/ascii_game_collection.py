import random

class ASCIIGameCollection:
    """ASCII游戏集合 - 俄罗斯方块/吃豆人等（演示版，内置贪吃蛇/猜数字/井字棋）"""
    def execute(self, game_name=None):
        if not game_name:
            return "可选游戏：snake（贪吃蛇）、guess（猜数字）、tictactoe（井字棋）\n如需体验请输入 game_name 参数。"
        if game_name.lower() == 'snake':
            return self.snake_demo()
        elif game_name.lower() == 'guess':
            return self.guess_demo()
        elif game_name.lower() == 'tictactoe':
            return self.tictactoe_demo()
        else:
            return "暂仅支持 snake/guess/tictactoe 三种小游戏（文本演示版）"

    def snake_demo(self):
        return (
            "贪吃蛇演示：\n"
            "+----------+\n"
            "|          |\n"
            "|   ooo*   |\n"
            "|          |\n"
            "+----------+\n"
            "（此为静态演示，完整版请用独立贪吃蛇工具）"
        )

    def guess_demo(self):
        secret = random.randint(1, 10)
        return (
            f"猜数字演示：\n我想了一个1~10的数字，比如 {secret}。\n你可以在终端输入数字尝试猜测。\n（此为静态演示，完整版请用独立猜数字游戏）"
        )

    def tictactoe_demo(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', ' '],
            [' ', 'O', 'X']
        ]
        s = '井字棋演示：\n'
        for row in board:
            s += ' | '.join(row) + '\n'
        s += "（此为静态演示，完整版请用独立井字棋工具）"
        return s
