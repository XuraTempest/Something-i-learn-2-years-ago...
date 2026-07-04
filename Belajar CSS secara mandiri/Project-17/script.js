const user = document.getElementById("username");
const pass = document.getElementById("password");
const btn = document.getElementById("loginBtn");
const pesan = document.getElementById("pesan");

btn.addEventListener("click", () => {
    if (user.value === "" || pass.value === "") {
        alert("Isi dulu username & password!");
    } else {
        pesan.textContent = `Selamat datang, ${user.value}! 🎉`;
    }
});

// biar bisa login pake Enter juga
document.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        btn.click(); // jalankan tombol login
    }
});