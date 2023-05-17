from faker import Faker

fake = Faker()

fake.locale = 'en_US'

for _ in range(5):
    name = fake.name()
    phone_number = fake.phone_number()
    seed_data = f"INSERT INTO drivers (name, phone_number) VALUES ('{name}', '{phone_number}');"
    print(seed_data)
