
# import barcode
# from barcode.writer import ImageWriter
# ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
# ean.save('21011003')

# import barcode
# from barcode.writer import ImageWriter
# ean = barcode.get('ean13', '2110311112341', writer=ImageWriter())
# filename = ean.save('2110311112341')

import barcode
from barcode.writer import ImageWriter
ean = barcode.get('code39', '21103111123412', writer=ImageWriter())
filename = ean.save('21103111123412')