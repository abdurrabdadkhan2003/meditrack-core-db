import random
from faker import Faker

fake = Faker()

REASONS = [
    "Routine Checkup",
    "Dental Consultation",
    "Follow-up",
    "General Malaise",
    "Prescription Refill",
    "Blood Test Review",
    "Orthopedic Evaluation"
]

def generate_patients(num_records=200):
    print(f"-- Generating {num_records} synthetic patients...")
    with open("seed/mock_patients.sql", "w") as file:
        file.write("INSERT INTO patients (patient_id, first_name, last_name, date_of_birth, contact_number) VALUES\n")

        for i in range(1, num_records + 1):
            first_name = fake.first_name().replace("'", "")
            last_name = fake.last_name().replace("'", "")
            dob = fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
            phone = fake.basic_phone_number()

            line = f"({i}, '{first_name}', '{last_name}', '{dob}', '{phone}')"
            if i < num_records:
                line += ",\n"
            else:
                line += ";\n"
            file.write(line)

def generate_visits(num_records=500, patient_count=200):
    print(f"-- Generating {num_records} synthetic visits...")
    with open("seed/mock_visits.sql", "w") as file:
        file.write("INSERT INTO visits (patient_id, visit_date, reason_for_visit, notes) VALUES\n")

        for i in range(num_records):
            patient_id = random.randint(1, patient_count)
            visit_date = fake.date_time_between(start_date="-1y", end_date="now").strftime("%Y-%m-%d %H:%M:%S")
            reason = random.choice(REASONS)
            notes = fake.sentence(nb_words=8).replace("'", "")

            line = f"({patient_id}, '{visit_date}', '{reason}', '{notes}')"
            if i < num_records - 1:
                line += ",\n"
            else:
                line += ";\n"
            file.write(line)

if __name__ == "__main__":
    generate_patients(200)
    generate_visits(500, 200)
    print("Verification complete: generated 200 patients and 500 visits.")
