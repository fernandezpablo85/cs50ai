import tictactoe as ttt
from hypothesis import given
from hypothesis.strategies import integers, tuples, one_of, just


coordinate = tuples(integers(min_value=0, max_value=2), integers(min_value=0, max_value=2))
any_marker = one_of(just(ttt.X), just(ttt.O))


def test_flatten_board():
    init = ttt.initial_state()
    flat = ttt._flatten_board(init)
    assert isinstance(flat, list)
    assert len(flat) == 9


def test_board_is_empty():
    init = ttt.initial_state()
    assert ttt._is_empty(init)


@given(coordinate, any_marker)
def test_board_is_not_empty(coord, marker):
    init = ttt.initial_state()
    x, y = coord
    init[x][y] = marker
    assert not ttt._is_empty(init)


def test_x_moves_first():
    init = ttt.initial_state()
    assert ttt.player(init) == ttt.X


@given(coordinate)
def test_x_moves_after_any_o(coord):
    init = ttt.initial_state()
    x, y = coord
    init[x][y] = ttt.O
    assert ttt.player(init) == ttt.X


@given(coordinate)
def test_o_moves_after_any_x(coord):
    init = ttt.initial_state()
    x, y = coord
    init[x][y] = ttt.X
    assert ttt.player(init) == ttt.O


def test_all_available_actions():
    init = ttt.initial_state()
    actions = ttt.actions(init)
    assert len(actions) == 9


@given(coordinate, any_marker)
def test_available_actions_after_move(coord, marker):
    init = ttt.initial_state()
    x, y = coord
    init[x][y] = marker
    actions = ttt.actions(init)
    assert len(actions) == 8
    assert (x, y) not in actions


@given(coordinate)
def test_board_move(coord):
    init = ttt.initial_state()
    new_state = ttt.result(init, coord)

    xs, os, empty = ttt._coords(new_state)
    assert len(xs) == 1
    assert len(os) == 0
    assert len(empty) == 8

    assert ttt._is_empty(init), "initial board unmodified"


@given(any_marker, integers(min_value=0, max_value=7))
def test_winner(marker, winner_move_idx):
    init = ttt.initial_state()
    assert ttt.winner(init) is None
    assert not ttt.terminal(init)

    # perform the winning move
    for i, j in ttt._winner_moves()[winner_move_idx]:
        init[i][j] = marker

    # and win!
    assert ttt.winner(init) is marker
    assert ttt.terminal(init)
