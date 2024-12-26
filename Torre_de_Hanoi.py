import tkinter as tk
import time

class TorreDeHanoi:
    def __init__(self, master, num_discos):
        self.master = master
        self.num_discos = num_discos
        self.pegs = [[], [], []]  # Tres varas de la torre
        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()
        self.create_pegs()
        self.create_discs()

    def create_pegs(self):
        # Crear las tres varas
        for i in range(3):
            x = 150 + i * 200
            self.canvas.create_line(x, 150, x, 300, width=5)

    def create_discs(self):
        for i in range(3):
            x = 150 + i * 200
            self.canvas.create_line(x, 150, x, 300, width=5)

    def create_discs(self):
        # Crear los discos y ubicarlos en la primera vara
        for i in range(self.num_discos):
            width = 120 - i * 15
            disc = self.canvas.create_rectangle(
                150 - width // 2,
                280 - i * 20,
                150 + width // 2,
                300 - i * 20,
                fill="blue"
            )
            self.pegs[0].append(disc)

    def move_disc(self, from_peg, to_peg):
        # Mover un disco de una vara a otra
        disc = self.pegs[from_peg].pop()
        self.pegs[to_peg].append(disc)

        # Animar el movimiento
        x_from = 150 + from_peg * 200
        x_to = 150 + to_peg * 200
        y_to = 280 - len(self.pegs[to_peg]) * 20
        self.animate_move(disc, x_from, x_to, y_to)

    def animate_move(self, disc, x_from, x_to, y_to):
        # Obtener las coordenadas actuales del disco
        x0, y0, x1, y1 = self.canvas.coords(disc)
        dx = (x_to - (x0 + x1) / 2) / 20
        dy_up = -5
        dy_down = (y_to - y1) / 20

        # Subir el disco
        for _ in range(20):
            self.canvas.move(disc, 0, dy_up)
            self.master.update()
            time.sleep(0.01)

        # Mover horizontalmente
        for _ in range(20):
            self.canvas.move(disc, dx, 0)
            self.master.update()
            time.sleep(0.01)

        # Bajar el disco
        for _ in range(20):
            self.canvas.move(disc, 0, dy_down)
            self.master.update()
            time.sleep(0.01)

    def solve_hanoi(self, n, from_peg, to_peg, aux_peg):
        if n == 1:
            self.move_disc(from_peg, to_peg)
            return
        self.solve_hanoi(n - 1, from_peg, aux_peg, to_peg)
        self.move_disc(from_peg, to_peg)
        self.solve_hanoi(n - 1, aux_peg, to_peg, from_peg)

# Configuración de la ventana
def main():
    root = tk.Tk()
    root.title("Torre de Hanói")
    num_discos = int(input("Introduce el número de discos (2-8): "))
    if not (2 <= num_discos <= 8):
        print("Por favor, ingresa un número de discos entre 2 y 8.")
        return

    hanoi = TorreDeHanoi(root, num_discos)

    # Resolver el problema después de un pequeño retraso
    root.after(1000, lambda: hanoi.solve_hanoi(num_discos, 0, 2, 1))
    root.mainloop()

if __name__ == "__main__":
    main()




