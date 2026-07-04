//  operasi string

// 1. char at
let data_string = "abcdef";
let data_char = data_string.charAt(0);
console.log(`character pada index ke 0 = ${data_char}`);
data_char = data_string.charAt(1);
console.log(`character pada index ke 1 = ${data_char}`);
data_char = data_string.charAt(2);
console.log(`character pada index ke 3 = ${data_char}`);
data_char = data_string.charAt(4);
console.log(`character pada index ke 4 = ${data_char}`);
data_char = data_string.charAt(5);
console.log(`character pada index ke 5 = ${data_char}`);
data_char = data_string.charAt(6);
console.log(`character pada index ke 6 = ${data_char}`); // tidak ada karakter

//  2. menyambung string
let nama_depan = "ucup";
let nama_belakang = "surucup";

let nama_lengkap = nama_depan.concat(" ", nama_belakang, 'si keren');
console.log(nama_lengkap);

// 3. mengambil indexnya
console.log(nama_lengkap.indexOf("k"));
console.log(nama_lengkap.indexOf("c")); // akan mengambil yang pertama muncul di suatu data
console.log(nama_lengkap.indexOf("u"));
console.log(nama_lengkap.indexOf("U"));

//  4. substring
console.log(nama_lengkap.substring(5,12));
let nama_lengkap_dari5_smampai_12 = nama_lengkap.substring(12,5);
console.log(nama_lengkap_dari5_smampai_12);

// 5. slice 
console.log(nama_lengkap.slice(5,12));
console.log(nama_lengkap.slice(12,5)); // menjadi kosong

// 6.replace
let nama_baru = nama_lengkap.replace("ucup surucup", "otong surotong"); 
console.log(nama_baru);
nama_lengkap = nama_lengkap.replace("ucup surucup", "otong surotong");
console.log(nama_lengkap);

// 7. to lower
console.log(nama_lengkap.toLowerCase());

// 8. to upper
console.log(nama_lengkap.toUpperCase());

// 9. extract data number
let data_string2 = "10";
console.log(typeof data_string2);
let data_integer = parseInt(data_string2);
console.log(data_integer)
console.log(typeof data_integer);

let data_string3 = "10.125"
console.log(typeof data_string2);
let data_float = parseFloat(data_string2);
console.log(data_float)
console.log(typeof data_float);