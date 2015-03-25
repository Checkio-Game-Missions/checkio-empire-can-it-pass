from checkio_referee import RefereeBase
from checkio_referee import representations

import settings
import settings_env
from tests import TESTS

cover = """
def cover(func, data):
    return func(tuple(tuple(row) for row in data[0]), tuple(data[1]), tuple(data[2]))
"""


def py_tuple_od_tuples(test, DEFAULT_FUNCTION_NAME):
    data = test["input"]
    return "{}({})".format(DEFAULT_FUNCTION_NAME,
                           tuple(tuple(row) for row in data[0]), tuple(data[1]), tuple(data[2]))


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "can_pass"
    CALLED_REPRESENTATIONS = {
        "python_3": py_tuple_od_tuples,
        "python_2": py_tuple_od_tuples,
        "javascript": representations.unwrap_arg_representation
    }
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
