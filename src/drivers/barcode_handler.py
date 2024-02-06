from barcode import Code128
from barcode.writer import ImageWriter

class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code , writer=ImageWriter())
        path_form_tag = f'{tag}'
        tag.save(path_form_tag)

        return path_form_tag 