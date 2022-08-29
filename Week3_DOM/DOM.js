<script type="text/javascript">
  function setTime(){
  setTimeout(function(){
    alert('hello');
  },3000)
}

let id;
function setInter(){
  let num = 0
  id = setInterval(function(){
    console.log(num);
    num ++
  },1000);
}

function clearInter(){
  clearInterval(id);
}

let root = document.getElementById('root');

let outer = document.createElement('div');
let inner = document.createElement('div');
outer.classList.add('outer');
inner.classList.add('inner');
inner.setAttribute('id','main');
outer.appendChild(inner);
root.appendChild(outer);

function myMove() {
  var elem = document.getElementById("main");
  var pos = 0;
  let id = setInterval(function() {
    if (pos == 350) {
      clearInterval(id);
    }
    else {
      pos++;
      elem.style.top = pos + "px";
      elem.style.left = pos + "px";
    }
  }, 5);
}
</script>