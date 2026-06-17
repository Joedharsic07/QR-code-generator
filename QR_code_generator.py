import qrcode  # Importing the qrcode library to generate QR codes
import os  # Importing the os library to handle file paths and directories

data = "Hello John"
image = qrcode.make(data)  # Generating a QR code image from the provided data
file_name = "qrcode.png"
output_folder = "Your output folder path (e.g., C:\\example\\folder)"  # Specifying the output folder where the QR code image will be saved
main_output_file = os.path.join(
    output_folder, file_name
)  # Creating the full path for the output file by joining the output folder and file name

# Checking if the output folder exists, if not, it creates the folder
if not os.path.exists(output_folder):
    print(f"Output folder '{output_folder}' does not exist. Creating it...")
    os.makedirs(output_folder)

# Checking if the output file already exists, if it does, it creates a new file with a different name
if os.path.exists(main_output_file):
    print(
        f"File '{main_output_file}' already exists. Creating a new file with a different name..."
    )
    changed_name = file_name.split(".")[0] + "_new." + file_name.split(".")[1]
    main_output_file = os.path.join(output_folder, changed_name)
    print(f"New file name: '{changed_name}' created.")
save_image = image.save(
    main_output_file
)  # Saving the generated QR code image to the specified output file path
print(f"QR code image saved successfully at: '{main_output_file}'")
