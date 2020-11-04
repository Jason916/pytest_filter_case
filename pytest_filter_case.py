# -*- coding: utf-8 -*-
__author__ = 'jasonxu'


def pytest_addoption(parser):
    parser.addoption("--run-env", default="public",
                     help="run testcases filter by mark of env, options: private/public/canary/deployment/all, example: [single] --run-env public")
    parser.addoption("--run-testcase-level", default="P0",
                     help="run testcases filter by mark of testcase level, options: P0/P1/P2/P3, example: [single] --run-testcase-level P0,[multi] --run-testcase-level P0 P1 P2")


def pytest_configure(config):
    config.addinivalue_line("markers", "private: mark private testcases")
    config.addinivalue_line("markers", "public: mark public testcases")
    config.addinivalue_line("markers", "canary: mark canary testcases")
    config.addinivalue_line("markers", "deployment: mark deployment testcases")
    config.addinivalue_line("markers", "all: mark all testcases")
    config.addinivalue_line("markers", "P0: mark P0 testcases")
    config.addinivalue_line("markers", "P1: mark P1 testcases")
    config.addinivalue_line("markers", "P2: mark P2 testcases")
    config.addinivalue_line("markers", "P3: mark P3 testcases")


def pytest_collection_modifyitems(config, items):
    run_env = "public"
    run_testcase_level = "P0"
    if config.getoption("--run-env"):
        run_env = config.getoption("--run-env")
    if config.getoption("--run-testcase-level"):
        run_testcase_level = config.getoption("--run-testcase-level")

    run_testcase_level_list = run_testcase_level.split(" ")
    for run_testcase_level_item in run_testcase_level_list:
        if run_testcase_level_item not in ("P0", "P1", "P2", "P3"):
            raise RuntimeError("non support testcase level: {}".format(run_testcase_level_item))

    if run_env not in ("private", "public", "deployment", "all", "canary"):
        raise RuntimeError("non support env level: {}".format(run_env))

    run_test_cases, skip_test_cases = [], []
    if "all" == run_env:
        return

    for item in items:
        run_testcase_level_arr = [item.get_closest_marker(x) for x in run_testcase_level_list]
        condition = item.get_closest_marker(run_env) and (
            reduce(lambda (condition1, condition2): condition1 or condition2, run_testcase_level_arr))
        if condition:
            run_test_cases.append(item)
        else:
            skip_test_cases.append(item)

    if run_test_cases:
        items[:] = run_test_cases
        if skip_test_cases:
            config.hook.pytest_deselected(items=skip_test_cases)
    else:
        raise RuntimeError("no testcase is marked by '{}'".format(run_env))
