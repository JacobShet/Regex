import re

records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]

def extract_names(records):
    """Return a list of names from records"""
    names = []
    for record in records:
        name = re.findall(r'Name: (.*?) \|', record)
        if name:
            names.extend(name)
    return names

def extract_emails(records):
    """Return a list of emails from records"""
    emails = []
    for record in records:
        email = re.findall(r'Email: (.*?) \|', record)
        if email:
            emails.extend(email)
    return emails

def normalize_phones(records):
    """Strip all non-digits and reformat as XXX-XXX-XXXX"""
    phone_numbers = []
    for record in records:
        # Remove formatting characters before standardizing phone numbers.
        phone_number = re.findall(r'Phone: (.*?) \|', record)
        digits = re.sub(r"\D", "", phone_number[0])
        phone_numbers.append(f"{digits[:3]}-{digits[3:6]}-{digits[6:10]}")
    return phone_numbers

def extract_dates(records):
    """Return all dates regardless of format"""
    dates = []
    for record in records:
        date = re.findall(r'Joined: (.*)', record)
        if date:
            dates.extend(date)
    return dates

def parse_records(records):
    """Parse each record into its own dictionary"""
    parsed_records = []

    for record in records:
        parsed_dict = {}
        # Split each record into its own individual fields using the pipe delimiter.
        fields = record.split(" | ")
        for field in fields:
            parts = field.split(": ", 1)
            parsed_dict[parts[0].lower()] = parts[1]
        parsed_records.append(parsed_dict)

    return parsed_records

#clean = re.sub(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", normalize_phones, records)

print(extract_names(records)) 
print(extract_emails(records))
print(normalize_phones(records))
print(extract_dates(records))

print("\n")
print(parse_records(records))

