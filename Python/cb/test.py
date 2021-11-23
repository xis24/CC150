class C4:
    def __init__(self, row, col):
        self.board = [["_" for _ in range(col)] for _ in range(row)]
        # self.depth[i] means at the ith col, the row we are at
        self.depth = [row-1] * col
        self.cur_move = "X"
        self.row = row
        self.col = col

    def move(self, col):
        if col > self.col:
            raise Exception("exceed column bound")
        if self.depth[col] < 0:
            raise Exception("column is filled")
        if self.cur_move == "X":
            self.cur_move = "O"
        else:
            self.cur_move = "X"
        cur_row = self.depth[col]
        self.depth[col] -= 1
        self.board[cur_row][col] = self.cur_move
        print("added {} to row {} col {}".format(self.cur_move, cur_row, col))
        for row in self.board:
            print(row)
            print("\n")
        self.checkwin(cur_row, col)

    def checkwin(self, row, col):
        from collections import deque
        # row case
        cur_row = self.board[row]
        goal = (self.cur_move * 4)
        if goal in "".join(cur_row):
            print("winner is {} with horizontal".format(self.cur_move))
            return
        # column case
        cur_column = []
        for board_row in self.board:
            cur_column.append(board_row[col])
        if goal in "".join(cur_column):
            print("winner is {} vertical".format(self.cur_move))
            return
        # diagonal case, left to right
        cur_diag1 = []
        cur_diag2 = []
        tmp_row, tmp_col = row, col
        tmp2_row, tmp2_col = row, col
        for change in range(-3, 4, 1):
            tmp_row += change
            tmp_col += change
            #print("diag1 coord", tmp_row, tmp_col)
            if tmp_row >= 0 and tmp_col >= 0 and tmp_row < self.row and tmp_col < self.col:
                cur_diag1.append(self.board[tmp_row][tmp_col])
            tmp_row -= change
            tmp_col -= change

            tmp2_row -= change
            tmp2_col += change
            #print("diag2 coord", tmp2_row, tmp2_col)
            if tmp2_row >= 0 and tmp2_col >= 0 and tmp2_row < self.row and tmp2_col < self.col:
                cur_diag2.append(self.board[tmp2_row][tmp2_col])
            tmp2_row += change
            tmp2_col -= change

        print("diag1", cur_diag1)
        if goal in "".join(cur_diag1):
            print("winner is {} with diagonal 1".format(self.cur_move))
        print("diag2", cur_diag2)
        if goal in "".join(cur_diag2):
            print("winner is {} with diagonal 2".format(self.cur_move))


class Solution:
    def convert(self, start, end, ls):
        from collections import deque, defaultdict
        graph = defaultdict(defaultdict)
        # graph[a][b] means the 1 a -> graph[a][b] number of b
        for [id1, id2, ask, bid] in ls:
            if id2 not in graph[id1]:
                graph[id1][id2] = max(bid)
            else:
                graph[id1][id2] = max(graph[id1][id2], max(bid))
            if id1 not in graph[id2]:
                ask = list(filter(lambda x: x != 0, ask))
                if not ask:
                    raise Exception("Invalid, free money")
                graph[id2][id1] = 1.0 / min(ask)
        best_target = defaultdict(float)
        best_target[start] = 0
        self.best_path = []
        visited = set([start])

        def dfs(start_id, path, cur_money):
            if start_id == end:
                print(path, cur_money, "setting", best_target[start_id])
                self.best_path = path
                return
            for end_id in graph[start_id]:
                if end_id not in visited and (end_id not in best_target or graph[start_id][end_id] * cur_money > best_target[end_id]):
                    best_target[end_id] = graph[start_id][end_id] * cur_money
                    visited.add(end_id)
                    dfs(end_id, path + [end_id],
                        cur_money * graph[start_id][end_id])
                    visited.remove(end_id)
        dfs(start, [start], 1)
        return self.best_path

    def by_api(self):
        import requests
        info = requests.get("https://api.pro.coinbase.com/products").json()
        all_pairs = []
        count = 0
        for pair in info:
            count += 1
            connected_pair = pair["id"]
            pair_info = requests.get(
                "https://api.pro.coinbase.com/products/" + connected_pair + "/book").json()
            bids = list(map(lambda s: float(s), pair_info["bids"][0][:-1]))
            asks = list(map(lambda s: float(s), pair_info["asks"][0][:-1]))
            [c1, c2] = pair["id"].split("-")
            all_pairs.append([c1, c2, asks, bids])
            if count > 45:
                break
        print(self.convert('WCFG', 'EUR', all_pairs))
