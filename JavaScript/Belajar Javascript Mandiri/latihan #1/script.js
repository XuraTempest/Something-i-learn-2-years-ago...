let angka_1,angka_2,hasil;

document.getElementById("button_jumlah").onclick = function(){
    angka_1 = document.getElementById("angka_1").valueAsNumber;
    angka_2 = document.getElementById("angka_2").valueAsNumber;
    hasil = angka_1 + angka_2;

    document.getElementById("hasil").textContent = hasil;
}

document.getElementById("button_kurang").onclick = function(){
    angka_1 = document.getElementById("angka_1").valueAsNumber;
    angka_2 = document.getElementById("angka_2").valueAsNumber;
    hasil = angka_1 - angka_2;

    document.getElementById("hasil").textContent = hasil;
}

document.getElementById("button_kali").onclick = function(){
    angka_1 = document.getElementById("angka_1").valueAsNumber;
    angka_2 = document.getElementById("angka_2").valueAsNumber;
    hasil = angka_1 * angka_2;

    document.getElementById("hasil").textContent = hasil;
}

document.getElementById("button_bagi").onclick = function(){
    angka_1 = document.getElementById("angka_1").valueAsNumber;
    angka_2 = document.getElementById("angka_2").valueAsNumber;
    hasil = angka_1 / angka_2;

    document.getElementById("hasil").textContent = hasil;
}