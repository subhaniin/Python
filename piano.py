import msvcrt  # For reading key presses (Windows only)
import winsound  # For playing beeps (Windows only)

# Map keyboard keys to note frequencies (approximate piano notes)
KEY_TO_NOTE = {
    b'a': ("C4", 261),
    b's': ("D4", 294),
    b'd': ("E4", 329),
    b'f': ("F4", 349),
    b'g': ("G4", 392),
    b'h': ("A4", 440),
    b'j': ("B4", 494),
}

NOTE_DURATION_MS = 300  # how long each note plays (in milliseconds)

print("Simple Python Piano 🎹")
print("Press keys: a s d f g h j for C D E F G A B")
print("Press q to quit.")

while True:
    key = msvcrt.getch()  # Wait for a key press

    # Quit if user presses 'q'
    if key in (b'q', b'Q'):
        print("Goodbye! 👋")
        break

    if key in KEY_TO_NOTE:
        note_name, freq = KEY_TO_NOTE[key]
        print(f"Playing {note_name} ({freq} Hz)")
        winsound.Beep(freq, NOTE_DURATION_MS)
    else:
        # Ignore other keys
        print("That key doesn't play a note. Use a s d f g h j or q to quit.")
aa