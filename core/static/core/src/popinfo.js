"use strict";

var host = window.location.host;
var prot = window.location.protocol;
var url = (prot === "https:" ? "wss" : "ws") + "://" + host + "/popinfo/ws/";


(function () {
  var path = window.location.pathname.replace(/\/+$/, "");
  console.log("App started!", path);

  if (path === "/popinfo/admin") {
    var connection = new WebSocket(url);
    console.log("Admin page");

    connection.onopen = function () {
      console.log("Connected");
    };

    var elements = document.querySelectorAll(".btn-broadcast");

    for (var i = elements.length - 1; i >= 0; i--) {
      var el = elements[i];
      el.addEventListener("click", function (e) {
        var btn = e.target;
        var id = btn.dataset.id;
        var data = JSON.stringify({
          cmd: "broadcast",
          id: id
        });
        console.log(data);
        connection.send(JSON.stringify(data));

      });
    }
     connection.onmessage = (e)=>{
        var data = JSON.parse(e.data).message;
        console.log(data);
        location.reload(true)
     }
  } else if (path === "/popinfo"){
    var connection = new WebSocket(url);
    console.log("Other users");

    connection.onopen = function () {
      console.log("Connected");
    };

    connection.onmessage = function (e) {
      console.log(e.data);
      document.querySelector("#distributor").classList.remove("hide");
      var data = JSON.parse(e.data).message;
      console.log(data);

      var setValue = function setValue(cls, value) {
        document.querySelector("." + cls).innerHTML = value;
      };

      setValue("title", data.title);
      setValue("winner", data.winner);
      let ul=document.querySelector(".facts-list");
      ul.innerHTML=""
      data.facts.forEach((f)=>{
          let li=document.createElement("li")
          li.classList.add('card-mutted')
          li.classList.add('text-mutted')
          li.innerHTML=f;
          ul.appendChild(li)
      })
      navigator.vibrate = navigator.vibrate || navigator.webkitVibrate || navigator.mozVibrate || navigator.msVibrate;
      if ("vibrate" in navigator) {
        navigator.vibrate(1000);
      }else{
        console.log('Vibration  not supported')
      }
    };

    connection.onerror = function (error) {
      console.log("WebSocket error: " + error);
    };
  }
})();
