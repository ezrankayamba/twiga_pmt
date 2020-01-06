"use strict";

var host = window.location.host;
var prot = window.location.protocol;
var url = (prot === "https:" ? "wss" : "ws") + "://" + host + "/popinfo/ws/";

(function () {
  var path = window.location.pathname;
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
  } else if (path === "/popinfo") {
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

      setValue("card-title", data.name);
      setValue("card-subtitle", "Aged: " + data.age);
      setValue("card-text", "This distributor executed his duties for " + data.projects + " project(s) and managed to archieve a performance of " + data.performance + "%");
    };

    connection.onerror = function (error) {
      console.log("WebSocket error: " + error);
    };
  }
})();