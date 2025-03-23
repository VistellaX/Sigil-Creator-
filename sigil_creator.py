import hashlib
import turtle

# --- set caracteres allowed ---
char_set = "0123456789abcdefghijklmnopqrstuvwxyz"

# --- new Mapeamento amplied ---
angle_map = {char: (i * (360 / len(char_set))) for i, char in enumerate(char_set)}  # distribute angles
distance_map = {char: (i * 3) + 140 for i, char in enumerate(char_set)}  # distance betwen 10 and ~100px

# --- phrase reduce ---
def reduce_phrase(text):
    """ Remove vowels and mantain only unique consonants to compactation """
    vowels = "aeiouAEIOU"
    reduced_text = ''.join([char for char in text.lower() if char in char_set and char not in vowels])
    return ''.join(sorted(set(reduced_text), key=reduced_text.index))

# --- generate Hash from reduced phrase ---
def generate_hash(text, length=30):
    """ generate a hash SHA-256 and return first `length` characters, comverting to base 36. """
    reduced_text = reduce_phrase(text)
    full_hash = hashlib.sha256(reduced_text.encode()).hexdigest()
    
    # Convert hexadecimal to alfanumber (0-9, a-z)
    alphanumeric_hash = ''.join(char_set[int(char, 16) % len(char_set)] for char in full_hash[:length])
    
    return alphanumeric_hash  # Return modified hash

# --- draw sigil from intention ---
def draw_sigil(hash_string):
    """ Convert a reduced hash in a geometrical sigil. """
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan") #choose color

    for char in hash_string:
        t.forward(distance_map[char])
        t.right(angle_map[char])
    
    t.hideturtle()
    screen.mainloop()

# --- input: yous affirmative positive phrase ---
intentions = [
    " ", ""
]# you can write to many phrases after comma 

# --- create Sigil from intention  ---
full_text = " ".join(intentions)  
hash_result = generate_hash(full_text)  # generate a reduced hash
print(f"Reduced Alphanumeric Hash: {hash_result}")  

draw_sigil(hash_result)  # Desenha o sigilo
