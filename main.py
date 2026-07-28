
# from funcFile import generate_patient_data

from funcFile import generate_patient_data, validate_patient_information, generate_patient_report, display_patient_report

patients = generate_patient_data(int(input("Enter the number of patients to generate: ")))
# print(validate_patient_information(patients[0]))
for patient in patients:
    is_valid, errors = validate_patient_information(patient)
    if not is_valid:
        print(f"Patient {patient} has the following validation errors: {errors}")

# print(generate_patient_report(patients))
display_patient_report(generate_patient_report(patients))

# Example usage:
# patients = generate_patient_data(int(input("Enter the number of patients to generate: ")))
# print(patients) 
