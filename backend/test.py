'''from blockchain import Blockchain
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
print(blockchain.get_last_block())'''

from cryptography.fernet import Fernet

# Key and encrypted data
key = b"vZUuYfHnem5w6_JFw6cqSWrzAFPAYov8QP92KFEj8BQ="
token = b"gAAAAABn3ug_rxKrbDISvxN_2FmxtshVoJ-5JOW7V0iNwC2hPtC1mwUa3X_tQc_rmIxcKqWT0r1cG6JzVTyLKDCpKLDatW4H9G8-21afepn4rZmY1HbLqZEmTA53lQ_OI8CJGz2RStAqGHs6BxOKf8DdLSWZkjOs8Yw5y0tTN50lqeB5NJs1iROmy23-qYdD4wfUGy1jcTB_UJSkwh-L57oIY-Ol9tKQwGWGuPbWA43ix6US270t1TdEj8Nj2VZhevO_AwddzP2yKPQFh7djiFH1I2s50_fV9y9T_CHWRLw4LSm0z2ts5IoZxUjyHF2IbOujdTUIKprFKynVe4peXZGvBKRIAbnx_wT0mHliGdy4d4XyE-9hDLcSvMH8U5CuK7uKZgVwKcyrjgPveCub2KphqZUl7uZ9ER7aLZ01uI8QRu7aLX4h4KCmAo3bMjhDyTjc0yOXsVzde58PioinrmojZMFBG9MWU_P1jXMR98fyhLp0_NTbnGbuCtIS5MxFc8pzMnqO7y5qvZFsYwtc6rI7ZTBl5o3KKXtX5MT6pOhRxNN168fx6BRcL2yMqrFvZrskzGaehPYRdS8QbD7Y1uGkA3GzT174AmzWDYQALEY43OzRapEvAgcWMn4dfcQkrKwNELQn9s87IS8TN5zz858JdMrIGh0e95X6n-B-tQCs1p_4w9L1t7LvXnaiyvNHmct0qV1O7e9yOO8ixjOB0tm5wuXmqGZ-KmnBMQlsNP_Z_J5FpgrqNK1aTz8ZK7VqAplL4OSbbG8gM-EEfiY2r_lS_-Aogm8gu_H5YeOoNWb1bXxw8A2HMEe0BhKRS5Vzg5amznQTSWdrRsc0f63AXG6u2OODAPBvqNphIBQgm34JAgdAESgUqJU="

# Decryption
f = Fernet(key)
decrypted = f.decrypt(token)

print(decrypted.decode())

