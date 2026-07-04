const tambahkan = document.getElementById("tambahkan");
const input_nama = document.getElementById("nama");
const input_kegiatan = document.getElementById("kegiatan");
const input_waktu = document.getElementById("waktu");
const input_submit = document.getElementById("submit");
const input_cancel = document.getElementById("cancel");
const body = document.body;
let check = true;

function renderTodo(todo) {
    let table = document.querySelector("table");
    let tr = document.createElement("tr");
    tr.style.animationName = "kanankekiri";
    tr.style.animationTimingFunction = "ease";
    tr.style.animationFillMode = "forward";
    tr.style.animationDuration = "0.5s";
    tr.id = todo.id;

    let selesaiBtn = document.createElement("button");
    selesaiBtn.textContent = "✔";
    selesaiBtn.style.borderRadius = "50%";
    selesaiBtn.addEventListener("click", () => {
        removeTodo(todo.id);
    });

    let tdNama = document.createElement("td");
    tdNama.textContent = todo.nama;

    let tdKegiatan = document.createElement("td");
    tdKegiatan.textContent = todo.kegiatan;

    let tdWaktu = document.createElement("td");
    tdWaktu.textContent = todo.waktu;

    tr.appendChild(selesaiBtn);
    tr.appendChild(tdNama);
    tr.appendChild(tdKegiatan);
    tr.appendChild(tdWaktu);

    table.appendChild(tr);
}

function removeTodo(id) {
    let todos = JSON.parse(localStorage.getItem("todos")) || [];
    todos = todos.filter(todo => todo.id !== id);
    localStorage.setItem("todos", JSON.stringify(todos));

    let tr = document.getElementById(id);
    tr.remove();
}

tambahkan.addEventListener("click", () => {
    var old_msg = document.getElementById("error-msg")
    if(old_msg) {
        old_msg.remove()
    }

    if(check === false) {
        input_nama.style.display = "none";
        input_kegiatan.style.display = "none";
        input_waktu.style.display = "none";
        input_submit.style.display = "none";
        cancel.style.display = "none";
        check = true;
    } else {
        input_nama.style.display = "block";
        input_kegiatan.style.display = "block";
        input_waktu.style.display = "block";
        input_submit.style.display = "inline";
        cancel.style.display = "inline";
        check = false;
    };
});

cancel.addEventListener("click", () => {
     var old_msg = document.getElementById("error-msg")
    if(old_msg) {
        old_msg.remove()
    }
    input_nama.style.display = "none";
    input_kegiatan.style.display = "none";
    input_waktu.style.display = "none";
    input_submit.style.display = "none";
    cancel.style.display = "none";
    check = true;
});

input_submit.addEventListener("click", () => {
    let bagian_tombol = document.getElementsByClassName("control")[0];
    let isi_nama = input_nama.value;
    let isi_kegiatan = input_kegiatan.value;
    let isi_waktu = input_waktu.value || "-"; // default jika kosong
    
    if(isi_nama === "" || isi_kegiatan === "") {
        // Hapus pesan error lama kalau ada
        var old_msg = document.getElementById("error-msg");
        if (old_msg) {
            old_msg.remove();
        }

        var p = document.createElement("p");
        p.id = "error-msg";
        p.textContent = "tolong isi nama atau kegiatan terlebih dahulu";
        p.style.color = "red";
        p.style.fontWeight = "bold";
        p.style.marginTop = "10px";
        bagian_tombol.appendChild(p);
    } else {
        var old_msg = document.getElementById("error-msg");
        if (old_msg) {
            old_msg.remove();
        }
        let todos = JSON.parse(localStorage.getItem("todos")) || [];

        let newTodo = {
            id: Date.now(), // unik
            nama: isi_nama,
            kegiatan: isi_kegiatan,
            waktu: isi_waktu
        };

        todos.push(newTodo);
        localStorage.setItem("todos", JSON.stringify(todos));

        // render ke table
        renderTodo(newTodo);

        // reset input
        input_nama.value = "";
        input_kegiatan.value = "";
        input_waktu.value = "";
    };
});

window.addEventListener("load", () => {
    let todos = JSON.parse(localStorage.getItem("todos")) || [];
    todos.forEach(todo => renderTodo(todo));
});

