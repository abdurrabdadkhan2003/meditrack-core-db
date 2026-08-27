import random
from faker import Faker

fake = Faker()

def generate_patients(num_records=200):
    print(f"-- Generating {num_records} synthetic patients...")
    with open("seed/mock_patients.sql", "w") as file:
        file.write("INSERT INTO patients (first_name, last_name, date_of_birth, contact_number) VALUES\n")

        for i in range(num_records):
            first_name = fake.first_name().replace("'", "")
            last_name = fake.last_name().replace("'", "")
            dob = fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
            phone = fake.basic_phone_number()

            line = f"('{first_name}', '{last_name}', '{dob}', '{phone}')"
            if i < num_records - 1:
                line += ",\n"
            else:
                line += ";\n"
            file.write(line)

    print("Success! Data saved to seed/mock_patients.sql")

if __name__ == "__main__":
    generate_patients(200)
