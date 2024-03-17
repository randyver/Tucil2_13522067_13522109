import bezier_visualize

def print_title():
    print("---------------------------------------------------------------------------------------")
    title = """
██████╗░███████╗███████╗███████╗██╗██████╗░  ░█████╗░██╗░░░██╗██████╗░██╗░░░██╗███████╗
██╔══██╗██╔════╝╚════██║██╔════╝██║██╔══██╗  ██╔══██╗██║░░░██║██╔══██╗██║░░░██║██╔════╝
██████╦╝█████╗░░░░███╔═╝█████╗░░██║██████╔╝  ██║░░╚═╝██║░░░██║██████╔╝╚██╗░██╔╝█████╗░░
██╔══██╗██╔══╝░░██╔══╝░░██╔══╝░░██║██╔══██╗  ██║░░██╗██║░░░██║██╔══██╗░╚████╔╝░██╔══╝░░
██████╦╝███████╗███████╗███████╗██║██║░░██║  ╚█████╔╝╚██████╔╝██║░░██║░░╚██╔╝░░███████╗
╚═════╝░╚══════╝╚══════╝╚══════╝╚═╝╚═╝░░╚═╝  ░╚════╝░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
"""
    print(title)
    print("---------------------------------------------------------------------------------------")

def run_program():
    order = int(input("Masukkan order kurva n (1 untuk linier, 2 untuk quadratic, dst): "))

    control_points: list[tuple[float, float]] = []
    print(f"Masukkan {order + 1} titik kontrol (P_0, ..., P_{order}):")
    for i in range(order + 1):
        point = map(float, input().split())
        control_points.append(tuple(point))

    control_points_str = ', '.join([f'({x}, {y})' for x, y in control_points])
    print("Titik kontrol:", control_points_str)

    iteration = int(input("Masukkan jumlah iterasi: "))

    while True:
        print("""Pilihan pembuatan kurva Bezier
        1. Divide and Conquer
        2. Bruteforce""")

        option = int(input("Masukkan pilihan: "))
        if option in [1, 2]:
            break
        print("Opsi tidak valid. Harap masukkan angka 1 atau 2.")
    
    if option == 1:
        bezier_visualize.visualize(order, control_points, iteration)
    else:
        bezier_visualize.visualize_bruteforce(order, control_points)

print_title()
while True:
    # print_title()
    run_program()
    print("---------------------------------------------------------------------------------------")
    run_again = input("Apakah Anda ingin menjalankan program lagi? (Y/N): ").strip().upper()
    print("---------------------------------------------------------------------------------------")
    if run_again != 'Y':
        break