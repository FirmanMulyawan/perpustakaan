function buku() {
    var nobuku = document.getElementById('nobuku').value
    var judul_buku = document.getElementById('judul_buku').value
    var tahun_terbit = document.getElementById('tahun_terbit').value
    var pengarang = document.getElementById('pengarang').value
    

    console.log(nobuku);
    console.log(judul_buku);
    console.log(tahun_terbit);
    console.log(pengarang)

    $.ajax({
        url: 'http://127.0.0.1:6750/addBuku',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            nobuku: nobuku,
            judul_buku: judul_buku,
            tahun_terbit: tahun_terbit,
            pengarang: pengarang
        }),
        success: function () {
            alert("anda berhasil menambahkan buku")
            window.location.href = 'index.html'
        },
        error: function () {
            alert("silahkan coba lagi")
            window.location.href = 'buku.html'
        }
    })
}