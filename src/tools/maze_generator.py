class MazeGenerator:
    """迷宫生成器 - 随机生成可解迷宫（演示）"""
    def execute(self, width=None, height=None):
        try:
            w = int(width) if width else 8
            h = int(height) if height else 5
        except Exception:
            w, h = 8, 5
        maze = ['#' * (w+2)]
        for i in range(h):
            row = '#' + ' ' * w + '#'
            maze.append(row)
        maze.append('#' * (w+2))
        maze[1] = maze[1][:1] + 'S' + maze[1][2:]
        maze[-2] = maze[-2][:-2] + 'E' + maze[-2][-1:]
        return '\n'.join(maze) + '\nS=起点 E=终点（演示）'
