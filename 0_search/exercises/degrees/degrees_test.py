import pytest
import os
from degrees import shortest_path, load_data


@pytest.fixture
def load_small_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_data(f"{dir_path}/small")


def test_degrees(load_small_data):
    kevin_bacon = "102"
    tom_cruise = "129"
    tom_hanks = "158"
    emma_watson = "914612"

    a_few_good_men = "104257"
    apollo_13 = "112384"

    assert shortest_path(kevin_bacon, tom_cruise) == [(a_few_good_men, tom_cruise)]
    assert shortest_path(tom_cruise, kevin_bacon) == [(a_few_good_men, kevin_bacon)]

    assert shortest_path(tom_hanks, kevin_bacon) == [(apollo_13, kevin_bacon)]
    assert shortest_path(kevin_bacon, tom_hanks) == [(apollo_13, tom_hanks)]

    assert shortest_path(tom_hanks, tom_cruise) == [
        (apollo_13, kevin_bacon),
        (a_few_good_men, tom_cruise),
    ]
    assert shortest_path(tom_cruise, tom_hanks) == [
        (a_few_good_men, kevin_bacon),
        (apollo_13, tom_hanks),
    ]

    assert shortest_path(kevin_bacon, emma_watson) is None
    assert shortest_path(emma_watson, kevin_bacon) is None
