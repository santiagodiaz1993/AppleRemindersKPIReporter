from google_reporting_api import GoogleDocsSession, GoogleEmailSession

if __name__ == "__main__":
    email = GoogleEmailSession(
        sender="santiagobmxdiaz@gmail.com",
        to="santiagobmx@hotmail.com",
        subject="hello",
        message_text="hello",
        file_dir="./task_logging/2020-05-23/",
        filename="logging.txt",
    )
    email = GoogleEmailSession.create_message_with_attachment(
        sender="santiagobmxdiaz@gmail.com",
        to="santiagobmx@hotmail.com",
        subject="hello",
        message_text="hello",
        file_dir="./task_logginkjsdf;aljsf;lajsdf;lkjasdf;ljasd;fljasd;lfjads;klfjsad;lkjfa;lsdkjf;alskdjfg/2020-05-23/",
        filename="logging.txt",djfklajsd
