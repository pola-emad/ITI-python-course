import csv
email_file = open('E-mails.csv', 'r')
email_reader = csv.reader(email_file)
data = list(email_reader)
row_count = len(data)
emails = []
for row in range(1, row_count):
    emails.append(data[row][3])
email_file.close()

from authorization import filter_emails
from text_functions import count_domains

valid_emails = list(filter_emails(emails))
no_of_domains=set(count_domains(emails))
print(f"Number of total emails: {row_count-1} \t Number of valid emails: {len(valid_emails)}")
print(f"Number of unique domains: {len(no_of_domains)}")


