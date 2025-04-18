from blockchain import Blockchain
# Initialize blockchain
blockchain = Blockchain()

# Add a medical record
print(blockchain.add_medical_record(
    patient_id="123456",
    full_name="John Doe",
    dob="1990-05-20",
    gender="Male",
    address="123 Street, NY, USA",
    phone="123-456-7890",
    email="john.doe@example.com",
    emergency_contact="Jane Doe - 987-654-3210",
    past_illnesses=["Flu", "Chickenpox"],
    past_surgeries=["Appendix Removal"],
    family_history=["Diabetes"],
    medications=["Paracetamol"],
    allergies=["Peanuts"],
    chronic_conditions=["Hypertension"],
    vaccinations=["COVID-19", "Hepatitis B"],
    insurance="HealthFirst",
    occupation="Software Engineer",
    lifestyle="Non-smoker, occasional drinker"
))

# Mine the block (store it in MongoDB)
print(blockchain.mine_block())
print(blockchain.get_last_block())
