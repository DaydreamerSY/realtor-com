// window.onload = _prepare();
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
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})

