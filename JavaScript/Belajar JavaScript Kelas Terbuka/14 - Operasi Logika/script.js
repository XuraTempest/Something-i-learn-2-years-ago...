// Operator Logika

// and, or, not

let data_bool = true;
console.log(data_bool);

// 1. not (kebalikan)
console.log(!data_bool); // memutar atau flip data bool
console.log(!!data_bool);
console.log(!1);
console.log(!0);

let is_keren = true;
let is_jelek = !is_keren;

// 2. or (Operasi antara 2 variabe; boolean)
// A     true true  false false
// B     true false true  false
// Hasil true true  true  false

console.log(`true OR true, Hasil = ${true || true}`);
console.log(`true OR false, Hasil = ${true || false}`);
console.log(`false OR true, Hasil = ${false || true}`);
console.log(`false OR false, Hasil = ${false || false}`);

let makan = true;
let minum = true;

let sudah_menyantap = makan || minum;
console.log(`sudah menyantap = ${sudah_menyantap}`)

// 3. And -> && (poperasi antara 2 variabel boolean)
// A     true true  false false
// B     true false true  false
// Hasil true false false false

console.log(`true OR true, Hasil = ${true && true}`);
console.log(`true OR false, Hasil = ${true && false}`);
console.log(`false OR true, Hasil = ${false && true}`);
console.log(`false OR false, Hasil = ${false && false}`);

makan = true;
minum = false;

sudah_menyantap = makan && minum;
console.log(`sudah menyantap = ${sudah_menyantap}`)