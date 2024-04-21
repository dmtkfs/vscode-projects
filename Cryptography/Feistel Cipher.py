from tools.checkers import check_binary_array, check_valid_key_length
from tools.modify import array_split
from tools.generators import primary_key_generator, roundkey_generator


inputarray = list(input("Give 8-bit input: "))
rounds = int(input("How many rounds?: "))
while not check_binary_array(inputarray):
    inputarray = list(input("Not bits or not 8. Give 8-bit input: "))

l_array, r_array = array_split(inputarray)
print(f" Input split: {l_array, r_array}")

keylength = int(input("Choose key length (128-bit, 192-bit or 256-bit): "))
while not check_valid_key_length(keylength):
    keylength = int(
        input("Invalid choice. Choose key length (128-bit, 192-bit or 256-bit): ")
    )
primarykey = primary_key_generator(keylength)
print(f"Primary Key: {primarykey}")
print(f"Round Keys: {roundkey_generator(primarykey, rounds)}")
