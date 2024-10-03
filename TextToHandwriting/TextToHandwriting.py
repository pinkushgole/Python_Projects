# pip install pywhatkit

import pywhatkit as kit

text = "Hello, this is a sample text converted to handwriting."

save_path = "handwriting_output.png"

kit.text_to_handwriting(text)

print(f"Handwriting image saved to {save_path}")

