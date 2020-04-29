# -*- coding: utf-8 -*-
__author__ = 'jasonxu'


def pytest_addoption(parser):
    parser.addoption("--run-mark", default="all",
                     help="run test cases filter by mark, options: private/public/deployment/all/P0/P1/P2/P3")


def pytest_configure(config):
    config.addinivalue_line("markers", "private: mark private testcase")
    config.addinivalue_line("markers", "public: mark public testcase")
    config.addinivalue_line("markers", "deployment: mark deployment testcase")
    config.addinivalue_line("markers", "all: mark all testcase")
    config.addinivalue_line("markers", "P0: mark P0 testcase")
    config.addinivalue_line("markers", "P1: mark P1 testcase")
    config.addinivalue_line("markers", "P2: mark P2 testcase")
    config.addinivalue_line("markers", "P3: mark P3 testcase")


def pytest_collection_modifyitems(config, items):
    run_mark = "all"
    if config.getoption("--run-mark"):
        run_mark = config.getoption("--run-mark")

    run_mark_list = run_mark.split(" ")
    for run_mark_item in run_mark_list:
        if run_mark_item not in ("private", "public", "deployment", "all", "P0", "P1", "P2", "P3"):
            raise RuntimeError("non support {} mode".format(run_mark_item))

    run_test_cases, skip_test_cases = [], []
    if "all" in run_mark:
        return
    for item in items:
        if len(run_mark_list) == 1:
            condition = item.get_closest_marker(run_mark_list[0])
        elif len(run_mark_list) == 2:
            condition = item.get_closest_marker(run_mark_list[0]) and item.get_closest_marker(run_mark_list[1])
        else:
            raise RuntimeError("number of run mark is exceed")
        case_list = run_test_cases if condition else skip_test_cases
        case_list.append(item)

    if run_test_cases:
        items[:] = run_test_cases
        if skip_test_cases:
            config.hook.pytest_deselected(items=skip_test_cases)
    else:
        raise RuntimeError("no testcase is marked by '{}'".format(run_mark))
