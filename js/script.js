
/* Navigo routing - defaults */
var root = null;
var useHash = false;
var hash = '#';
var router = new Navigo(root, useHash, hash);

document.getElementById('login_btn').onclick = function(){
    fetch('http://localhost:8080/')
    .then(function(response) {
      return response.json();
    })
    .then(function(json) {
      console.log(JSON.stringify(json));
    });
}

router
.on({'/:userid':  {
as: 'play.show', uses: () => {
  console.log('hejsan');
}
  },
  '*': function () {
    console.log('main')
    }
  }).resolve();

  console.log(router.generate('play.show', {userid: 'alicecold'}));
