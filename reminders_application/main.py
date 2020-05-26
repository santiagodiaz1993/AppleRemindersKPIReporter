from datetime import datetime as dt
import json

from apple_reminder_reporter.reminders_kpi_reporter import *
from google_docs_api.google_docs import *
from google_email_api.gmail_api import *

with open("configuration.json") as config:
    user_configuration = json.load(config)


SCOPES = user_configuration["SCOPES"]

reminders_completed = get_text(
    user_configuration["completed_tasks_document_id"]
)
reminders_initiated = get_text(
    user_configuration["initiated_tasks_document_id"]
)

tasks_completed_formatted = ReportGenerator.get_reminders_from_document(
    reminders_completed
)
tasks_initiated_formatted = ReportGenerator.get_reminders_from_document(
    reminders_initiated
)

TaskLogging.log_tasks("test", tasks_completed_formatted)
TaskLogging.log_tasks("test", tasks_completed_formatted)
ReportGraphing.build_bar_chart(tasks_completed_formatted, 3)
ReportGraphing.build_pie_chart(tasks_completed_formatted)
#ReportGenerator.get_tasks_with_priority_set(tasks_completed_formatted)
#ReportGenerator.get_number_of_reminders(tasks_completed_formatted)
#ReportGenerator.get_tasks_name(tasks_completed_formatted)
#ReportGenerator.get_tasks_in_time_range(tasks_completed_formatted, 22)
#ReportGenerator.create_date_ranges(3)
#ReportGenerator.classify_tasks_in_date_range(tasks_completed_formatted, 4)
#TaskLogging.log_tasks("logging", tasks_completed_formatted)
#ReportGenerator.categorize_tasks(tasks_completed_formatted)


current_date = str(dt.today().date())
request_message = EmailInteraction.CreateMessageWithAttachment(
    user_configuration["sender_email"],
    user_configuration["send_to_email"],
    user_configuration["email_subject"],
    TaskLogging.load_template("template1", tasks_completed_formatted, tasks_initiated_formatted),
    "task_logging/" + current_date + "/",
    [
        "productivity_distribution_" + current_date + ".png",
        "productivity_progress_" + current_date + ".png",
    ],
)

EmailInteraction.SendMessage(
    EmailInteraction.authorization(),
    user_configuration["sender_email"],
    request_message,
)
