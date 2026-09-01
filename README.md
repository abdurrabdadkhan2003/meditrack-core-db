# Meditrack Core Database (`meditrack-core-db`)

Core relational database module for clinic operations, tracking patient demographics and appointment history using synthetic, compliance-safe data.

## Schema Overview
- **`patients`**: Core patient demographic information.
- **`visits`**: Clinical visits linked via foreign key to patient records.

## Data Generation
Synthetic seed data generated via Faker (`seed/generate_mock_patients.py`):
- 200 Synthetic Patients
- 500 Linked Visit Records

## ERD Diagram
See `docs/erd.md` for the ASCII entity-relationship model.
