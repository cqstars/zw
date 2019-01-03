var ajax = new XMLHttpRequest();
ajax.open('get','getStar.php?starName='+name);
ajax.send();
ajax.onreadystatechange = function () {
   if (ajax.readyState==4 &&ajax.status==200) {
　　　　console.log(ajax.responseText);//输入相应的内容
  　　}
}