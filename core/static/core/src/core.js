"use strict";

function docReady(fn) {
    if (
        document.readyState === "complete" ||
        document.readyState === "interactive"
    ) {
        setTimeout(fn, 1);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}
let dynamicColor = () => {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgb(" + r + "," + g + "," + b + ")";
};

let dashboard_loadtypes = () => {
    let chartEl = document.getElementById("projectType");
    var ctx = chartEl.getContext("2d");
    let data = {
        datasets: [
            {
                data: []
            }
        ],
        labels: []
    };
    let options = {
        plugins: {
            datalabels: {
                formatter: function (value, context) {
                    return context.chart.data.datasets[0][context.dataIndex];
                },
                color: "#f1f1f1"
            }
        },
        legend: {
            display: false
        },
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true
                    }
                }
            ]
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
    fetch(chartEl.dataset.url)
        .then(res => res.json())
        .then(res => {
            console.log(res);
            myPieChart.data.datasets = [
                {
                    data: res.data,
                    backgroundColor: res.data.map(dynamicColor)
                }
            ];
            myPieChart.data.labels = res.labels;
            myPieChart.update();
            console.log(myPieChart);
        })
        .catch(err => {
            console.error(err);
        });
};

let dashboard_loadstatuses = () => {
    let chartEl = document.getElementById("projectStatus");
    var ctx = chartEl.getContext("2d");
    let data = {
        datasets: [
            {
                data: []
            }
        ],
        labels: []
    };
    let options = {
        plugins: {
            datalabels: {
                formatter: function (value, context) {
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
    fetch(chartEl.dataset.url)
        .then(res => res.json())
        .then(res => {
            console.log(res);
            myPieChart.data.datasets = [
                {
                    data: res.data,
                    backgroundColor: res.data.map(dynamicColor)
                }
            ];
            myPieChart.data.labels = res.labels;
            myPieChart.update();
            console.log(myPieChart);
        })
        .catch(err => {
            console.error(err);
        });
};

let dashboard_loadsizes = () => {
    let chartEl = document.getElementById("projectSize");
    var ctx = chartEl.getContext("2d");
    let data = {
        datasets: [
            {
                data: []
            }
        ],
        labels: []
    };
    let options = {
        plugins: {
            datalabels: {
                formatter: function (value, context) {
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
    fetch(chartEl.dataset.url)
        .then(res => res.json())
        .then(res => {
            console.log(res);
            myPieChart.data.datasets = [
                {
                    data: res.data,
                    backgroundColor: res.data.map(dynamicColor)
                }
            ];
            myPieChart.data.labels = res.labels;
            myPieChart.update();
            console.log(myPieChart);
        })
        .catch(err => {
            console.error(err);
        });
};

let dashboard_loadsuppliers = () => {
    let chartEl = document.getElementById("projectSupplier");
    var ctx = chartEl.getContext("2d");
    let data = {
        datasets: [
            {
                data: []
            }
        ],
        labels: []
    };
    let options = {
        plugins: {
            datalabels: {
                formatter: function (value, context) {
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
    fetch(chartEl.dataset.url)
        .then(res => res.json())
        .then(res => {
            console.log(res);
            myPieChart.data.datasets = [
                {
                    data: res.data,
                    backgroundColor: res.data.map(dynamicColor)
                }
            ];
            myPieChart.data.labels = res.labels;
            myPieChart.update();
            console.log(myPieChart);
        })
        .catch(err => {
            console.error(err);
        });
};

let dashboard_loadregions = () => {
    let chartEl = document.getElementById("projectRegion");
    var ctx = chartEl.getContext("2d");
    let fullData = [];
    let labels = [];
    let data = {
        datasets: [
            {
                data: []
            }
        ],
        labels: []
    };
    let makeToolTip = (tooltipModel, ctx) => {
        let info = tooltipModel.dataPoints;
        var tooltipEl = document.getElementById("per-region-tooltip");
        if (!tooltipEl) {
            tooltipEl = document.createElement("div");
            tooltipEl.id = "per-region-tooltip";
            tooltipEl.innerHTML = `
                <div class="my_tootip shadow bg-white pl-2 pr-2">
                    <h6 class="title">My Title</h6>
                    <div class="districts text-muted"></div>
                </div>
            `;
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
                let label = labels[info[0].index];
                let region = fullData[label];
                root.querySelector(
                    ".title"
                ).textContent = `${label} (${region.count})`;
                let div = root.querySelector(".districts");
                while (div.firstChild) {
                    div.removeChild(div.firstChild);
                }
                let listD = region.districts;
                console.log("ListD: ", listD);
                for (const d in listD) {
                    let p = document.createElement("p");
                    p.textContent = `${d}: ${listD[d]}`;
                    p.classList.add(["mb-0"]);
                    div.appendChild(p);
                }
            }
        }
        var position = ctx._chart.canvas.getBoundingClientRect();
        tooltipEl.style.opacity = 1;
        tooltipEl.style.position = "absolute";
        tooltipEl.style.left =
            position.left + window.pageXOffset + tooltipModel.caretX + "px";
        tooltipEl.style.top =
            position.top + window.pageYOffset + tooltipModel.caretY + "px";
        tooltipEl.style.fontFamily = tooltipModel._bodyFontFamily;
        tooltipEl.style.fontSize = tooltipModel.bodyFontSize + "px";
        tooltipEl.style.fontStyle = tooltipModel._bodyFontStyle;
        tooltipEl.style.padding =
            tooltipModel.yPadding + "px " + tooltipModel.xPadding + "px";
        tooltipEl.style.pointerEvents = "none";
    };
    let options = {
        plugins: {
            datalabels: {
                formatter: function (value, context) {
                    let info = context.chart.data.datasets[0];
                    return info.data[context.dataIndex];
                },
                color: "#f1f1f1"
            }
        },
        legend: {
            display: false
        },
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true
                    }
                }
            ]
        },
        tooltips: {
            enabled: false,
            custom: function (model) {
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
    fetch(chartEl.dataset.url)
        .then(res => res.json())
        .then(res => {
            console.log(res);
            fullData = res.full;
            labels = res.labels;
            myPieChart.data.datasets = [
                {
                    data: res.data,
                    backgroundColor: res.data.map(dynamicColor)
                }
            ];
            myPieChart.data.labels = res.labels;
            myPieChart.update();
        })
        .catch(err => {
            console.error(err);
        });
};

let initMap = () => {
    var map;
    let mapEl = document.getElementById("map");
    let url = mapEl.dataset.url;

    map = new google.maps.Map(mapEl, {
        center: { lat: -6.192, lng: 35.7699 },
        zoom: 6
    });

    let infoWindows = [];
    let closeOpen = () => {
        infoWindows.forEach(w => {
            w.close();
        });
    };

    fetch(url)
        .then(res => res.json())
        .then(res => {
            let json = res.data;
            json.forEach(p => {
                let name = p.name;
                let id = p.id;
                let latLng = {
                    lat: parseFloat(p.lat),
                    lng: parseFloat(p.lng)
                };

                let c_html = `<div>Main Contractor(s):<ul class="pl-3">`;
                p.contractors.forEach(c => {
                    c_html += `<li>${c}</li>`;
                });
                c_html += `</ul></div>`;

                let contentString = `
        <p class="mb-1 lead text-success">${name}</p>
        <p class="mb-1">Authority: ${p.authority}</p>
        <p class="mb-1">Quantity: ${p.qty}</p>
        ${c_html}
        <a class="btn btn-outline-secondary btn-sm" href="${p.url}">Open details</a>
        `;
                let infowindow = new google.maps.InfoWindow({
                    content: contentString
                });
                infoWindows.push(infowindow);

                let marker = new google.maps.Marker({
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
let popupWindow;
let loadDistrUrl;
let refreshOnRegion = (el, cb) => {
    document.querySelector("#btn_select_district").disabled = el.value
        ? false
        : true;
    let id = el.value | 0;
    fetch(`${window.location.origin}${loadDistrUrl}?region=${id}`)
        .then(res => {
            return res.text();
        })
        .then(function (res) {
            document.querySelector("#id_district").innerHTML = res;
            cb();
        })
        .catch(function (error) {
            console.log("Request failed", error);
        });
};
function addOtherPopupHandler(baseUrl, btn) {
    //data-toggle="modal" data-target="#mapModel"
    btn.dataset.toggle = "modal";
    btn.dataset.target = "#setup-model";
    btn.addEventListener("click", e => {
        let url = btn.dataset.url;
        url = baseUrl + url;
        if (btn.id === "btn_select_district") {
            url = `${url}?region=${document.querySelector("#id_region").value}`;
        }
        console.log(url);
        // popupCenter(url, "popUpWindow", w, h);
        fetch(url)
            .then(res => res.text())
            .then(html => {
                // console.log(html)
                let form = document.getElementById("setup-model-form");
                form.innerHTML = html;

                let btnSubmit = document.getElementById("btn-model-submit");
                btnSubmit.onclick = () => {
                    let data = new FormData(form.querySelector("form"));
                    var object = {};
                    data.forEach(function (value, key) {
                        object[key] = value;
                    });
                    var json = JSON.stringify(object);
                    console.log("Submit: ", url, json);
                    fetch(url, {
                        method: "post",
                        body: data
                    })
                        .then(res => res.text())
                        .then(text => {
                            console.log(text);
                            let regex = /closePopup\((\d+), "([\w ]+)", "(#[\w]+)"\);/g;
                            let params = [...text.matchAll(regex)];
                            let id = parseInt(params[0][1]);
                            let name = params[0][2];
                            // let elId = params[0][3];
                            let elId = btn.parentElement.querySelector(
                                ".select"
                            ).id;
                            elId = `#${elId}`;
                            console.log(id, name, elId);
                            closePopup(id, name, elId);
                        })
                        .catch(err => {
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
    btn.addEventListener("click", e => {
        let sel = e.target.parentElement.parentElement.querySelector('select')
        // console.log(sel.value)
        let url = btn.dataset.url.replace(/.$/, sel.value);
        url = baseUrl + url;
        if (btn.id === "btn_select_district") {
            url = `${url}?region=${document.querySelector("#id_region").value}`;
        }
        console.log(url);
        // popupCenter(url, "popUpWindow", w, h);
        fetch(url)
            .then(res => res.text())
            .then(html => {
                // console.log(html)
                let form = document.getElementById("setup-model-form");
                form.innerHTML = html;

                let btnSubmit = document.getElementById("btn-model-submit");
                btnSubmit.onclick = () => {
                    let data = new FormData(form.querySelector("form"));
                    var object = {};
                    data.forEach(function (value, key) {
                        object[key] = value;
                    });
                    var json = JSON.stringify(object);
                    console.log("Submit: ", url, json);
                    fetch(url, {
                        method: "POST",
                        body: data
                    })
                        .then(res => res.text())
                        .then(text => {
                            console.log(text);
                            let regex = /closePopup\((\d+), "([\w ]+)", "(#[\w]+)"\);/g;
                            let params = [...text.matchAll(regex)];
                            let id = parseInt(params[0][1]);
                            let name = params[0][2];
                            // let elId = params[0][3];
                            let elId = btn.parentElement.querySelector(
                                ".select"
                            ).id;
                            elId = `#${elId}`;
                            console.log(id, name, elId);
                            closePopup(id, name, elId);
                        })
                        .catch(err => {
                            console.log(err);
                        });
                };
            });
    });
}
let load_form_js = urls => {
    // console.log(urls)
    loadDistrUrl = urls.querySelector(".popup-setups-load-districts").value;

    (function () {
        console.log(loadDistrUrl);
        document.querySelector("#id_region").addEventListener("change", e => {
            console.log(e);
            let el = e.target;
            refreshOnRegion(el, () => {
                console.log("Loaded successfully");
            });
        });

        let w = window.innerWidth / 2;
        let h = (window.innerHeight * 3) / 5;
        let baseUrl = window.location.origin;
        let regionSel = undefined;
        [
            {
                name: "type",
                url: urls.querySelector(".popup-setups-type-create").value
            },
            {
                name: "region",
                url: urls.querySelector(".popup-setups-region-create").value
            },
            {
                name: "district",
                url: urls.querySelector(".popup-setups-district-create").value
            },
            {
                name: "authority",
                url: urls.querySelector(".popup-setups-authority-create").value
            },
            {
                name: "status",
                url: urls.querySelector(".popup-setups-status-create").value
            },
            {
                name: "size",
                url: urls.querySelector(".popup-setups-size-create").value
            }
        ].forEach(fld => {
            let name = fld.name;
            // console.log(fld, name)
            let container = document.querySelector(`#div_id_${name}`);
            if (container) {
                let sel = container.querySelector("select");
                let btn = null;
                function addBtn(name) {
                    let btn = document.createElement("button");
                    btn.innerHTML = `<i class="fa fa-plus"></i>`;
                    btn.classList.add("btn");
                    btn.classList.add("btn-link");
                    btn.classList.add("text-secondary");
                    btn.classList.add("pr-0");
                    btn.classList.add("pl-1");
                    btn.dataset.url = fld.url;
                    btn.type = "button";
                    btn.classList.add(`${name}-other`);
                    btn.title = `${name} other`;
                    if (name === "district") {
                        btn.disabled = document.querySelector("#id_region").value
                            ? false
                            : true;
                        btn.id = "btn_select_district";
                    }
                }
                // addBtn('add')
                addBtn('edit')
                sel.parentNode.insertBefore(btn, sel.nextSibling);
                sel.parentElement.classList.add("d-flex");
                if (name === "region") {
                    regionSel = sel;
                }
                if (name === "district") {
                    let tmp = sel.value;
                    refreshOnRegion(regionSel, () => {
                        sel.value = tmp;
                    });
                }
            }
        });

        let list = document.querySelectorAll(".add-other");

        for (let i = 0; i < list.length; i++) {
            let btn = list[i];
            addOtherPopupHandler(baseUrl, btn);
        }
    })();

    function popupCenter(url, title, w, h) {
        var dualScreenLeft =
            window.screenLeft != undefined ? window.screenLeft : window.screenX;
        var dualScreenTop =
            window.screenTop != undefined ? window.screenTop : window.screenY;

        var width = window.innerWidth
            ? window.innerWidth
            : document.documentElement.clientWidth
                ? document.documentElement.clientWidth
                : screen.width;
        var height = window.innerHeight
            ? window.innerHeight
            : document.documentElement.clientHeight
                ? document.documentElement.clientHeight
                : screen.height;

        var systemZoom = width / window.screen.availWidth;
        var left = (width - w) / 2 / systemZoom + dualScreenLeft;
        var top = (height - h) / 2 / systemZoom + dualScreenTop;
        top = (top * 3) / 10;
        popupWindow = window.open(
            url,
            title,
            "resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes,width=" +
            w / systemZoom +
            ", height=" +
            h / systemZoom +
            ", top=" +
            top +
            ", left=" +
            left
        );

        if (window.focus) popupWindow.focus();
    }
};

let closePopup = (newID, newRepr, id) => {
    let x = document.querySelector(id);
    console.log("Exist?", x.value, newID)
    let exists = newID == x.value
    console.log(x.value, newID)
    let option = exists ? x.options[x.selectedIndex] : document.createElement("option");
    option.text = newRepr;
    option.selected = true;
    option.value = newID;
    if (!exists) x.add(option);

    console.log("Select: ", x);
    if (x.id === "id_region") {
        refreshOnRegion(x);
    }

    console.log(newID, newRepr, id);
    // popupWindow.close();
};

let initMapOnForm = () => {
    function markerLocation() {
        var loc = marker.getPosition();
        document.querySelector("input[name=longitude]").value = loc.lng();
        document.querySelector("input[name=latitude]").value = loc.lat();
        document.querySelector(
            "#coordinates"
        ).textContent = `(${loc.lng().toFixed(4)}, ${loc.lat().toFixed(4)})`;
    }
    var map; //Will contain map object.
    var marker = false;
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -6.192, lng: 35.7699 },
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
let setLocation = (loc, err) => { };
let form_capture_GPS = () => {
    document
        .querySelector("#captureGPS")
        .addEventListener("click", function (e) {
            console.log("Capture location");
            if (navigator.geolocation) {
                console.log("GPS Supported2");
                let options = {
                    timeout: 60000, //2 minutes timeout
                    maximumAge: 180000 //3 minutes ago
                };
                navigator.geolocation.getCurrentPosition(
                    function (loc) {
                        console.log("OnLocation");
                        console.log(loc);
                        document.querySelector("input[name=longitude]").value =
                            loc.coords.longitude;
                        document.querySelector("input[name=latitude]").value =
                            loc.coords.latitude;
                        document.querySelector("#coordinates").textContent =
                            "(" +
                            loc.coords.longitude.toFixed(4) +
                            "," +
                            loc.coords.latitude.toFixed(4) +
                            ")";
                    },
                    function (err) {
                        console.log("OnError: ", err.code, err.message);
                        console.log(err);
                    },
                    options
                );
            } else {
                console.error("No GPS Capture Support!");
                alert("No GPS Capture Support!");
            }
        });
};
let handleUploadJs = () => {
    let btnImport = document.getElementById("btnImport");
    let fInput = document.getElementById("file");
    let confirmTrigger = document.getElementById("confirmTrigger");
    let confirmed = document.getElementById("confirmed");
    let file;
    fInput.addEventListener(
        "change",
        e => {
            file = e.target.files[0];
            console.log("Selected", file);
            document.getElementById("txtFile").innerHTML = file.name;
            if (file) {
                confirmTrigger.click();
            }
        },
        false
    );
    btnImport.addEventListener("click", () => {
        fInput.click();
    });
    console.log(btnImport);
    let upload = (file, url) => {
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
        fd.append(
            "csrfmiddlewaretoken",
            document.querySelector("input[name='csrfmiddlewaretoken']").value
        );
        xhr.send(fd);
    };

    confirmed.addEventListener("click", e => {
        let url = e.target.dataset.url;
        console.log("Confirmed", file, url);
        upload(file, url);
    });
};
let filter_form_rerender = () => {
    (function () {
        let getEl = (selector, prnt) => {
            return prnt.querySelector(selector);
        };
        let addCls = (el, cls) => {
            cls.split(" ").forEach(cl => {
                el.classList.add(cl);
            });
        };
        let form = document.querySelector("#filter-form");

        let inputNodes = form.querySelectorAll(".form-group");
        for (let i = 0; i < inputNodes.length; i++) {
            let grp = inputNodes[i];
            addCls(grp, "input-group input-group-sm mr-2 mt-2");
            let label = getEl("label", grp);
            let div = document.createElement("div");
            let span = document.createElement("span");
            addCls(div, "input-group-prepend");
            addCls(span, "input-group-text");
            span.textContent = label.textContent;
            grp.removeChild(label);
            div.appendChild(span);
            let inputDiv = getEl("div", grp);
            let crtr = getEl(".form-control", inputDiv);
            grp.removeChild(inputDiv);
            grp.appendChild(div);
            grp.appendChild(crtr);
        }

        let fltOnPag = document.querySelector(".filter-on-pagination");
        if (fltOnPag) {
            let selNodes = document
                .querySelector(".filter-on-pagination")
                .querySelectorAll(".select");
            for (let i = 0; i < selNodes.length; i++) {
                let sel = selNodes[i];
                sel.id = `${sel.id}_1`;
            }
            let txtNodes = document
                .querySelector(".filter-on-pagination")
                .querySelectorAll(".textinput");
            for (let i = 0; i < txtNodes.length; i++) {
                let txt = txtNodes[i];
                txt.id = `${txt.id}_1`;
            }
        }
        handleUploadJs();
    })();
};
