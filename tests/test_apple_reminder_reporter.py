# coding=utf-8

import test
from reminders_application.google_email_api import google_docs

# from google_docs_api.google_docs import *
# from google_email_api.gmail_api import *
# from apple_reminder_reporter.reminders_kpi_reporter import *

from main import *


def test_extract_reminders_document():
    document = (
        "Testing List$$ Ffoutfdrdr7isyidd$$ May "
        "09, 2020 at 11:41PM$$ None$$ //-//"
    )
    result = extract_reminders_document(document)
    testing_list = [
        [
            "Testing List",
            " Ffoutfdrdr7isyidd",
            " May 09, 2020 at 11:41PM",
            " None",
        ]
    ]
    assert result == testing_list


def test_log_tasks():
    tasks_for_logging_test = [
        ["Testing List", " Ffoutfd", " May 09, 2020 at 11:41PM", " None"],
        ["Testing List", " Jgkccccccui", " May 09, 2020 at 11:41PM", " None"],
        [
            "Testing List",
            " Hgkcgjcutcu",
            " May 09, 2020 at 11:41PM",
            " Medium",
        ],
    ]
    log = log_tasks("unit_test", tasks_for_logging_test)
    expected = " Ffoutfd,  Jgkccccccui,  Hgkcgjcutcu, "
    assert log == expected


def test_check_for_high_priority():
    reminder = [
        ["Testing List", " Hgkcgjcut", " May 09, 2020 at 11:41PM", " Medium"],
        ["Testing List", " Ffoutf", " May 09, 2020 at 11:41PM", " None"],
    ]
    from_function = check_for_high_priority(reminder)
    expected = [" Hgkcgjcut"]
    assert expected == from_function


def test_categorize_tasks():
    tasks_for_logging_test = [
        ["Testing List", " Ffoutfd", " May 09, 2020 at 11:41PM", " None"],
        ["Testing List", " Jgkccccccui", " May 09, 2020 at 11:41PM", " None"],
        [
            "Testing List",
            " Hgkcgjcutcu",
            " May 09, 2020 at 11:41PM",
            " Medium",
        ],
    ]
    categorized_tasks = categorize_tasks(tasks_for_logging_test)
    expected_categorization = {
        "Work": 0,
        "Personal Errands": 0,
        "Machine Learning Project": 0,
        "Artificial Inteligence Podcast": 0,
        "Movies to do": 0,
        "VIM Learning": 0,
        "Testing List": 3,
    }
    assert categorized_tasks == expected_categorization


def test_load_template():
    load_template()


# def test_classify_by_date_range():
#    tasks = [
#            ['Testing List', ' Ffoutfdrdr7isyidd', ' May 09, 2020 at 11:41PM', ' None'],
#            ['Testing List', ' Jgkccccccuifccccoutcutocccfc', ' May 09, 2020 at 11:41PM', ' None'],
#            ['Testing List', ' Hgkcgjcutcutcocutoctuoc', ' May 04, 2020 at 11:41PM', ' Medium'],
#            ['Testing List', ' Ffoutfdrdr7isyidd', ' May 11, 2020 at 11:41PM', ' None'],
#            ['Testing List', ' Hgkcgjcutcutcocutoctuoc', ' May 10, 2020 at 11:41PM', ' Medium'],
#            ['Testing List', ' Jgkccccccuifccccoutcutocccfc', ' May 14, 2020 at 11:41PM', ' None']
#        ]
#    from_function = classify_by_date_range(tasks, 4)
#    expected_outcome = {'2020-05-03 to 2020-05-07': 1,
#                        '2020-05-07 to 2020-05-11': 3,
#                        '2020-05-11 to 2020-05-15': 2,
#                        '2020-05-15 to 2020-05-19': 0}
#
#    assert from_function == expected_outcome
