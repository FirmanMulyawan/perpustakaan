import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ==================================== Buku ==================================================


class Buku(db.Model):
    __tablename__ = 'buku'

    id_buku = db.Column(db.Integer, primary_key=True)
    nobuku = db.Column(db.Integer())
    judul_buku = db.Column(db.String())
    tahun_terbit = db.Column(db.Integer())
    pengarang = db.Column(db.String())
    

    def __init__(self, nobuku, judul_buku, tahun_terbit, pengarang):
        # self.id_buku = id_buku
        self.nobuku = nobuku
        self.judul_buku = judul_buku
        self. tahun_terbit = tahun_terbit
        self.pengarang = pengarang

    def __repr__(self):
        return '<buku id {}>'.format(self.id_buku)

    def serialize(self):
        return{
            'id_buku': self.id_buku,
            'nobuku': self.nobuku,
            'judul_buku': self.judul_buku,
            'tahun_terbit': self.tahun_terbit,
            'pengarang': self.pengarang
        }

# ============================== Peminjam ==================================================

class Peminjam(db.Model):
    __tablename__ = 'peminjam'

    peminjam_id = db.Column(db.Integer, primary_key=True)
    nama_peminjam = db.Column(db.String())
    tanggal_pinjam = db.Column(db.DateTime())
    tanggal_pengembalian = db.Column(db.DateTime())
    judul_buku = db.Column(db.String())
    nobuku = db.Column(db.Integer())

    def __init__(self, nama_peminjam, tanggal_pinjam, tanggal_pengembalian, judul_buku, nobuku):
        self.nama_peminjam = nama_peminjam
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_pengembalian = tanggal_pengembalian
        self.judul_buku = judul_buku
        self.nobuku = nobuku

    def __repr__(self):
        return '<peminjam id {}>'.format(self.peminjam_id)

    def serialize(self):
        return{
            'peminjam_id': self.peminjam_id,
            'nama_peminjam': self.nama_peminjam,
            'tanggal_pinjam': self.tanggal_pinjam,
            'tanggal_pengembalian': self.tanggal_pengembalian,
            'judul_buku': self.judul_buku,
            'nobuku': self.nobuku
        }