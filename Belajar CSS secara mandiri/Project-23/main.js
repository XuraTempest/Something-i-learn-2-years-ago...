let happy, netral, sad, kotak_1, kotak_2, kotak_3;

happy = document.getElementById("happy");
netral = document.getElementById("netral");
sad = document.getElementById("sad");
kotak_1 = localStorage.getItem("kotak_1");
kotak_2 = localStorage.getItem("kotak_2");
kotak_3 = localStorage.getItem("kotak_3");

if (kotak_1 === null) {
    kotak_1 = true;
} else {
    kotak_1 = JSON.parse(kotak_1);
}

if(kotak_1 === true) {
    happy.textContent = "Aku Lagi Seneng Nih";
} else {
    happy.textContent = "Mantap";
}


happy.addEventListener("click", () => {
    kotak_1 = localStorage.getItem("kotak_1");
    if (kotak_1 === null) {
    kotak_1 = true;
    } else {
    kotak_1 = JSON.parse(kotak_1);
    }

    if(kotak_1 === true) {
        happy.textContent = "Mantap";
        kotak_1 = false;
    } else {
        happy.textContent = "Aku Lagi Seneng Nih";
        kotak_1 = true;
    }
    localStorage.setItem("kotak_1", kotak_1)
})


if (kotak_2 === null) {
    kotak_2 = true;
} else {
    kotak_2 = JSON.parse(kotak_2);
}

if(kotak_2 === true) {
    netral.textContent = "Aku Lagi Biasa Aja Sih";
} else {
    netral.textContent = "Diem";
}


netral.addEventListener("click", () => {
    kotak_2 = localStorage.getItem("kotak_2");
    if (kotak_2 === null) {
    kotak_2 = true;
    } else {
    kotak_2 = JSON.parse(kotak_2);
    }

    if(kotak_2 === true) {
        netral.textContent = "Diem";
        kotak_2 = false;
    } else {
        netral.textContent = "Aku Lagi Biasa Aja Sih";
        kotak_2 = true;
    }
    localStorage.setItem("kotak_2", kotak_2)
})


if (kotak_3 === null) {
    kotak_3 = true;
} else {
    kotak_3 = JSON.parse(kotak_3);
}

if(kotak_3 === true) {
    sad.textContent = "Aku Lagi Sedih Nih";
} else {
    sad.textContent = "Mau Coding Tapi Pusing";
}


sad.addEventListener("click", () => {
    kotak_3 = localStorage.getItem("kotak_3");
    if (kotak_3 === null) {
    kotak_3 = true;
    } else {
    kotak_3 = JSON.parse(kotak_3);
    }

    if(kotak_3 === true) {
        sad.textContent = "Mau Coding Tapi Pusing";
        kotak_3 = false;
    } else {
        sad.textContent = "Aku Lagi Sedih Nih";
        kotak_3 = true;
    }
    localStorage.setItem("kotak_3", kotak_3)
})