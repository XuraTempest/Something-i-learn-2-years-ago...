// numbers - 64-bit 2^1024 - 2^1024

let nilai_int = 10; // interger (nilai bulat)
let nilai_float = 10.123; // float (nilai bilangan desimal)
let nilai_big_int = 1231231244124123124741271724n; // big integer

console.log(typeof nilai);
console.log(typeof nilai_float);
console.log(typeof nilai_big_int);

//  menggunakan tipe data ini

let angka = 5.678;

let angka_int = parseInt(angka);
console.log(angka_int);

let angka_2 = 10.98;
let angka_2_float = parseFloat(angka_2);
console.log(angka_2);
console.log(angka_2_float);

// merubah string

let data = "10.98 ada apa dengan ucup?";
console.log(data);
console.log(parseInt(data)+10); // harus di parcing dulu, tidak bis langsung dengan float
console.log(parseFloat(data));

// note, jika angka nya berada di belakang maka akan menjadi Nan daripada sebuah tipe data numbers

let data_1 = "ada apa dengan ucup? 10.98"; // menjadi Nan
console.log(data_1);
console.log(parseInt(data_1)+10); // harus di parcing dulu, tidak bis langsung dengan float
console.log(parseFloat(data_1));

// contoh

let pembelian = "10000";
let pajak = 0.12;
let bayar = parseInt(pembelian) + parsefloat(pembelian) * pajak // harus di parse dulu, jika tidak, datanya akan nyambung