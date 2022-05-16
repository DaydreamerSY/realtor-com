window.onload = function () {
    load_total();
    load_visit()
};

function load_visit() {
    var xValues = ["Posts", "Visited", "Contacts", "Reported"];
    var yValues = [55, 150, 53, 4];
    var barColors = ["yellow", "green", "pink", "red"];

    new Chart("visit-chart", {
        type: "pie",
        data: {
            labels: xValues,
            datasets: [{
                backgroundColor: barColors,
                data: yValues
            }]
        },
        options: {
            legend: {display: false},
            title: {
                display: true,
                text: "Location Overview"
            }
        }
    });
}

function load_total() {
    const ctx = document.getElementById("total-chart").getContext('2d');

    var xValues = ["Posts", "Visited", "Contacts", "Reported"]
    var yValues = [2836, 1860, 2780, 150];
    var barColors = ["yellow", "green", "pink", "red"];

    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["sunday", "monday", "tuesday",
                "wednesday", "thursday", "friday", "saturday"],
            datasets: [{
                label: 'Last week',
                backgroundColor: 'rgba(161, 198, 247, 1)',
                borderColor: 'rgb(47, 128, 237)',
                data: [3000, 4000, 2000, 5000, 8000, 9000, 2000],
            },{
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                    }
                }]
            }
        },
    });
}

//
// function _prepare() {
//     navbarDropdown =
//     navbarDropdown.onmouseover = navbarDropdown.click();
// }

function print(str) {
    console.log(str);
}

// function unhideBuy() {
//     document.getElementById("homeExpand").classList.remove("hide");
//     print("unhide");
// }
//
// function hideBuy() {
//     document.getElementById("homeExpand").classList.add("hide");
//     print("hide");
// }

// $(document).ready(function(){
//     $(".drpd").hover(function(){
//         print("hovered");
//         var dropdownMenu = $(this).children(".dropdown-menu");
//         print(!dropdownMenu.is(":visible"));
//         if(!dropdownMenu.is(":visible")){
//             dropdownMenu.parent().toggleClass("open");
//             dropdownMenu.toggleClass("show");
//         }
//     });
// });

let items = document.querySelectorAll('.carousel .carousel-item')

items.forEach((el) => {
    const minPerSlide = 4
    let next = el.nextElementSibling
    for (var i = 1; i < minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
            next = items[0]
        }
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})

