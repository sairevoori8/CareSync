document.getElementById('healthForm').addEventListener('submit', function (e) {
  e.preventDefault();

  const formData = new FormData(this);
  const data = {};

  formData.forEach((value, key) => {
    // Convert comma-separated fields to arrays
    if (["past_illnesses", "past_surgeries", "family_history", "medications", "allergies", "chronic_conditions", "vaccinations"].includes(key)) {
      data[key] = value.split(',').map(item => item.trim());
    } else {
      data[key] = value;
    }
  });

  fetch('http://127.0.0.1:5000/insert-data', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  })
    .then(res => res.json())  // Expecting a JSON response
    .then(data => {
      if (data.success) {
        alert('Form submitted successfully!');
        const resultDiv = document.getElementById('result');  // Make sure this exists
        resultDiv.style.display = 'block';
        resultDiv.innerHTML = `
                 <div class="result-box">
                  <h2>Block Added Successfully ✅</h2>
                      <p><strong>Block Index:</strong> ${data.block_data.index}</p>
                  <p><strong>Block Hash:</strong> <code>${data.block_data.hash}</code></p>
                  </div>`;
      } else {
        alert('Submission failed. ' + data.message);  // Handle server-specific errors
      }
    })
    .catch(err => {
      console.error('Error:', err);
      alert('Server error. Please try again later.');
    });
});
