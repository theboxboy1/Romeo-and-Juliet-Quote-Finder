import re
import difflib

def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text.lower())

def main():
    file_name = "randj.txt"
    quote = input("Enter a quote from Romeo and Juliet: ")

    with open(file_name, "r") as file:
        lines = file.readlines()

    current_act = ""
    current_scene = ""
    current_character = ""
    line_number = 1
    quote_found = False
    similarity_threshold = 0.8

    for line in lines:
        if "PROLOGUE" in line:
            current_act = "Prologue"
            current_scene = ""
        elif "ACT " in line:
            act_match = re.search("ACT ([IVX]+)", line)
            if act_match:
                current_act = act_match.group(1)
        elif "SCENE " in line:
            scene_match = re.search("SCENE ([IVX0-9]+)", line)
            if scene_match:
                current_scene = scene_match.group(1)
                line_number = 1
        elif re.match("^[A-Z]+\\.", line):
            character_match = re.match("^([A-Z]+)\\.", line)
            if character_match:
                current_character = character_match.group(1)
        elif re.search("\\[.*?\\]", line):
            continue
        else:
            line_number += 1

        similarity = difflib.SequenceMatcher(None, clean_text(quote), clean_text(line)).ratio()
        if similarity >= similarity_threshold:
            print(f"Act: {current_act}, Scene: {current_scene}, Line: {line_number}, Character: {current_character}")
            quote_found = True
            break

    if not quote_found:
        print("Quote not found.")

if __name__ == "__main__":
    main()
