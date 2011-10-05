import os, sys, sqlite3
from mod_python import apache

mbtiles = os.path.join(os.path.dirname(__file__), 'osm.mbtiles')

def index(req, x, y, z):
  req.content_type = 'image/png'
  conn = sqlite3.connect(mbtiles)
  c = conn.cursor()
  c.execute('select tile_data \
    from tiles \
    where zoom_level=? \
      and tile_column=? \
      and tile_row=?', (z, x, y))
  res = c.fetchone()
  if res:
    return res[0]
  else:
    req.status = apache.HTTP_NOT_FOUND

