const btn = document.getElementById('themeBtn');
    let isDefault = true;

    btn.addEventListener('click', () => {
    if(isDefault) {
        document.documentElement.style.setProperty('--main-color', '#2ecc71'); // hijau
        document.documentElement.style.setProperty('--secondary-color', '#f1c40f'); // kuning
        document.documentElement.style.setProperty('--padding', '30px');
    } else {
        document.documentElement.style.setProperty('--main-color', '#3498db'); // biru
        document.documentElement.style.setProperty('--secondary-color', '#e74c3c'); // merah
        document.documentElement.style.setProperty('--padding', '20px');
    }
    isDefault = !isDefault;
    });