document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM fully loaded and parsed");
    get_data();
    
    async function get_data(){
        try{
            const result = await fetch('http://127.0.0.1:5000/basic')
            const data =  await result.json()
            document.getElementById('display').innerHTML=`<div class='dis'>Total Blocks : ${data.Blocks}</div>
            <img src="assets/block.webp" alt="CareSync Blockchain Background" height=100px><div class='dis'>Last Hash</div><div class='dis'>${data.lasthash}</div>`
            console.log(data)
        }
        catch(err){
            console.log('an error occur',err)
            alert('Erorr occured while loading')
        }
    
    }
  });