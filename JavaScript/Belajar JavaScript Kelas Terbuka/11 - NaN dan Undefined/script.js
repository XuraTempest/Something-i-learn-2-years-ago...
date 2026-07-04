// NaN dan Undefined

// NaN = Not a Number
console.log(`akar dari -1 ${Math.sqrt(-1)}`)
console.log(`"ucup / otong" :${"ucup" / "otong"}`)
console.log(`"ucup X otong" :${"ucup" * "otong"}`)
console.log(`"ucup - otong" :${"ucup" - "otong"}`) // kecuali tambha, malah jadi nempel

let data = parseInt("test123");
console.log(data); //mau ada operasi tambah, kurang, atau pun operasi apapun, maka akan menjadi tetap NaN

// undefined = dia belum tau nilai nya
let a;
console.log(`a = ${a}`);
console.log(Math.sqrt(4));
console.log(console.log("text")); // console.log tidak menghasilkan apapun, maka semua data yang tidak menghasilkan apapun, menjadi undefined

//contoh

let d = console.log("otong");
console.log(typeof(d))

// perbedaan NaN dan Undefined
// NaN adalah semua operasi yang berhubungan dengan data, tetapi tidak menghasilkan sesuatu yang ada tapi tidak jelas hasilnya.
// undefined adalah data yang terbentuk karena suatu fungsi atau suatu method yang menghasilkan data berbentuk tidak ada atau hasilnya tidak jelas dari method tertentu, lalu undefined juga dapat dibuat dengan mengosongkan variabel