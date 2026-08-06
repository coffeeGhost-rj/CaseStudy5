# with open('text.dat', 'r+') as f:
#     # Comment: 
#     # print(f.read())
#     list1 = ["\n hey there","\n what's up?"]
#     f.writelines(list1)
# end open file


import pickle

# # A complex dictionary to save
# data_to_save = {"user": "Alice", "scores": [95, 88, 100], "verified": True}

# # --- PICKLING ---
# # Open a file in Write-Binary ('wb') mode
# with open("game_data.dat", "wb") as file:
#     pickle.dump(data_to_save, file)

# # --- UNPICKLING ---
# Open the file in Read-Binary ('rb') mode
# with open("game_data.dat", "rb") as file:
with open("text.dat", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
# # Output: {'user': 'Alice', 'scores': [95, 88, 100], 'verified': True}
