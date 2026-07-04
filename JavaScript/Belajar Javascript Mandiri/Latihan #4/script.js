let random_easy,random_normal,random_hard,user_easy,user_normal,user_hard,hasil_easy,hasil_normal,hasil_hard;
let nyawa_easy,nyawa_normal,nyawa_hard;

document.getElementById("button_easy").onclick = function() {
    random_easy = Math.floor((Math.random()) * 5) + 1;
    user_easy = document.getElementById("easy").valueAsNumber;
    
    if (nyawa_easy === 0) {
        document.getElementById("hasil_easy").innerText = "GAME OVER";
        return;
    }

    if (isNaN(nyawa_easy) || nyawa_easy === undefined) {
        document.getElementById("hasil_easy").innerText = "Submit dulu nyawanya";
        return;
    }

    if (nyawa_easy === -1) {
        document.getElementById("hasil_easy").innerText = "Isi nyawa karena kamu menekan reset button";
        return;
    }

    if (isNaN(user_easy)) {
        document.getElementById("hasil_easy").innerText = "Isi dulu angkanya!";
        return;
    }

    if (user_easy < 1 || user_easy > 5) {
        document.getElementById("hasil_easy").innerText = "Angka harus antara 1 sampai 5!";
        return;
    }

    if (user_easy === random_easy) {
        document.getElementById("hasil_easy").innerText = "Kamu Benar! Jawabannya adalah " + random_easy + ". Nyawa sisa: " + nyawa_easy;
        nyawa_easy = 0;
    } else {
        nyawa_easy -= 1;
        document.getElementById("hasil_easy").innerText = "Salah! Jawabannya adalah " + random_easy + ". Nyawa sisa: " + nyawa_easy;
    }

};

document.getElementById("total_nyawa_easy").onclick = function() {
    nyawa_easy = document.getElementById("nyawa_easy").valueAsNumber;
}

document.getElementById("reset_button_easy").onclick = function(){
    nyawa_easy = -1
}





document.getElementById("button_normal").onclick = function() {
    random_normal = Math.floor((Math.random()) * 10) + 1;
    user_normal = document.getElementById("normal").valueAsNumber;
    
    if (nyawa_normal === 0) {
        document.getElementById("hasil_normal").innerText = "GAME OVER";
        return;
    }

    if (isNaN(nyawa_normal) || nyawa_normal === undefined) {
        document.getElementById("hasil_normal").innerText = "Submit dulu nyawanya";
        return;
    }

    if (nyawa_normal === -1) {
        document.getElementById("hasil_normal").innerText = "Isi nyawa karena kamu menekan reset button";
        return;
    }

    if (isNaN(user_normal)) {
        document.getElementById("hasil_normal").innerText = "Isi dulu angkanya!";
        return;
    }

    if (user_normal < 1 || user_normal > 10) {
        document.getElementById("hasil_normal").innerText = "Angka harus antara 1 sampai 10!";
        return;
    }

    if (user_normal === random_normal) {
        document.getElementById("hasil_normal").innerText = "Kamu Benar! Jawabannya adalah " + random_normal + ". Nyawa sisa: " + nyawa_normal;
        nyawa_normal = 0;
    } else {
        nyawa_normal -= 1;
        document.getElementById("hasil_normal").innerText = "Salah! Jawabannya adalah " + random_normal + ". Nyawa sisa: " + nyawa_normal;
    }
};


document.getElementById("total_nyawa_normal").onclick = function() {
    nyawa_normal = document.getElementById("nyawa_normal").valueAsNumber;
}

document.getElementById("reset_button_normal").onclick = function(){
    nyawa_normal = -1
}






document.getElementById("button_hard").onclick = function() {
    random_hard = Math.floor((Math.random()) * 20) + 1;
    user_hard = document.getElementById("hard").valueAsNumber;
    
    if (nyawa_hard === 0) {
        document.getElementById("hasil_hard").innerText = "GAME OVER";
        return;
    }

    if (isNaN(nyawa_hard) || nyawa_hard === undefined) {
        document.getElementById("hasil_hard").innerText = "Submit dulu nyawanya";
        return;
    }

    if (nyawa_hard === -1) {
        document.getElementById("hasil_hard").innerText = "Isi nyawa karena kamu menekan reset button";
        return;
    }

    if (isNaN(user_hard)) {
        document.getElementById("hasil_hard").innerText = "Isi dulu angkanya!";
        return;
    }

    if (user_hard < 1 || user_hard > 20) {
        document.getElementById("hasil_hard").innerText = "Angka harus antara 1 sampai 20!";
        return;
    }

    if (user_hard === random_hard) {
        document.getElementById("hasil_hard").innerText = "Kamu Benar! Jawabannya adalah " + random_hard + ". Nyawa sisa: " + nyawa_hard;
        nyawa_hard = 0;
    } else {
        nyawa_hard -= 1;
        document.getElementById("hasil_hard").innerText = "Salah! Jawabannya adalah " + random_hard + ". Nyawa sisa: " + nyawa_hard;
    }
};


document.getElementById("total_nyawa_hard").onclick = function() {
    nyawa_hard = document.getElementById("nyawa_hard").valueAsNumber;
}

document.getElementById("reset_button_hard").onclick = function(){
    nyawa_hard = -1
}
