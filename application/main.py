from google_reporting_api import GoogleDocsSession, GoogleEmailSession


def main():
    testDoc = GoogleDocsSession("19GFEhbZ0KlWknhEw6Js0mCEeIwNQgVeif-3Bw_yFpVs")
    print(testDoc.get_reminders_from_document())

    testEmail = GoogleEmailSession(
        sender="santiagobmxdiaz@gmail.com",
        to="santiagobmxdiaz@gmail.com",
        subject="Weekly Report",
        message_text="Hello",
    )

    # with open("configuration.json") as config:
    #     user_configuration = json.load(config)
    #
    # report1 = get_reminders_as_text(
    #     user_configuration["completed_tasks_document_id"]
    # )
    #
    # completed_tasks_report = ReportGenerator(report1, 8)
    # print(completed_tasks_report.get_reminders_from_document(report1))
    # print(completed_tasks_report.get_tasks_with_priority_set())


#    tasks_completed_formatted = ReportGenerator.get_reminders_from_document(
#        get_reminders_as_text(
#            user_configuration["completed_tasks_document_id"]
#        )
#    )
#    tasks_initiated_formatted = ReportGenerator.get_reminders_from_document(
#        get_reminders_as_text(
#            user_configuration["initiated_tasks_document_id"]
#        )
#    )
#
#    result = (
#        initiate_doc_api(user_configuration["completed_tasks_document_id"])
#        .documents()
#        .get(documentId=user_configuration["completed_tasks_document_id"])
#        .execute()
#    )
#    print(json.dumps(result, indent=4, sort_keys=True))
#
#    TaskLogging.log_tasks("test", tasks_completed_formatted)
#    ReportGraphing.build_bar_chart(tasks_completed_formatted, 8)
#    ReportGraphing.build_pie_chart(tasks_completed_formatted)
#
#    current_date = str(dt.today().date())
#    request_message = EmailInteraction()
#    request_message.authorize()
#
#    request_message = EmailInteraction.create_message_with_attachment(
#        user_configuration["sender_email"],
#        user_configuration["send_to_email"],
#        user_configuration["email_subject"],
#        TaskLogging.load_template(
#            "template1", tasks_completed_formatted, tasks_initiated_formatted
#        ),
#        "task_logging/" + current_date + "/",
#        [
#            "productivity_distribution_" + current_date + ".png",
#            "productivity_progress_" + current_date + ".png",
#        ],
#    )
#
#    EmailInteraction.send_message(
#        EmailInteraction.authorize(),
#        user_configuration["sender_email"],
#        request_message,
#    )
#

if __name__ == "__main__":
    main()
