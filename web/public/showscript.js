async function get_data() {
    const index = document.getElementById('userIndex').value;
    if (index === '') {
      alert('Please enter a valid index');
      return;
    }
  
    const url = `http://127.0.0.1:5000/get-user-details/${index}`;
    try {
      const response = await fetch(url);
      if (!response.ok) throw new Error(`Status: ${response.status}`);
      const data = await response.json();
  
      let html = '<table><thead><tr><th>Field</th><th>Value</th></tr></thead><tbody>';
  
      for (let key in data) {
        if (key === 'records' && Array.isArray(data[key])) {
          data[key].forEach((record, idx) => {
            html += `<tr><td colspan="2"><strong>Record #${idx + 1}</strong></td></tr>`;
            for (let subKey in record) {
              let value = Array.isArray(record[subKey]) ? record[subKey].join(', ') : record[subKey];
              html += `<tr><td>${subKey}</td><td>${value}</td></tr>`;
            }
          });
        } else {
          let value = typeof data[key] === 'object' ? JSON.stringify(data[key]) : data[key];
          html += `<tr><td>${key}</td><td>${value}</td></tr>`;
        }
      }
  
      html += '</tbody></table>';
      document.getElementById('result').innerHTML = html;
    } catch (error) {
      document.getElementById('result').innerHTML = `<p class="error">Error: ${error.message}</p>`;
    }
  }
  