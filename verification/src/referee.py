from checkio_referee import RefereeBase
from checkio_referee import representations, covercodes, ENV_NAME


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
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "canPass"
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: py_tuple_od_tuples,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: cover,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }
