const hasil = document.getElementById("hasil");
const angka_0 = document.getElementsByClassName("box_0")[0];
const angka_1 = document.getElementsByClassName("box_1")[0];
const angka_2 = document.getElementsByClassName("box_2")[0];
const angka_3 = document.getElementsByClassName("box_3")[0];
const angka_4 = document.getElementsByClassName("box_4")[0];
const angka_5 = document.getElementsByClassName("box_5")[0];
const angka_6 = document.getElementsByClassName("box_6")[0];
const angka_7 = document.getElementsByClassName("box_7")[0];
const angka_8 = document.getElementsByClassName("box_8")[0];
const angka_9 = document.getElementsByClassName("box_9")[0];
const kali = document.getElementsByClassName("kali")[0];
const tambah = document.getElementsByClassName("tambah")[0];
const kurang = document.getElementsByClassName("kurang")[0];
const pangkat = document.getElementsByClassName("pangkat")[0]; 
const sama_dengan = document.getElementsByClassName("sama_dengan")[0]; 
const bagi = document.getElementsByClassName("bagi")[0];
const hapus = document.getElementsByClassName("hapus")[0];
const hapus_Semua = document.getElementsByClassName("hapus_semua")[0];
const koma = document.getElementsByClassName("koma")[0];
const titik = document.getElementsByClassName("titik")[0];
const hasil_text = hasil;

angka_0.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 0;
});
angka_1.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 1;
});
angka_2.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 2;
});
angka_3.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 3;
});
angka_4.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 4;
});
angka_5.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 5;
});
angka_6.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 6;
});
angka_7.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 7;
});
angka_8.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 8;
});
angka_9.addEventListener("click", () => {
    hasil.textContent = hasil_text.textContent + 9;
});

koma.addEventListener("click", () => {
    if(hasil.textContent === "" || hasil.textContent === null) {
        return;
    } else {
        hasil.textContent = hasil_text.textContent + ",";
    };
});

titik.addEventListener("click", () => {
    if(hasil.textContent === "" || hasil.textContent === null) {
        return;
    } else {
        hasil.textContent = hasil_text.textContent + ".";
    };
});

kali.addEventListener("click", () => {
    if(hasil.textContent === "" || hasil.textContent === null) {
        return;
    } else {
        hasil.textContent = hasil_text.textContent + "*";
    };
});

bagi.addEventListener("click", () => {
    if(hasil.textContent === "" || hasil.textContent === null) {
        return;
    } else {
        hasil.textContent = hasil_text.textContent + "/";
    };
});

pangkat.addEventListener("click", () => {
    if(hasil.textContent === "" || hasil.textContent === null) {
        return;
    } else {
        hasil.textContent = hasil_text.textContent + "**";
    };
});

tambah.addEventListener("click", () => {
    if(hasil.textContent === "" || hasil.textContent === null) {
        return;
    } else {
        hasil.textContent = hasil_text.textContent + "+";
    };
});

kurang.addEventListener("click", () => {
    if(hasil.textContent === "" || hasil.textContent === null) {
        return;
    } else {
        hasil.textContent = hasil_text.textContent + "-";
    };
});

hapus_Semua.addEventListener("click", () => {
    hasil.textContent = ""
});

hapus.addEventListener("click", () => {
    hasil.textContent = hasil.textContent.slice(0, -1);
});

sama_dengan.addEventListener("click", () => {
    let hasil_arimatika = eval(hasil.textContent);
    hasil.textContent = hasil_arimatika
})

/*
 fungsi slice(0,-1) = 0 → mulai dari index 0

-1 → potong 1 karakter terakhir

Jadi waktu di kalkulator kamu pencet tombol ← (hapus/backspace), slice(0, -1) ngapus karakter terakhir dari input. 

fungsi eval() = Kalau tanpa eval(), "2+3*4" cuma teks. Tapi eval() ngubahnya jadi perhitungan beneran.
⚠️ Hati-hati kalau di dunia nyata, karena eval() bisa bahaya kalau dipakai di input user (orang bisa masukin kode aneh). Tapi untuk latihan kalkulator, aman-aman aja.

disclaimer: bisa menggunakan ini atau menggunakan loop lain kali supaya hasil bisa dibaca secara manusiawi dan dapat dibaca semua orang

const angka = document.querySelectorAll(".box_0, .box_1, .box_2, .box_3, .box_4, .box_5, .box_6, .box_7, .box_8, .box_9");
angka.forEach(btn => {
    btn.addEventListener("click", () => {
        hasil.textContent += btn.textContent;
    });
});

quaryselectorall itu mengambil semua class yang disebutkan, contohnya seperti tadi biar gak ngulang, ini contohnya

const angka = document.querySelectorAll(".box_0, .box_1, .box_2, .box_3, .box_4, .box_5, .box_6, .box_7, .box_8, .box_9");

*/

// brightness

const brightness = document.getElementsByClassName("brightness")[0];
const img = document.getElementById("bright");
let bright = false;
const root = document.documentElement;

function setdarkmode() {
    root.style.setProperty("--first-color", "#1a1a1b");
    root.style.setProperty("--second-color", "#2563EB");
    root.style.setProperty("--third-color", "#212423");
    root.style.setProperty("--fourth-color", "#F59E0B");
    root.style.setProperty("--fifth-color", "#EF4444");
    root.style.setProperty("--gray-color", "#747070");
    root.style.setProperty("--another-calc-color", "#23222b");
    root.style.setProperty("--border-color-calc", "#a59da1");
    root.style.setProperty("--big-box-color", "#000000");
    root.style.setProperty("--white-color", "aliceblue");
    root.style.setProperty("--brightness-color", "#bbc2bb");
}

function setlightmode() {
    root.style.setProperty("--first-color", "#f9f9f9");
    root.style.setProperty("--second-color", "#2563EB");
    root.style.setProperty("--third-color", "#ffffff");
    root.style.setProperty("--fourth-color", "#F59E0B");
    root.style.setProperty("--fifth-color", "#ff88caff");
    root.style.setProperty("--gray-color", "#555555");
    root.style.setProperty("--another-calc-color", "#e5e7eb");
    root.style.setProperty("--border-color-calc", "#cbd5e1");
    root.style.setProperty("--big-box-color", "#ffffff");
    root.style.setProperty("--white-color", "#000000");
    root.style.setProperty("--brightness-color", "#f3f4f6");
}

brightness.addEventListener("click", () => {
    if(bright === false) {
        img.src = "img/brightness-high.svg"
        setdarkmode()
        bright = true;
    } else {
        img.src = "img/brightness-high-fill.svg"
        setlightmode()
        bright = false;
    };
});

/* 
Evaluasi dari project ini

📝 Catatan Project Kalkulator + Dark/Light Mode
1. Struktur Project

HTML:

Elemen p untuk menampilkan hasil (id="hasil").

Tombol angka 0–9, operator (+, -, *, /, **), titik, koma.

Tombol khusus: hapus satu (C), hapus semua (CA), sama dengan (=).

Tombol brightness untuk toggle dark/light mode dengan icon.

CSS:

Warna-warna didefinisikan pakai --variabel di :root.

Bisa diubah lewat JS dengan root.style.setProperty("--nama-var", "value").

JS:

Ambil semua elemen dengan getElementById atau getElementsByClassName.

Event listener untuk setiap tombol (angka/operator).

Logic kalkulasi pakai eval().

Tombol hapus → slice(0, -1) untuk menghapus karakter terakhir.

Tombol brightness → toggle dark/light mode + ganti icon.

2. Fitur Utama

✔️ Input angka & operator.
✔️ Perhitungan otomatis dengan tombol =.
✔️ Fungsi hapus 1 huruf terakhir dan hapus semua.
✔️ Bisa pakai pangkat (**).
✔️ Dark mode & light mode toggle.
✔️ Icon brightness ikut berubah.

3. Kesalahan yang Sempat Muncul

Salah id / class → bikin event listener gak jalan.

getElementById("bright") dipakai salah (seharusnya untuk img, tapi button juga perlu id/selector yang bener).

Typo kecil di setProperty atau variabel warna.

Copy-paste event listener angka terlalu panjang → bisa dipendekin pakai querySelectorAll + forEach.

4. Hal Penting Dipelajari

DOM Manipulation:

document.getElementById() → ambil 1 elemen.

document.getElementsByClassName()[0] → ambil elemen pertama dari HTMLCollection.

document.querySelectorAll() + .forEach() → ambil banyak elemen sekaligus dan kasih event listener bareng-bareng.

String Manipulation:

.slice(0, -1) → hapus karakter terakhir.

Eval:

Ubah string jadi operasi matematika beneran.

⚠️ Aman untuk latihan, tapi bahaya di aplikasi nyata kalau input bisa di-hack user.

Toggle Mode:

Pakai variabel CSS global (--warna) biar gampang diubah lewat JS.

Simpel, fleksibel, dan gak perlu bikin CSS file terpisah.

5. Next Level Improvement

Gunakan loop + querySelectorAll untuk tombol angka/operasi biar gak panjang banget.

Tambahkan validasi biar gak bisa input operator dua kali berturut-turut (++, --, dll).

Simpan mode terakhir (dark/light) ke localStorage, jadi kalau reload tetap sama.

Styling lebih modern (misal shadow, hover, animasi klik).
*/