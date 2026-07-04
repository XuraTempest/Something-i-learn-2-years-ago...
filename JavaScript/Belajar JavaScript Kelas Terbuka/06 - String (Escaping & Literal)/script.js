let data_string = "data string";
console.log(data_string);

// 1. escaping string (\" \' \\ \n \r \t \b \f)
let data1 = "ucup berkata 'apa kabar dunia?'";
console.log(data1);
let data2 = "otong berkata \"tetap mantap\"";
console.log(data2);
let data3 = "ucup berjalan-jalan di tepi pantai, \nkeren";
console.log(data3);

// 2. literal string (template literal string)
let nama_depan = "otong";
let nama_belakang = "surotong";
let umur = 7
let nama_lengkap = umur + " " + nama_depan + " " + nama_belakang; //bikin masalah
console.log(nama_lengkap);
console.log(typeof nama_lengkap);

// lebih elehan supaya ini tidak bikin error
let biodata = `${nama_depan} ${nama_belakang} dengan umur ${umur}`;
console.log(biodata)