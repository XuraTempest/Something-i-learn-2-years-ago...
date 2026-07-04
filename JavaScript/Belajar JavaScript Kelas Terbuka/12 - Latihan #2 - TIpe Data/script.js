let angka_1,angka_2,hasil;

document.getElementById("button_jumlah").onclick = function(){
    angka_1 = document.getElementById("angka_1").value // tipe dari data yang di ambil di web adalah berjenis string jadi berhati hatilah, dan di ubah ke number terlebih dahulu
    angka_2 = document.getElementById("angka_2").valueAsNumber
    hasil = parseFloat(angka_1) + angka_2

    console.log(`hasil = ${hasil} tipe=${typeof hasil}`)

    document.getElementById("hasil").textContent = hasil
    
}