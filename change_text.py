def change_text(text):
    text=text.replace(b"stockholm",b"linkoping")
    text=text.replace(b"Stockholm",b"Linkoping")
    text=text.replace(b"Smiley",b"Trolly")
    text=text.replace(b"round",b"sharp")
    return text

