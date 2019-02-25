import pytest
import allure
import tesults
import sys
import os
from _pytest.runner import runtestprotocol


# The data variable holds test results and tesults target information, at the end of test run it is uploaded to tesults for reporting.
data = {
    'target': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
              '.eyJpZCI6ImFhOWYyOTVlLTI0NjEtNGU3Ny1iODlhLTkzYjAxNmJhYjU1MS0xNTMxMTE1OTk0NjE1IiwiZXhwIjo0MTAyNDQ0ODAwMDAwLCJ2ZXIiOiIwIiwic2VzIjoiODNhZTc4MzgtZmFhMy00M2EyLTliNzgtOGViZjNiNzA4YmRkIiwidHlwZSI6InQifQ.lBKWmQrjAYyROIgxjq8J4aW9eDIbiQ3aj0BlwHTsUVs',
    'results': {'cases': []}
}


# Converts pytest test outcome to a tesults friendly result (for example pytest uses 'passed', tesults uses 'pass')
def tesultsFriendlyResult(outcome):
    if (outcome == 'passed'):
        return 'pass'
    elif (outcome == 'failed'):
        return 'fail'
    else:
        return 'unknown'


# Extracts test failure reason
def reasonForFailure(report):
    if report.outcome == 'passed':
        return ''
    else:
        return report.longreprtext


def paramsForTest(item):
    paramKeys = item.get_marker('parametrize')
    if (paramKeys):
        paramKeys = paramKeys.args[0]
        params = {}
        values = item.name.split('[')
        if len(values) > 1:
            values = values[1]
            values = values[:-1]  # removes ']'
            values = values.split("-")  # values now separated
        else:
            return None
        for key in paramKeys:
            if (len(values) > 0):
                params[key] = values.pop(0)
        return params
    else:
        return None


def filesForTest(item):
    files = []
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "path-to-test-generated-files", item.name)
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                files.append(os.path.join(path, file))
    return files


# A pytest hook, called by pytest automatically - used to extract test case data and append it to the data global variable defined above.
def pytest_runtest_protocol(item, nextitem):
    global data
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            testcase = {
                'name': item.name,
                'result': tesultsFriendlyResult(report.outcome),
                'suite': str(item.parent),
                'desc': item.name,
                'reason': reasonForFailure(report)
            }
            files = filesForTest(item)
            if len(files) > 0:
                testcase['files'] = files
            params = paramsForTest(item)
            if (params):
                testcase['params'] = params
                testname = item.name.split('[')
                if len(testname) > 1:
                    testcase['name'] = testname[0]
            paramDesc = item.get_marker('description')
            if (paramDesc):
                testcase['desc'] = paramDesc.args[0]
            data['results']['cases'].append(testcase)
    return True


# A pytest hook, called by pytest automatically - used to upload test results to tesults.
def pytest_unconfigure(config):
    global data
    print('-----Tesults output-----')
    if len(data['results']['cases']) > 0:
        print('data: ' + str(data))
        ret = tesults.results(data)
        print('success: ' + str(ret['success']))
        print('message: ' + str(ret['message']))
        print('warnings: ' + str(ret['warnings']))
        print('errors: ' + str(ret['errors']))
    else:
        print('No test results.')


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--env", default="remote")
    parser.addoption("--url")


def pytest_report_header(config):
    if config.getoption("verbose") > 0:
        return ["info1: Running test scripts ...", "Run by Felix"]


#def pytest_runtest_logreport(report):#
    """ process a test setup/call/teardown report relating to
    the respective phase of executing a test. """


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    allure.environment(
        report='Castlighthealth',
        url='https://us.castlighthealth.com',
        browser=u'Google Chrome',
        environment="remote",
    )


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" % previousfailed.name)


regression = pytest.mark.Name
functional = pytest.mark.Name
description = pytest.mark.Description
# order = pytest.mark.Name

# pytest_plugins = 'allure.pytest_plugin'

