from datetime import datetime as dt
from apple_reminder_reporter.reminders_kpi_reporter import *
from google_docs_api.google_docs import *
from google_email_api.gmail_api import *
from google_docs_api.google_docs import *
from google_email_api.gmail_api import *


# TODO(santiago): Remove unnecessary scopes
SCOPES = [
    "https://www.googleapis.com/auth/drive.activity.readonly",
    "https://www.googleapis.com/auth/documents",
    "https://mail.google.com/",
]

reminders_completed = get_text("19GFEhbZ0KlWknhEw6Js0mCEeIwNQgVeif-3Bw_yFpVs")
reminders_started = get_text("1HuonqcF3SwcfwTebKL2hCNW3LjZ87jrC4byV_Zh7PQ0")

tasks_organized = ReportGenerator.get_reminders_from_document(
    reminders_completed
)
TaskLogging.log_tasks("test", tasks_organized)
ReportGraphing.build_bar_chart(tasks_organized, 3)
ReportGraphing.build_pie_chart(tasks_organized)
ReportGenerator.get_tasks_with_priority_set(tasks_organized)
ReportGenerator.get_number_of_reminders(tasks_organized)
ReportGenerator.get_tasks_name(tasks_organized)
ReportGenerator.get_tasks_in_time_range(tasks_organized, 22)
ReportGenerator.create_date_ranges(3)
ReportGenerator.classify_tasks_in_date_range(tasks_organized, 4)
TaskLogging.log_tasks("logging", tasks_organized)
ReportGenerator.categorize_tasks(tasks_organized)

current_date = str(dt.today().date())
request_message = EmailInteraction.CreateMessageWithAttachment(
    "santiagobmxdiaz@gmail.com",
    "santiagobmxdiaz@gmail.com",
    "weekly Productivity Report",
    TaskLogging.load_template("template1", tasks_organized, tasks_organized),
    "task_logging/" + current_date + "/",
    [
        "productivity_distribution_" + current_date + ".png",
        "productivity_progress_" + current_date + ".png",
    ],
)

EmailInteraction.SendMessage(
    EmailInteraction.authorization(),
    "santiagobmxdiaz@gmail.com",
    request_message,
)
