import pytest
import os
from degrees import shortest_path, load_data


@pytest.fixture
def load_small_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_data(f"{dir_path}/small")


def test_degrees_len(load_small_data):
    kevin_bacon = "102"
    tom_cruise = "129"
    tom_hanks = "158"
    emma_watson = "914612"

    a_few_good_men = "104257"
    apollo_13 = "112384"

    assert shortest_path(kevin_bacon, tom_cruise) == [a_few_good_men]
    assert shortest_path(tom_cruise, kevin_bacon) == [a_few_good_men]

    assert shortest_path(tom_hanks, kevin_bacon) == [apollo_13]
    assert shortest_path(kevin_bacon, tom_hanks) == [apollo_13]

    assert shortest_path(tom_hanks, tom_cruise) == [a_few_good_men, apollo_13]
    assert shortest_path(tom_cruise, tom_hanks) == [apollo_13, a_few_good_men]

    assert shortest_path(kevin_bacon, emma_watson) is None
    assert shortest_path(emma_watson, kevin_bacon) is None
