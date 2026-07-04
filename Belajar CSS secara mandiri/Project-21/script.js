let happy, neutral, sad, kotak_1, kotak_2, kotak_3;

happy = document.getElementById("happy");
neutral = document.getElementsByClassName("neutral")[0];
sad = document.getElementById("sad");

function textboxt(kotak, nama_1, nama_2) {
    kotak.addEventListener("click", () => {
        if(kotak.textContent === nama_1) {
            kotak.textContent = nama_2;
        } else {
            kotak.textContent = nama_1;
        };
        localStorage.setItem(kotak.textContent)
    })
};

textboxt(happy, "Mantap", "Aku lagi seneng nih")
textboxt(neutral, "Aku lagi biasa aja sih", "Gak kenapa kenapa")
textboxt(sad, "Males coding tapi pengen", "Aku lagi sedih nih bro")

// happy.addEventListener("click", () => {
//     if(kotak_1 === true) {
//         happy.textContent = "Mantap";
//         kotak_1 = false;
//     } else {
//         happy.textContent = "Aku lagi senang nih";
//         kotak_1 = true;
//     };
// });

// neutral.addEventListener("click", function name() {
//     if(kotak_2 === true) {
//         neutral.textContent = "Gk kenapa kenapa";
//         kotak_2 = false;
//     } else {
//         neutral.textContent = "Aku lagi biasa aja sih";
//         kotak_2 = true;
//     }
// });

// sad.addEventListener("click", () => {
//     if(kotak_3 === true) {
//         sad.textContent = "Males coding tapi pengen";
//         kotak_3 = false;
//     } else {
//         sad.textContent = "Aku lagi sedih nih bro";
//         kotak_3 = true;
//     }
// });