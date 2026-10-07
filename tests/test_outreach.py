from digisetu.enrichment.approval import HumanApproval
from digisetu.enrichment.email import EmailSender


message = """Dear ABC Dental Clinic Team,

We noticed that your website currently does not appear to have
online booking and payment features.

Would you be open to a quick conversation about these digital gaps?
"""

approval = HumanApproval()
email_sender = EmailSender()

approved = approval.approve(message)

if approved:
    email_sender.send(
        recipient="clinic@example.com",
        subject="Digital opportunities for ABC Dental Clinic",
        message=message,
    )
else:
    print("\nMessage rejected. Email was not sent.")