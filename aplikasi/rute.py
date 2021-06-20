from aplikasi import app
from flask import render_template


#halaman awal
@app.route("/beranda", methods=["GET"])
def halaman_awal():
    return render_template("dashboard/dashboard.j2", title="Beranda")
    
#halaman galeri
@app.route("/beranda/pesan", methods=["GET"])
def galeri_awal():
    return render_template("dashboard/pesan.j2", title="Pesan") 