import pickle

def save_game(data, filename='save_game'):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    print(f"Game saved to {filename}")

def load_game(filename='save_game'):
    try:
        with open(filename, 'rb') as file:
            loaded_data = pickle.load(file)
        print(f"Game loaded from {filename}")
        return loaded_data
    except FileNotFoundError:
        print("No saved game found.")
        return None