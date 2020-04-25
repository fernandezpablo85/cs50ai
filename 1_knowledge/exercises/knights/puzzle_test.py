from functools import partial
import puzzle
from puzzle import AKnight, AKnave, BKnight, BKnave, CKnight, CKnave


def entails_knowledge(knowledge_base, proposition):
    return puzzle.model_check(knowledge_base, proposition)


def test_puzzle_0():
    entails = partial(entails_knowledge, puzzle.knowledge0)
    assert entails(AKnave)
    assert not entails(AKnight)


def test_puzzle_1():
    entails = partial(entails_knowledge, puzzle.knowledge1)
    assert entails(AKnave)
    assert not entails(AKnight)

    assert entails(BKnight)
    assert not entails(BKnave)


def test_puzzle_2():
    entails = partial(entails_knowledge, puzzle.knowledge2)
    assert entails(AKnave)
    assert not entails(AKnight)

    assert entails(BKnight)
    assert not entails(BKnave)


def test_puzzle_3():
    entails = partial(entails_knowledge, puzzle.knowledge3)
    assert entails(AKnight)
    assert not entails(AKnave)

    assert entails(BKnave)
    assert not entails(BKnight)

    assert entails(CKnight)
    assert not entails(CKnave)
