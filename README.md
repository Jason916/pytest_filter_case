## pytest_filter_case
[pytest plugin]  run test cases filter by mark

run test cases filter by mark of env and mark of testcase level

    run testcases filter by mark of env, options: private/public/canary/deployment/all, example: [single] --run-env public
    run testcases filter by mark of testcase level, options: P0/P1/P2/P3, example: [single] --run-testcase-level P0,[multi] --run-testcase-level P0 P1 P2

## Install
pip install pytest-filter-case

## Usage
for example:
  single option
    pytest --run-env=public --run-testcase-level=P0

  multi options
    pytest --run-env=public --run-testcase-level="P0 P1 P2"