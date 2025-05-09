from blockchain import Blockchain
import random

# Initialize blockchain
blockchain = Blockchain()

# Sample data pools
first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah"]
last_names = ["Smith", "Doe", "Brown", "Johnson", "Williams", "Taylor", "Davis", "Miller", "Wilson", "Moore"]
genders = ["Male", "Female", "Other"]
activities = ["Low", "Moderate", "High"]
lifestyles = ["Non-smoker", "Smoker", "Occasional drinker", "Non-smoker, occasional drinker"]
illnesses = ["Flu", "Chickenpox", "Malaria", "Dengue"]
surgeries = ["Appendix Removal", "Gallbladder Surgery", "Knee Replacement", "None"]
family_histories = ["Diabetes", "Hypertension", "Heart Disease", "None"]
medications = ["Paracetamol", "Ibuprofen", "Vitamin D", "None"]
allergies = ["Peanuts", "Dust", "Pollen", "None"]
conditions = ["Hypertension", "Asthma", "Diabetes", "None"]
vaccinations = ["Tetanus", "Hepatitis B", "COVID-19", "MMR"]

def generate_random_record(index):
    first = random.choice(first_names)
    last = random.choice(last_names)
    full_name = f"{first} {last}"
    age = random.randint(18, 70)
    gender = random.choice(genders)
    address = f"{random.randint(1, 999)} Main St, City {index}"
    phone = f"+1-555-{random.randint(1000, 9999)}"
    email = f"{first.lower()}.{last.lower()}{index}@example.com"
    emergency_contact = f"+1-555-{random.randint(1000, 9999)}"
    occupation = random.choice(["Engineer", "Doctor", "Teacher", "Artist", "Manager"])
    insurance_provider = f"HealthCare {random.randint(100, 999)}"
    height = random.randint(150, 190)
    weight = random.randint(50, 100)
    
    return {
        "Full Name": full_name,
        "Age": age,
        "Gender": gender,
        "Address": address,
        "Phone": phone,
        "Email": email,
        "Emergency Contact": emergency_contact,
        "Occupation": occupation,
        "Insurance Provider": insurance_provider,
        "Height (cm)": height,
        "Weight (kg)": weight,
        "Activity Level": random.choice(activities),
        "Lifestyle": random.choice(lifestyles),
        "Past Illnesses": ", ".join(random.sample(illnesses, k=2)),
        "Past Surgeries": random.choice(surgeries),
        "Family History": random.choice(family_histories),
        "Medications": ", ".join(random.sample(medications, k=2)),
        "Allergies": random.choice(allergies),
        "Chronic Conditions": random.choice(conditions),
        "Vaccinations": ", ".join(random.sample(vaccinations, k=2))
    }

# Add 30 records
for i in range(30):
    record = generate_random_record(i)
    print(blockchain.add_medical_record(record))
    print(blockchain.mine_block())
    print(f"Record {i+1} added.")

# Mine the block
print("Mining block...")

