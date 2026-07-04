const tempat_mata = document.getElementById("tempat_mata");
let cek = true;

// tempat_mata.addEventListener("click", () => {
//     let mata = document.getElementById("gambar_mata");
//     let pass = document.getElementById("password");

//     if(cek === true) {
//         mata.src = "image/eye.svg";
//         pass.type = "text";
//         cek = false;
//     }else {
//         mata.src = "image/eye-fill.svg";
//         pass.type = "password";
//         cek = true;
//     };
// });


tempat_mata.addEventListener("mousedown", () => {
    let mata = document.getElementById("gambar_mata");
    let pass = document.getElementById("password");

    pass.type = "text"; // password keliatan
    mata.src = "image/eye.svg"; // mata kebuka
});

tempat_mata.addEventListener("mouseup", () => {
    let mata = document.getElementById("gambar_mata");
    let pass = document.getElementById("password");

    pass.type = "password"; // password ketutup lagi
    mata.src = "image/eye-fill.svg"; // mata ketutup
});

// biar aman juga kalau mouse keluar dari tombol
tempat_mata.addEventListener("mouseleave", () => {
    let mata = document.getElementById("gambar_mata");
    let pass = document.getElementById("password");

    pass.type = "password";
    mata.src = "image/eye-fill.svg";
});