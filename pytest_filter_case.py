# -*- coding: utf-8 -*-
__author__ = 'jasonxu'


def pytest_addoption(parser):
    parser.addoption("--run-mark", default="all", help="run test cases filter by mark, options: private/public/all")


def pytest_collection_modifyitems(config, items):
    global run_mark
    if config.getoption("--run-mark"):
        run_mark = config.getoption("--run-mark")

    if run_mark not in ("private", "public", "all"):
        raise Exception("non support {} mode".format(run_mark))

    run_test_cases, skip_test_cases = [], []
    if run_mark == "all":
        return
    for item in items:
        case_list = run_test_cases if item.get_marker(run_mark) else skip_test_cases
        case_list.append(item)

    if run_test_cases:
        items[:] = run_test_cases
        if skip_test_cases:
            config.hook.pytest_deselected(items=skip_test_cases)
