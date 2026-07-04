const hamburger = document.getElementById("button");
const list = document.getElementsByClassName("list");
let cek = false;

hamburger.addEventListener("click", function() {
    if(cek === false) {
        for (let i = 0; i < list.length; i++) {
            list[i].style.display = "none";
        }
        cek = true
    } else {
        for (let i = 0; i < list.length; i++) {
            list[i].style.display = "block";
        }
        cek = false;
    };
});

const body = document.body;

const cahaya = document.getElementById("cahaya");
let benar = false;

cahaya.addEventListener("click", () => {
    if(benar) {
        body.style.background = "white";
        body.style.color = "black";
        benar = false;
    } else {
        body.style.background = "black";
        body.style.color = "white";
        benar = true;
    }
});
