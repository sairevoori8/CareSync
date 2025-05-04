document.querySelector("form").addEventListener("submit", async function (e) {
    e.preventDefault(); // Prevent page reload
  
    try {
      const selected = Array.from(document.querySelectorAll('input[name="symptoms"]:checked'))
                            .map(cb => cb.value);
  
      const response = await fetch("http://127.0.0.1:5000/analysis", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ symptoms: selected })
      });
  
      if (!response.ok) {
        alert("server busy")
        throw new Error("Network response was not ok");
      }
  
      const result = await response.json();
      console.log(result)
      openPopup(result)
  
  
    } catch (error) {
      console.error("Error during prediction:", error);
      alert("An error occurred: " + error.message);
    }
  });
function openPopup(des) {
    document.getElementById("popup").style.display = "block";
    document.getElementById("popup").innerHTML=`<h1>Analysis of desease</h1>
        <h2>${des}</h2><div class="cenbtn">
        <button class="btn" onclick='closePopup()'>Close</buttton></div>`;
    document.getElementById("overlay").style.display = "block";
}
  
function closePopup() {
    document.getElementById("popup").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}
  
  