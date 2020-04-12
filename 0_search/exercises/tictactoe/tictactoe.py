"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"  # noqa: E741
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if _is_empty(board):
        return X
    else:
        xs, os, _ = _coords(board)
        if len(xs) > len(os):
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    _, _, empty = _coords(board)
    return empty


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    assert i >= 0 and i <= 3, f"invalid row {i}"
    assert j >= 0 and j <= 3, f"invalid column {j}"
    assert action in actions(board), f"invalid action {action} for board {board}"

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for moves in _winner_moves():
        if all(board[i][j] is X for (i, j) in moves):
            return X
        elif all(board[i][j] is O for (i, j) in moves):
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    somebody_won = winner(board) is not None
    board_complete = not any(cell is EMPTY for cell in _flatten_board(board))
    return somebody_won or board_complete


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win is X:
        return 1
    elif win is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        actions_and_boards = [(action, result(board, action)) for action in actions(board)]
        if player(board) is X:
            scored_actions = [(_min_value(board), action) for action, board in actions_and_boards]
            best = max(scored_actions)
            _, action = best
            return action
        else:
            scored_actions = [(_max_value(board), action) for action, board in actions_and_boards]
            best = min(scored_actions)
            _, action = best
            return action


def _max_value(board):
    if terminal(board):
        return utility(board)
    else:
        next_moves = [result(board, action) for action in actions(board)]
        return max(_min_value(move) for move in next_moves)


def _min_value(board):
    if terminal(board):
        return utility(board)
    else:
        next_moves = [result(board, action) for action in actions(board)]
        return min(_max_value(move) for move in next_moves)


def _flatten_board(board):
    flat = []
    for row in board:
        for cell in row:
            flat.append(cell)

    return flat


def _is_empty(board):
    return all(cell is EMPTY for cell in _flatten_board(board))


def _coords(board):
    xs = set()
    os = set()
    empty = set()

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col is X:
                xs.add((i, j))
            elif col is O:
                os.add((i, j))
            else:
                empty.add((i, j))

    return xs, os, empty


def _winner_moves():
    winners = []

    # horizontal
    for i in range(3):
        m = [(i, j) for j in range(3)]
        winners.append(m)

    # vertical
    for j in range(3):
        m = [(i, j) for i in range(3)]
        winners.append(m)

    # diagonal
    winners.append([(0, 0), (1, 1), (2, 2)])
    winners.append([(2, 0), (1, 1), (0, 2)])

    return winners
