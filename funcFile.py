import random


def generate_patient_data(num_patients):
    """Generate random patient data for the given number of patients."""
    patients = []
    genders = ["Male", "Female"]

    for i in range(1, num_patients + 1):
        patient = {
            "ptID": f"P{i:03d}",
            "age": random.randint(18, 90),
            "weight": random.randint(45, 150),
            "height": random.randint(145, 210),
            "gender": random.choice(genders),
            "systolic_bp": random.randint(90, 180),
            "diastolic_bp": random.randint(50, 120),
        }
        patients.append(patient)

    return patients


def validate_patient_information(patient):
    """Validate a patient dictionary and return a tuple of (is_valid, errors)."""
    required_fields = {
        "ptID": str,
        "age": int,
        "weight": int,
        "height": int,
        "gender": str,
        "systolic_bp": int,
        "diastolic_bp": int,
    }
    errors = []

    if not isinstance(patient, dict):
        return False, ["Patient information must be provided as a dictionary."]

    for field, expected_type in required_fields.items():
        if field not in patient:
            errors.append(f"Missing required field: {field}")
            continue

        value = patient[field]
        if not isinstance(value, expected_type):
            errors.append(f"Field '{field}' must be of type {expected_type.__name__}.")
            continue

        if field == "age" and not 0 <= value <= 120:
            errors.append("Age must be between 0 and 120.")
        elif field == "weight" and not 1 <= value <= 500:
            errors.append("Weight must be between 1 and 500.")
        elif field == "height" and not 50 <= value <= 250:
            errors.append("Height must be between 50 and 250.")
        elif field == "gender" and value not in ["Male", "Female"]:
            errors.append("Gender must be either 'Male' or 'Female'.")
        elif field == "systolic_bp" and not 40 <= value <= 300:
            errors.append("Systolic BP must be between 40 and 300.")
        elif field == "diastolic_bp" and not 20 <= value <= 200:
            errors.append("Diastolic BP must be between 20 and 200.")

    if ("systolic_bp" in patient and "diastolic_bp" in patient
            and isinstance(patient["systolic_bp"], int)
            and isinstance(patient["diastolic_bp"], int)
            and patient["diastolic_bp"] > patient["systolic_bp"]):
        errors.append("Diastolic BP cannot be greater than systolic BP.")

    return len(errors) == 0, errors


def generate_patient_report(patients):
    """Generate a summary report for a list of patient details."""
    if not isinstance(patients, list):
        raise TypeError("Patients must be provided as a list of dictionaries.")

    if not patients:
        return {
            "total_patients": 0,
            "average_age": 0,
            "average_weight": 0,
            "average_height": 0,
            "average_systolic_bp": 0,
            "average_diastolic_bp": 0,
            "gender_breakdown": {},
            "invalid_patients": [],
        }

    valid_patients = []
    invalid_patients = []

    for patient in patients:
        is_valid, errors = validate_patient_information(patient)
        if is_valid:
            valid_patients.append(patient)
        else:
            invalid_patients.append({"patient": patient, "errors": errors})

    if not valid_patients:
        return {
            "total_patients": len(patients),
            "average_age": 0,
            "average_weight": 0,
            "average_height": 0,
            "average_systolic_bp": 0,
            "average_diastolic_bp": 0,
            "gender_breakdown": {},
            "invalid_patients": invalid_patients,
        }

    ages = [patient["age"] for patient in valid_patients]
    weights = [patient["weight"] for patient in valid_patients]
    heights = [patient["height"] for patient in valid_patients]
    systolic_values = [patient["systolic_bp"] for patient in valid_patients]
    diastolic_values = [patient["diastolic_bp"] for patient in valid_patients]
    gender_counts = {}

    for patient in valid_patients:
        gender_counts[patient["gender"]] = gender_counts.get(patient["gender"], 0) + 1

    report = {
        "total_patients": len(patients),
        "average_age": round(sum(ages) / len(ages), 2),
        "average_weight": round(sum(weights) / len(weights), 2),
        "average_height": round(sum(heights) / len(heights), 2),
        "average_systolic_bp": round(sum(systolic_values) / len(systolic_values), 2),
        "average_diastolic_bp": round(sum(diastolic_values) / len(diastolic_values), 2),
        "gender_breakdown": gender_counts,
        "invalid_patients": invalid_patients,
    }

    return report


def display_patient_report(report):
    """Return a neatly formatted patient report string for display."""
    if not isinstance(report, dict):
        raise TypeError("Report must be provided as a dictionary.")

    lines = []
    lines.append("=" * 70)
    lines.append("PATIENT REPORT")
    lines.append("=" * 70)
    lines.append(f"Total Patients: {report.get('total_patients', 0)}")
    lines.append(f"Average Age: {report.get('average_age', 0)}")
    lines.append(f"Average Weight: {report.get('average_weight', 0)}")
    lines.append(f"Average Height: {report.get('average_height', 0)}")
    lines.append(f"Average Systolic BP: {report.get('average_systolic_bp', 0)}")
    lines.append(f"Average Diastolic BP: {report.get('average_diastolic_bp', 0)}")
    lines.append("Gender Breakdown:")

    gender_breakdown = report.get("gender_breakdown", {})
    if gender_breakdown:
        for gender, count in gender_breakdown.items():
            lines.append(f"  - {gender}: {count}")
    else:
        lines.append("  - None")

    invalid_patients = report.get("invalid_patients", [])
    lines.append("Invalid Patients:")
    if invalid_patients:
        for item in invalid_patients:
            lines.append(f"  - {item['patient']} -> {item['errors']}")
    else:
        lines.append("  - None")

    lines.append("=" * 70)
    formatted_report = "\n".join(lines)
    print(formatted_report)
    return formatted_report