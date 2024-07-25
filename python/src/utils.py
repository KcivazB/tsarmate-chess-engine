def index_to_chess_notation(index):
        files = 'abcdefgh'
        ranks = '12345678'
        col = files[index % 8]
        row = ranks[index // 8]
        return f"{col}{row}"

def chess_notation_to_index(notation):
    files = 'abcdefgh'
    ranks = '12345678'
    
    # Extract file and rank from notation
    file = notation[0]
    rank = notation[1]
    
    # Calculate file index (0 for 'a', 1 for 'b', ..., 7 for 'h')
    file_index = files.index(file)
    
    # Calculate rank index (0 for '1', 1 for '2', ..., 7 for '8')
    rank_index = int(rank) - 1
    
    # Calculate and return board index
    return rank_index * 8 + file_index    