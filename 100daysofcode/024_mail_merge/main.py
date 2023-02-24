from pathlib import Path

INVITED_NAMES_PATH = Path("Input") / "Names" / "invited_names.txt"
STARTING_LETTER_PATH = Path("Input") / "Letters" / "starting_letter.txt"
OUTPUT_PATH = Path("Output") / "ReadyToSend"


with STARTING_LETTER_PATH.open() as letter_file:
    letter_template = letter_file.read()

with INVITED_NAMES_PATH.open() as names_file:
    for name in names_file.readlines():
        letter_text = letter_template.replace("[name]", name.strip())
        output_filepath = OUTPUT_PATH / f"letter_for_{name.strip()}.txt"
        with output_filepath.open(mode="w") as file:
            file.write(letter_text)
