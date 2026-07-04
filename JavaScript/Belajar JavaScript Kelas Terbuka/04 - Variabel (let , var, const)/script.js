// ini adalah command

// variabel dengan lett
let nama = "Ucup surucup";

// tampilkan data
console.log(nama);

// kita ubah nilai variabel nama
nama = "Otong Surotong";
console.log(nama);

// 2. Variabel dengan var
var nama_depan = "ucup";
console.log(nama_depan);
nama_depan = "Otong";
console.log(nama_depan);

// Kelakuan dari let
let nama_belakang = "Surucup";
{
    let nama_belakang = "surotong";
    console.log(nama_belakang);
}
console.log(nama_belakang);

// Kelakuan dari var
var nama_tengah = "keren";
{
    var nama_tengah = "ganteng";
    console.log(nama_tengah);
}
console.log(nama_tengah);

// kasus khusus tanpa keyword akan tetap jadi var
gorengan = "bala-bala";
console.log(gorengan);
{
    gorengan = "combro";
}
console.log(gorengan);

// 3.const

const TTL = "10 Maret 2022";
console.log(TTL);
// TTL = "11 Maret 2054" gak boleh dilakukan karena ini var const dan sudah janji XD