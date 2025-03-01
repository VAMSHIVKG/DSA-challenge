import qrcode
from PIL import Image

def generate_qr_code(roll_no, name, branch, cgpa):
    # Construct the data string for QR code
    data = f"Roll No: {roll_no}\nName: {name}\nBranch: {branch}\nCGPA: {cgpa}"

    # Generate QR code instance
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Create PIL Image from the QR code instance
    qr_image = qr.make_image(fill='black', back_color='white')

    return qr_image

def main():
    # Student information
    roll_number = "12345"
    student_name = "John Doe"
    student_branch = "Computer Science"
    student_cgpa = "3.8"

    # Generate QR code image
    qr_code_image = generate_qr_code(roll_number, student_name, student_branch, student_cgpa)

    # Display the QR code image
    qr_code_image.show()

    # Save the QR code image to a file
    qr_code_image.save("student_qr_code.png")

    print("QR code generated and displayed. Saved as 'student_qr_code.png'")

if __name__ == "__main__":
    main()
