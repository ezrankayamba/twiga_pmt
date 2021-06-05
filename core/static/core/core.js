"use strict";

function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance"); }

function _iterableToArray(iter) { if (Symbol.iterator in Object(iter) || Object.prototype.toString.call(iter) === "[object Arguments]") return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = new Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } }

function docReady(fn) {
  if (document.readyState === "complete" || document.readyState === "interactive") {
    setTimeout(fn, 1);
  } else {
    document.addEventListener("DOMContentLoaded", fn);
  }
}

var dynamicColor = function dynamicColor() {
  var r = Math.floor(Math.random() * 255);
  var g = Math.floor(Math.random() * 255);
  var b = Math.floor(Math.random() * 255);
  return "rgb(" + r + "," + g + "," + b + ")";
};

var dashboard_loadtypes = function dashboard_loadtypes() {
  var chartEl = document.getElementById("projectType");
  var ctx = chartEl.getContext("2d");
  var data = {
    datasets: [{
      data: []
    }],
    labels: []
  };
  var options = {
    plugins: {
      datalabels: {
        formatter: function formatter(value, context) {
          return context.chart.data.datasets[0][context.dataIndex];
        },
        color: "#f1f1f1"
      }
    },
    legend: {
      display: false
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    },
    layout: {
      padding: {
        right: 20
      }
    }
  };
  var myPieChart = new Chart(ctx, {
    type: "bar",
    data: data,
    options: options
  });
  fetch(chartEl.dataset.url).then(function (res) {
    return res.json();
  }).then(function (res) {
    console.log(res);
    myPieChart.data.datasets = [{
      data: res.data,
      backgroundColor: res.data.map(dynamicColor)
    }];
    myPieChart.data.labels = res.labels;
    myPieChart.update();
    console.log(myPieChart);
  }).catch(function (err) {
    console.error(err);
  });
};

var dashboard_loadstatuses = function dashboard_loadstatuses() {
  var chartEl = document.getElementById("projectStatus");
  var ctx = chartEl.getContext("2d");
  var data = {
    datasets: [{
      data: []
    }],
    labels: []
  };
  var options = {
    plugins: {
      datalabels: {
        formatter: function formatter(value, context) {
          return context.chart.data.datasets[0][context.dataIndex];
        },
        color: "#f1f1f1"
      }
    },
    legend: {
      position: "right",
      align: "middle"
    },
    layout: {
      padding: {
        right: 20
      }
    }
  };
  var myPieChart = new Chart(ctx, {
    type: "pie",
    data: data,
    options: options
  });
  fetch(chartEl.dataset.url).then(function (res) {
    return res.json();
  }).then(function (res) {
    console.log(res);
    myPieChart.data.datasets = [{
      data: res.data,
      backgroundColor: res.data.map(dynamicColor)
    }];
    myPieChart.data.labels = res.labels;
    myPieChart.update();
    console.log(myPieChart);
  }).catch(function (err) {
    console.error(err);
  });
};

var dashboard_loadsizes = function dashboard_loadsizes() {
  var chartEl = document.getElementById("projectSize");
  var ctx = chartEl.getContext("2d");
  var data = {
    datasets: [{
      data: []
    }],
    labels: []
  };
  var options = {
    plugins: {
      datalabels: {
        formatter: function formatter(value, context) {
          return context.chart.data.datasets[0][context.dataIndex];
        },
        color: "#f1f1f1"
      }
    },
    legend: {
      position: "right",
      align: "middle"
    },
    layout: {
      padding: {
        right: 20
      }
    }
  };
  var myPieChart = new Chart(ctx, {
    type: "pie",
    data: data,
    options: options
  });
  fetch(chartEl.dataset.url).then(function (res) {
    return res.json();
  }).then(function (res) {
    console.log(res);
    myPieChart.data.datasets = [{
      data: res.data,
      backgroundColor: res.data.map(dynamicColor)
    }];
    myPieChart.data.labels = res.labels;
    myPieChart.update();
    console.log(myPieChart);
  }).catch(function (err) {
    console.error(err);
  });
};

var dashboard_loadsuppliers = function dashboard_loadsuppliers() {
  var chartEl = document.getElementById("projectSupplier");
  var ctx = chartEl.getContext("2d");
  var data = {
    datasets: [{
      data: []
    }],
    labels: []
  };
  var options = {
    plugins: {
      datalabels: {
        formatter: function formatter(value, context) {
          return context.chart.data.datasets[0][context.dataIndex];
        },
        color: "#f1f1f1"
      }
    },
    legend: {
      position: "right",
      align: "middle"
    },
    layout: {
      padding: {
        right: 20
      }
    }
  };
  var myPieChart = new Chart(ctx, {
    type: "pie",
    data: data,
    options: options
  });
  fetch(chartEl.dataset.url).then(function (res) {
    return res.json();
  }).then(function (res) {
    console.log(res);
    myPieChart.data.datasets = [{
      data: res.data,
      backgroundColor: res.data.map(dynamicColor)
    }];
    myPieChart.data.labels = res.labels;
    myPieChart.update();
    console.log(myPieChart);
  }).catch(function (err) {
    console.error(err);
  });
};

var dashboard_loadregions = function dashboard_loadregions() {
  var chartEl = document.getElementById("projectRegion");
  var ctx = chartEl.getContext("2d");
  var fullData = [];
  var labels = [];
  var data = {
    datasets: [{
      data: []
    }],
    labels: []
  };

  var makeToolTip = function makeToolTip(tooltipModel, ctx) {
    var info = tooltipModel.dataPoints;
    var tooltipEl = document.getElementById("per-region-tooltip");

    if (!tooltipEl) {
      tooltipEl = document.createElement("div");
      tooltipEl.id = "per-region-tooltip";
      tooltipEl.innerHTML = "\n                <div class=\"my_tootip shadow bg-white pl-2 pr-2\">\n                    <h6 class=\"title\">My Title</h6>\n                    <div class=\"districts text-muted\"></div>\n                </div>\n            ";
      document.body.appendChild(tooltipEl);
    }

    if (tooltipModel.opacity === 0) {
      tooltipEl.style.opacity = 0;
      return;
    }

    if (tooltipModel.yAlign) {
      tooltipEl.classList.add(tooltipModel.yAlign);
    } else {
      tooltipEl.classList.add("no-transform");
    }

    function getBody(bodyItem) {
      return bodyItem.lines;
    }

    if (tooltipModel.body) {
      var root = tooltipEl.querySelector(".my_tootip");

      if (info) {
        var label = labels[info[0].index];
        var region = fullData[label];
        root.querySelector(".title").textContent = "".concat(label, " (").concat(region.count, ")");
        var div = root.querySelector(".districts");

        while (div.firstChild) {
          div.removeChild(div.firstChild);
        }

        var listD = region.districts;
        console.log("ListD: ", listD);

        for (var d in listD) {
          var p = document.createElement("p");
          p.textContent = "".concat(d, ": ").concat(listD[d]);
          p.classList.add(["mb-0"]);
          div.appendChild(p);
        }
      }
    }

    var position = ctx._chart.canvas.getBoundingClientRect();

    tooltipEl.style.opacity = 1;
    tooltipEl.style.position = "absolute";
    tooltipEl.style.left = position.left + window.pageXOffset + tooltipModel.caretX + "px";
    tooltipEl.style.top = position.top + window.pageYOffset + tooltipModel.caretY + "px";
    tooltipEl.style.fontFamily = tooltipModel._bodyFontFamily;
    tooltipEl.style.fontSize = tooltipModel.bodyFontSize + "px";
    tooltipEl.style.fontStyle = tooltipModel._bodyFontStyle;
    tooltipEl.style.padding = tooltipModel.yPadding + "px " + tooltipModel.xPadding + "px";
    tooltipEl.style.pointerEvents = "none";
  };

  var options = {
    plugins: {
      datalabels: {
        formatter: function formatter(value, context) {
          var info = context.chart.data.datasets[0];
          return info.data[context.dataIndex];
        },
        color: "#f1f1f1"
      }
    },
    legend: {
      display: false
    },
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    },
    tooltips: {
      enabled: false,
      custom: function custom(model) {
        makeToolTip(model, this, fullData);
      }
    },
    layout: {
      padding: {
        right: 20
      }
    }
  };
  var myPieChart = new Chart(ctx, {
    type: "bar",
    data: data,
    options: options
  });
  fetch(chartEl.dataset.url).then(function (res) {
    return res.json();
  }).then(function (res) {
    console.log(res);
    fullData = res.full;
    labels = res.labels;
    myPieChart.data.datasets = [{
      data: res.data,
      backgroundColor: res.data.map(dynamicColor)
    }];
    myPieChart.data.labels = res.labels;
    myPieChart.update();
  }).catch(function (err) {
    console.error(err);
  });
};

var initMap = function initMap() {
  var map;
  var mapEl = document.getElementById("map");
  var url = mapEl.dataset.url;
  map = new google.maps.Map(mapEl, {
    center: {
      lat: -6.192,
      lng: 35.7699
    },
    zoom: 6
  });
  var infoWindows = [];

  var closeOpen = function closeOpen() {
    infoWindows.forEach(function (w) {
      w.close();
    });
  };

  fetch(url).then(function (res) {
    return res.json();
  }).then(function (res) {
    var json = res.data;
    json.forEach(function (p) {
      var name = p.name;
      var id = p.id;
      var latLng = {
        lat: parseFloat(p.lat),
        lng: parseFloat(p.lng)
      };
      var c_html = "<div>Main Contractor(s):<ul class=\"pl-3\">";
      p.contractors.forEach(function (c) {
        c_html += "<li>".concat(c, "</li>");
      });
      c_html += "</ul></div>";
      var contentString = "\n        <p class=\"mb-1 lead text-success\">".concat(name, "</p>\n        <p class=\"mb-1\">Authority: ").concat(p.authority, "</p>\n        <p class=\"mb-1\">Quantity: ").concat(p.qty, "</p>\n        ").concat(c_html, "\n        <a class=\"btn btn-outline-secondary btn-sm\" href=\"").concat(p.url, "\">Open details</a>\n        ");
      var infowindow = new google.maps.InfoWindow({
        content: contentString
      });
      infoWindows.push(infowindow);
      var marker = new google.maps.Marker({
        position: latLng,
        map: map,
        draggable: false
      });
      marker.addListener("click", function () {
        closeOpen();
        infowindow.open(map, marker);
      });
    });
  });
};

var popupWindow;
var loadDistrUrl;

var refreshOnRegion = function refreshOnRegion(el, cb) {
  document.querySelector("#btn_select_district").disabled = el.value ? false : true;
  var id = el.value | 0;
  fetch("".concat(window.location.origin).concat(loadDistrUrl, "?region=").concat(id)).then(function (res) {
    return res.text();
  }).then(function (res) {
    document.querySelector("#id_district").innerHTML = res;
    cb();
  }).catch(function (error) {
    console.log("Request failed", error);
  });
};

function addOtherPopupHandler(baseUrl, btn) {
  //data-toggle="modal" data-target="#mapModel"
  btn.dataset.toggle = "modal";
  btn.dataset.target = "#setup-model";
  btn.addEventListener("click", function (e) {
    var url = btn.dataset.url;
    url = baseUrl + url;

    if (btn.id === "btn_select_district") {
      url = "".concat(url, "?region=").concat(document.querySelector("#id_region").value);
    }

    console.log(url); // popupCenter(url, "popUpWindow", w, h);

    fetch(url).then(function (res) {
      return res.text();
    }).then(function (html) {
      // console.log(html)
      var form = document.getElementById("setup-model-form");
      form.innerHTML = html;
      var btnSubmit = document.getElementById("btn-model-submit");

      btnSubmit.onclick = function () {
        var data = new FormData(form.querySelector("form"));
        var object = {};
        data.forEach(function (value, key) {
          object[key] = value;
        });
        var json = JSON.stringify(object);
        console.log("Submit: ", url, json);
        fetch(url, {
          method: "post",
          body: data
        }).then(function (res) {
          return res.text();
        }).then(function (text) {
          console.log(text);
          var regex = /closePopup\((\d+), "([\w ]+)", "(#[\w]+)"\);/g;

          var params = _toConsumableArray(text.matchAll(regex));

          var id = parseInt(params[0][1]);
          var name = params[0][2]; // let elId = params[0][3];

          var elId = btn.parentElement.querySelector(".select").id;
          elId = "#".concat(elId);
          console.log(id, name, elId);
          closePopup(id, name, elId);
        }).catch(function (err) {
          console.log(err);
        });
      };
    });
  });
}

function editOtherPopupHandler(baseUrl, btn) {
  //data-toggle="modal" data-target="#mapModel"
  btn.dataset.toggle = "modal";
  btn.dataset.target = "#setup-model";
  btn.addEventListener("click", function (e) {
    var sel = e.target.parentElement.parentElement.querySelector('select');
    if (!sel.value) return; // console.log(sel.value)

    var url = btn.dataset.url.replace(/.$/, sel.value);
    url = baseUrl + url;

    if (btn.id === "btn_select_district") {
      url = "".concat(url, "?region=").concat(document.querySelector("#id_region").value);
    }

    console.log(url); // popupCenter(url, "popUpWindow", w, h);

    fetch(url).then(function (res) {
      return res.text();
    }).then(function (html) {
      // console.log(html)
      var form = document.getElementById("setup-model-form");
      form.innerHTML = html;
      var btnSubmit = document.getElementById("btn-model-submit");

      btnSubmit.onclick = function () {
        var data = new FormData(form.querySelector("form"));
        var object = {};
        data.forEach(function (value, key) {
          object[key] = value;
        });
        var json = JSON.stringify(object);
        console.log("Submit: ", url, json);
        fetch(url, {
          method: "POST",
          body: data
        }).then(function (res) {
          return res.text();
        }).then(function (text) {
          console.log(text);
          var regex = /closePopup\((\d+), "([\w ]+)", "(#[\w]+)"\);/g;

          var params = _toConsumableArray(text.matchAll(regex));

          var id = parseInt(params[0][1]);
          var name = params[0][2]; // let elId = params[0][3];

          var elId = btn.parentElement.querySelector(".select").id;
          elId = "#".concat(elId);
          console.log(id, name, elId);
          closePopup(id, name, elId);
        }).catch(function (err) {
          console.log(err);
        });
      };
    });
  });
}

var load_form_js = function load_form_js(urls) {
  // console.log(urls)
  loadDistrUrl = urls.querySelector(".popup-setups-load-districts").value;

  (function () {
    console.log(loadDistrUrl);
    document.querySelector("#id_region").addEventListener("change", function (e) {
      console.log(e);
      var el = e.target;
      refreshOnRegion(el, function () {
        console.log("Loaded successfully");
      });
    });
    var w = window.innerWidth / 2;
    var h = window.innerHeight * 3 / 5;
    var baseUrl = window.location.origin;
    var regionSel = undefined;
    [{
      name: "type",
      url: urls.querySelector(".popup-setups-type-create").value
    }, {
      name: "region",
      url: urls.querySelector(".popup-setups-region-create").value
    }, {
      name: "district",
      url: urls.querySelector(".popup-setups-district-create").value
    }, {
      name: "authority",
      url: urls.querySelector(".popup-setups-authority-create").value
    }, {
      name: "status",
      url: urls.querySelector(".popup-setups-status-create").value
    }, {
      name: "size",
      url: urls.querySelector(".popup-setups-size-create").value
    }].forEach(function (fld) {
      var name = fld.name; // console.log(fld, name)

      var container = document.querySelector("#div_id_".concat(name));

      if (container) {
        var sel = container.querySelector("select");
        var btn = null;

        function addBtn(name) {
          var btn = document.createElement("button");
          btn.innerHTML = "<i class=\"fa fa-plus\"></i>";
          btn.classList.add("btn");
          btn.classList.add("btn-link");
          btn.classList.add("text-secondary");
          btn.classList.add("pr-0");
          btn.classList.add("pl-1");
          btn.dataset.url = fld.url;
          btn.type = "button";
          btn.classList.add("".concat(name, "-other"));
          btn.title = "".concat(name, " other");

          if (name === "district") {
            btn.disabled = document.querySelector("#id_region").value ? false : true;
            btn.id = "btn_select_district";
          }
        } // addBtn('add')


        addBtn('edit');
        sel.parentNode.insertBefore(btn, sel.nextSibling);
        sel.parentElement.classList.add("d-flex");

        if (name === "region") {
          regionSel = sel;
        }

        if (name === "district") {
          var tmp = sel.value;
          refreshOnRegion(regionSel, function () {
            sel.value = tmp;
          });
        }
      }
    });
    var list = document.querySelectorAll(".add-other");

    for (var i = 0; i < list.length; i++) {
      var btn = list[i];
      addOtherPopupHandler(baseUrl, btn);
    }
  })();

  function popupCenter(url, title, w, h) {
    var dualScreenLeft = window.screenLeft != undefined ? window.screenLeft : window.screenX;
    var dualScreenTop = window.screenTop != undefined ? window.screenTop : window.screenY;
    var width = window.innerWidth ? window.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
    var height = window.innerHeight ? window.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;
    var systemZoom = width / window.screen.availWidth;
    var left = (width - w) / 2 / systemZoom + dualScreenLeft;
    var top = (height - h) / 2 / systemZoom + dualScreenTop;
    top = top * 3 / 10;
    popupWindow = window.open(url, title, "resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes,width=" + w / systemZoom + ", height=" + h / systemZoom + ", top=" + top + ", left=" + left);
    if (window.focus) popupWindow.focus();
  }
};

var closePopup = function closePopup(newID, newRepr, id) {
  var x = document.querySelector(id);
  console.log("Exist?", x.value, newID);
  var exists = newID == x.value;
  console.log(x.value, newID);
  var option = exists ? x.options[x.selectedIndex] : document.createElement("option");
  option.text = newRepr;
  option.selected = true;
  option.value = newID;
  if (!exists) x.add(option);
  console.log("Select: ", x);

  if (x.id === "id_region") {
    refreshOnRegion(x);
  }

  console.log(newID, newRepr, id); // popupWindow.close();
};

var initMapOnForm = function initMapOnForm() {
  function markerLocation() {
    var loc = marker.getPosition();
    document.querySelector("input[name=longitude]").value = loc.lng();
    document.querySelector("input[name=latitude]").value = loc.lat();
    document.querySelector("#coordinates").textContent = "(".concat(loc.lng().toFixed(4), ", ").concat(loc.lat().toFixed(4), ")");
  }

  var map; //Will contain map object.

  var marker = false;
  map = new google.maps.Map(document.getElementById("map"), {
    center: {
      lat: -6.192,
      lng: 35.7699
    },
    zoom: 6
  });
  google.maps.event.addListener(map, "click", function (event) {
    var clickedLocation = event.latLng;

    if (marker === false) {
      marker = new google.maps.Marker({
        position: clickedLocation,
        map: map,
        draggable: true //make it draggable

      });
      google.maps.event.addListener(marker, "dragend", function (event) {
        markerLocation();
      });
    } else {
      marker.setPosition(clickedLocation);
    }

    markerLocation();
  });
};

var setLocation = function setLocation(loc, err) {};

var form_capture_GPS = function form_capture_GPS() {
  document.querySelector("#captureGPS").addEventListener("click", function (e) {
    console.log("Capture location");

    if (navigator.geolocation) {
      console.log("GPS Supported2");
      var options = {
        timeout: 60000,
        //2 minutes timeout
        maximumAge: 180000 //3 minutes ago

      };
      navigator.geolocation.getCurrentPosition(function (loc) {
        console.log("OnLocation");
        console.log(loc);
        document.querySelector("input[name=longitude]").value = loc.coords.longitude;
        document.querySelector("input[name=latitude]").value = loc.coords.latitude;
        document.querySelector("#coordinates").textContent = "(" + loc.coords.longitude.toFixed(4) + "," + loc.coords.latitude.toFixed(4) + ")";
      }, function (err) {
        console.log("OnError: ", err.code, err.message);
        console.log(err);
      }, options);
    } else {
      console.error("No GPS Capture Support!");
      alert("No GPS Capture Support!");
    }
  });
};

var handleUploadJs = function handleUploadJs() {
  var btnImport = document.getElementById("btnImport");
  var fInput = document.getElementById("file");
  var confirmTrigger = document.getElementById("confirmTrigger");
  var confirmed = document.getElementById("confirmed");
  var file;
  fInput.addEventListener("change", function (e) {
    file = e.target.files[0];
    console.log("Selected", file);
    document.getElementById("txtFile").innerHTML = file.name;

    if (file) {
      confirmTrigger.click();
    }
  }, false);
  btnImport.addEventListener("click", function () {
    fInput.click();
  });
  console.log(btnImport);

  var upload = function upload(file, url) {
    var xhr = new XMLHttpRequest();
    var fd = new FormData();
    xhr.open("POST", url, true);

    xhr.onreadystatechange = function () {
      if (xhr.readyState == 4 && xhr.status == 200) {
        console.log(xhr.responseText);
        location.reload(true);
      }
    };

    fd.append("file", file);
    fd.append("csrfmiddlewaretoken", document.querySelector("input[name='csrfmiddlewaretoken']").value);
    xhr.send(fd);
  };

  confirmed.addEventListener("click", function (e) {
    var url = e.target.dataset.url;
    console.log("Confirmed", file, url);
    upload(file, url);
  });
};

var filter_form_rerender = function filter_form_rerender() {
  (function () {
    var getEl = function getEl(selector, prnt) {
      return prnt.querySelector(selector);
    };

    var addCls = function addCls(el, cls) {
      cls.split(" ").forEach(function (cl) {
        el.classList.add(cl);
      });
    };

    var form = document.querySelector("#filter-form");
    var inputNodes = form.querySelectorAll(".form-group");

    for (var i = 0; i < inputNodes.length; i++) {
      var grp = inputNodes[i];
      addCls(grp, "input-group input-group-sm mr-2 mt-2");
      var label = getEl("label", grp);
      var div = document.createElement("div");
      var span = document.createElement("span");
      addCls(div, "input-group-prepend");
      addCls(span, "input-group-text");
      span.textContent = label.textContent;
      grp.removeChild(label);
      div.appendChild(span);
      var inputDiv = getEl("div", grp);
      var crtr = getEl(".form-control", inputDiv);
      grp.removeChild(inputDiv);
      grp.appendChild(div);
      grp.appendChild(crtr);
    }

    var fltOnPag = document.querySelector(".filter-on-pagination");

    if (fltOnPag) {
      var selNodes = document.querySelector(".filter-on-pagination").querySelectorAll(".select");

      for (var _i = 0; _i < selNodes.length; _i++) {
        var sel = selNodes[_i];
        sel.id = "".concat(sel.id, "_1");
      }

      var txtNodes = document.querySelector(".filter-on-pagination").querySelectorAll(".textinput");

      for (var _i2 = 0; _i2 < txtNodes.length; _i2++) {
        var txt = txtNodes[_i2];
        txt.id = "".concat(txt.id, "_1");
      }
    }

    handleUploadJs();
  })();
};