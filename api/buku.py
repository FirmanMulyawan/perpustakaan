from flask import Flask, jsonify, request
from app import app, db
from model import Buku
# from utils import generateToken


@app.route('/buku')
def tesUser():
    return 'tes koneksi buku'
# ================================== ADD Buku ==================================


@app.route('/addBuku', methods=["POST"])
def add_buku():

    body = request.json
    # id_buku = body['id_buku']
    nobuku = body['nobuku']
    judul_buku = body['judul_buku']
    tahun_terbit = body['tahun_terbit']
    pengarang = body['pengarang']

    try:
        buku = Buku(
            # id_buku=id_buku,
            nobuku=nobuku,
            judul_buku=judul_buku,
            tahun_terbit=tahun_terbit,
            pengarang=pengarang
        )

        db.session.add(buku)
        db.session.commit()
        return "add buku. buku id={}".format(buku.id_buku), 200

    except Exception as e:
        return(str(e)), 400

# ========================== GET ALL Buku =============================================
@app.route('/getAllBuku', methods=["GET"])
def get_all_Buku():
    try:
        buku = Buku.query.order_by(Buku.id_buku).all()
        return jsonify([usr.serialize()
                        for usr in buku])
    except Exception as e:
        return (str(e))

# ============================= GET Buku BY ID ==========================================
@app.route('/getBukuBy/<BukuId_>', methods=["GET"])
def get_Buku_by(BukuId_):
    try:
        buku = Buku.query.filter_by(id_buku=BukuId_).first()
        return jsonify(buku.serialize())
    except Exception as e:
        return (str(e))
