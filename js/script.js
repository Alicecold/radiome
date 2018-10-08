document.getElementById('login_btn').onclick = function(){
    fetch('http://localhost:8080/')
    .then(function(response) {
      return response.json();
    })
    .then(function(json) {
      console.log(JSON.stringify(json));
    });
}
