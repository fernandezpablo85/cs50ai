from logic import Symbol, And, Or, Implication, Biconditional, Not, model_check

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

OnlyOneKindForEach = And(Or(AKnave, AKnight), Or(BKnight, BKnave), Or(CKnave, CKnight))

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(OnlyOneKindForEach, Implication(AKnight, And(AKnight, AKnave)))

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

WereBothKnaves = And(BKnave, AKnave)
knowledge1 = And(
    OnlyOneKindForEach,
    Implication(AKnight, WereBothKnaves),
    Implication(AKnave, Not(WereBothKnaves)),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
WereTheSameKind = Or(And(BKnave, AKnave), And(BKnight, AKnight))
WereDifferentKinds = Or(And(BKnave, AKnight), And(BKnight, AKnave))

knowledge2 = And(
    OnlyOneKindForEach,
    Implication(AKnight, WereTheSameKind),
    Implication(AKnave, Not(WereTheSameKind)),
    Implication(BKnight, WereDifferentKinds),
    Implication(BKnave, Not(WereDifferentKinds)),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

# fmt: off
ASaysKnave = Or(
    And(AKnight, AKnave),
    And(AKnave, Not(AKnave))
)
ASaysKnight = Or(
    And(AKnight, AKnight),
    And(AKnave, Not(AKnight))
)

ASaysSomething = Or(ASaysKnight, ASaysKnave)

Truths = And(CKnave, ASaysKnave)
Lies = And(CKnight, ASaysKnight)
BSays = And(
    Biconditional(BKnight, Truths),
    Biconditional(BKnave, Lies)
)

CSays = And(
    Biconditional(CKnight, AKnight),
    Biconditional(CKnave, AKnave)
)

knowledge3 = And(OnlyOneKindForEach, ASaysSomething, BSays, CSays)
# fmt: on


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
