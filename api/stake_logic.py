import hmac
import hashlib

def generate_mines_layout(server_seed, client_seed, nonce, minesCount):
    combined = f"{server_seed}:{client_seed}:{nonce}"
    hash_bytes = hmac.new(server_seed.encode(), combined.encode(), hashlib.sha256).hexdigest()

    numbers = []
    for i in range(0, len(hash_bytes), 4):
        chunk = hash_bytes[i:i+4]
        if len(chunk) == 4:
            numbers.append(int(chunk, 16))

    bomb_tiles = []
    i = 0
    while len(bomb_tiles) < minesCount and i < len(numbers):
        index = numbers[i] % 25
        if index not in bomb_tiles:
            bomb_tiles.append(index)
        i += 1

    return bomb_tiles