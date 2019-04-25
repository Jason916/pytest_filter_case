from setuptools import setup

setup(
    name='pytest_filter_case',
    url='https://github.com/Jason916/pytest_filter_case',
    version='1.0.2',
    description='run test cases filter by mark',
    author='Jason916',
    author_email='Jason1989Xu@gmail.com',
    py_modules=['pytest_filter_case'],
    entry_points={
        'pytest11': [
            'pytest_filter_case = pytest_filter_case',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pytest',
        'Topic :: Software Development :: Testing',
    ],
    include_package_data=True,
)
