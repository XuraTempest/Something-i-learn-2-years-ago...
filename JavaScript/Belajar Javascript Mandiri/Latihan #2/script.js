let aritmatika_angka_1,operator_aritmarika,aritmatika_angka_2,hasil_operator_aritmatika;

document.getElementById("button_aritmatika").onclick = function(){
    aritmatika_angka_1 = document.getElementById("aritmatika_angka_1").value;
    aritmatika_angka_2 = document.getElementById("aritmatika_angka_2").valueAsNumber;
    operator_aritmarika = document.getElementById("operator_aritmatika").value;

    /* bisa menggunakan seperti ini dari apda menggunakan eval karena sangat rentan dan berbahaya mengenai bug
        if (operator === "+") {
        hasil = angka1 + angka2;
    } else if (operator === "-") {
        hasil = angka1 - angka2;
    } else if (operator === "*") {
        hasil = angka1 * angka2;
    } else if (operator === "/") {
        hasil = angka1 / angka2;
    } else if (operator === "%") {
        hasil = angka1 % angka2;
    } else {
        hasil = "Operator tidak valid";
    }
    */ 

    // operasi
    hasil_operator_aritmatika = eval(aritmatika_angka_1 + operator_aritmarika + aritmatika_angka_2);
    
    // output
    document.getElementById("hasil_operator_aritmatika").textContent =  hasil_operator_aritmatika
};

let aritmatika_boolean_1,operator_logika,aritmatika_boolean_2,hasil_operator_logika;

document.getElementById("button_boolean").onclick = function(){
    aritmatika_boolean_1 = document.getElementById("aritmatika_boolean_1").value === "true";
    aritmatika_boolean_2 = document.getElementById("aritmatika_boolean_2").value === "true";
    operator_logika = document.getElementById("operator_logika").value;

    // Operasi
    if (operator_logika === "&&") {
        hasil_operator_logika = aritmatika_boolean_1 && aritmatika_boolean_2;
    } else if (operator_logika === "||") {
        hasil_operator_logika = aritmatika_boolean_1 || aritmatika_boolean_2;
    } 
    else {
        hasil_operator_logika = "Operator tidak valid";
    }

    // output
    document.getElementById("hasil_operator_logika").textContent =  hasil_operator_logika
};