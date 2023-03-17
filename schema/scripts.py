from faker import Faker


def column_type_fake_relation(column):
    fake = Faker()

    if column.type == "Company":
        return fake.company()

    elif column.type == "Full name":
        return fake.name()

    elif column.type == "Email":
        return fake.company_email()

    elif column.type == "Date":
        return fake.date()

    elif column.type == "Job":
        return fake.job()
