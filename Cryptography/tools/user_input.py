from tools.checkers import check_binary_array


def get_binary_input(messagelength):
    input_str = input(f"Give {messagelength}-bit input: ")
    while not check_binary_array(input_str, messagelength):
        input_str = input(
            f"Not bits or not {messagelength}. Give {messagelength}-bit input: "
        )
    return [int(bit) for bit in input_str]
