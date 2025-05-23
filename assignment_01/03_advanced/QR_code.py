import qrcode
import cv2
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr(data, filename="qr_code.png"):
    """Generates a QR code image from input data."""
    qr = qrcode.QRCode(
        version=1,  # size of the QR Code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"[+] QR Code saved as '{filename}'")

def decode_qr(image_path):
    """Decodes the QR code from an image file."""
    img = cv2.imread(image_path)
    decoded_objects = decode(img)
    if not decoded_objects:
        print("[-] No QR code detected.")
        return

    for obj in decoded_objects:
        print(f"[+] Decoded Data: {obj.data.decode('utf-8')}")

if __name__ == "__main__":
    print("QR Code Encoder/Decoder")
    print("1. Generate QR Code")
    print("2. Decode QR Code")
    choice = input("Select an option (1/2): ").strip()

    if choice == '1':
        text = input("Enter text to encode: ")
        generate_qr(text)
    elif choice == '2':
        path = input("Enter path to QR code image: ")
        decode_qr(path)
    else:
        print("Invalid choice. Exiting.")
