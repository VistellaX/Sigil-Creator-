import hashlib
import turtle

# --- Definir caracteres aceitos ---
char_set = "0123456789abcdefghijklmnopqrstuvwxyz"

# --- Novo Mapeamento Ampliado ---
angle_map = {char: (i * (360 / len(char_set))) for i, char in enumerate(char_set)}  # ângulos distribuídos
distance_map = {char: (i * 3) + 140 for i, char in enumerate(char_set)}  # distância entre 10 e ~100px

# --- Redução da Frase ---
def reduce_phrase(text):
    """ Remove vogais e mantém apenas consoantes únicas para compactação. """
    vowels = "aeiouAEIOU"
    reduced_text = ''.join([char for char in text.lower() if char in char_set and char not in vowels])
    return ''.join(sorted(set(reduced_text), key=reduced_text.index))

# --- Gerar Hash da Frase Reduzida ---
def generate_hash(text, length=30):
    """ Gera um hash SHA-256 e retorna os primeiros `length` caracteres, convertendo para base 36. """
    reduced_text = reduce_phrase(text)
    full_hash = hashlib.sha256(reduced_text.encode()).hexdigest()
    
    # Converter hexadecimal para alfanumérico (0-9, a-z)
    alphanumeric_hash = ''.join(char_set[int(char, 16) % len(char_set)] for char in full_hash[:length])
    
    return alphanumeric_hash  # Retorna hash modificado

# --- Desenhar Sigilo a partir das Frases Externas ---
def draw_sigil(hash_string):
    """ Converte um hash reduzido em um sigilo geométrico. """
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("cyan")

    for char in hash_string:
        t.forward(distance_map[char])
        t.right(angle_map[char])
    
    t.hideturtle()
    screen.mainloop()

# --- Entrada: Frases que Alguém Falou ---
external_phrases = [
    "loki"
]

# --- Criar Sigilo a partir do Discurso Externo ---
full_text = " ".join(external_phrases)  # Junta todas as frases
hash_result = generate_hash(full_text)  # Gera um hash reduzido
print(f"Hash Reduzido Alfanumérico: {hash_result}")  

draw_sigil(hash_result)  # Desenha o sigilo