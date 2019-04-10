from flask import Flask, jsonify, request
from app import app, db
from model import Peminjam


@app.route('/peminjam')
def tesPeminjam():
    return 'tes koneksi Peminjam'

# ============================================ ADD Peminjam ==============================
@app.route('/addPeminjam', methods=["POST"])
def add_peminjam():

    body = request.json
    # id_buku = body['id_buku']
    nama_peminjam = body['nama_peminjam']
    tanggal_pinjam = body['tanggal_pinjam']
    tanggal_pengembalian = body['tanggal_pengembalian']
    judul_buku = body['judul_buku']
    nobuku = body['nobuku'] 

    try:
        peminjam = Peminjam(
            # id_buku=id_buku,
            nama_peminjam=nama_peminjam,
            tanggal_pinjam=tanggal_pinjam,
            tanggal_pengembalian=tanggal_pengembalian,
            judul_buku=judul_buku,
            nobuku=nobuku
        )

        db.session.add(peminjam)
        db.session.commit()
        return "add peminjam. peminjam id={}".format(peminjam.peminjam_id), 200

    except Exception as e:
        return(str(e)), 400
# # ========================================== GET ALL Peminjam ================================
@app.route('/getAllPeminjam', methods=["GET"])
def get_all_peminjam():
        try:
                peminjam = Peminjam.query.order_by(Peminjam.peminjam_id).all()
                return jsonify([usr.serialize()
                                for usr in peminjam])
        except Exception as e:
                return (str(e))

# # ============================================ GET Peminjam BY =====================================
@app.route('/getPeminjamBy/<peminjamId_>', methods=["GET"])
def get_Peminjam_by(peminjamId_):
        try:
                peminjam = Peminjam.query.filter_by(peminjam_id=peminjamId_).first()
                return jsonify(peminjam.serialize())
        except Exception as e:
                return (str(e))

# # =============================================== UPDATE ITEM =====================================
# @app.route('/updateItem/<itemId_>', methods=["PUT"])
# def update_item(itemId_):

#         body = request.json
#         item_existing = get_item_by(itemId_).json

#         if 'item_type' not in body:
#                 item_type = item_existing['item_type']
#         else:
#                 item_type = body['item_type']
#         if 'material' not in body:
#                 material = item_existing['material']
#         else:
#                 material = body['material']
#         if 'description' not in body:
#                 description = item_existing['description']
#         else:
#                 description = body['description']
#         if 'storage_location' not in body:
#                 storage_location = item_existing['storage_location']
#         else:
#                 storage_location = body['storage_location']
#         if 'quantity' not in body:
#                 quantity = item_existing['quantity']
#         else:
#                 quantity = body['quantity']
#         if 'price_each' not in body:
#                 price_each = item_existing['price_each']
#         else:
#                 price_each = body['price_each']
#         if 'budget_source' not in body:
#                 budget_source = item_existing['budget_source']
#         else:
#                 budget_source = body['budget_source']
#         if 'note' not in body:
#                 note = item_existing['note']
#         else:
#                 note = body['note']
#         try:
#                 itemUpdate = {
#                     'item_type': item_type,
#                     'material': material,
#                     'description': description,
#                     'storage_location': storage_location,
#                     'quantity': quantity,
#                     'price_each': price_each,
#                     'budget_source': budget_source,
#                     'note': note,


#                 }
#                 item = Item.query.filter_by(item_id=itemId_).update(itemUpdate)
#                 db.session.commit()
#                 return 'update item'
#         except Exception as e:
#                 return(str(e))