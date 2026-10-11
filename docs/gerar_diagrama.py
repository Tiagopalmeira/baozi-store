"""Gera docs/diagrama-caso-de-uso.png (Diagrama de Caso de Uso UML da API Baozi Store)."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch, Rectangle

ENTIDADES = ["Cliente", "Produto", "Pedido"]
ACOES = ["Cadastrar {}", "Listar {}s", "Consultar {} por ID", "Atualizar {} (opcional)", "Apagar {}"]

fig, ax = plt.subplots(figsize=(11, 15))
ax.set_xlim(0, 112)
ax.set_ylim(0, 150)
ax.axis("off")

# Limite do sistema
ax.add_patch(Rectangle((32, 4), 77, 138, fill=False, lw=1.6))
ax.text(70.5, 145, "API REST - Baozi Store", ha="center", fontsize=15, weight="bold")

# Ator (boneco UML)
ax_x, ax_y = 12, 72
ax.add_patch(plt.Circle((ax_x, ax_y + 9), 2.6, fill=False, lw=1.6))
ax.plot([ax_x, ax_x], [ax_y + 6.4, ax_y - 2], color="black", lw=1.6)
ax.plot([ax_x - 5, ax_x + 5], [ax_y + 3.5, ax_y + 3.5], color="black", lw=1.6)
ax.plot([ax_x, ax_x - 4.5], [ax_y - 2, ax_y - 9], color="black", lw=1.6)
ax.plot([ax_x, ax_x + 4.5], [ax_y - 2, ax_y - 9], color="black", lw=1.6)
ax.text(ax_x, ax_y - 13, "Usuário da API", ha="center", fontsize=12, weight="bold")

uc_x, uc_w, uc_h = 58, 38, 5.6
passo = 7.2
y = 132
for entidade in ENTIDADES:
    # Agrupamento visual por entidade
    topo, base = y + 4.5, y - 4 * passo - 4.5
    ax.add_patch(FancyBboxPatch((37, base), 44, topo - base, boxstyle="round,pad=0.6",
                                fill=True, fc="#f3f6fb", ec="#9aa8c0", lw=1, ls="--"))
    ax.text(38.5, topo - 1.5, entidade, fontsize=10, style="italic", color="#4a5a78")

    for acao in ACOES:
        nome = acao.format(entidade)
        ax.add_patch(Ellipse((uc_x, y), uc_w, uc_h, fill=True, fc="white", ec="black", lw=1.3))
        ax.text(uc_x, y, nome, ha="center", va="center", fontsize=10)
        ax.plot([ax_x + 5.5, uc_x - uc_w / 2], [ax_y + 3.5, y], color="black", lw=0.8)

        if nome == "Cadastrar Pedido":
            # <<include>>: o cadastro de pedido valida se cliente e produto existem
            vx, vy = 95, y - 8
            ax.add_patch(Ellipse((vx, vy), 22, 7, fill=True, fc="white", ec="black", lw=1.3))
            ax.text(vx, vy, "Validar cliente\ne produto", ha="center", va="center", fontsize=9)
            ax.annotate("", xy=(vx - 5, vy + 3.2), xytext=(uc_x + uc_w / 2 - 2, y - 1.5),
                        arrowprops=dict(arrowstyle="->", ls="--", lw=1))
            ax.text(88, y - 1.4, "«include»", fontsize=8.5, ha="center")

        y -= passo
    y -= 6

saida = Path(__file__).with_name("diagrama-caso-de-uso.png")
fig.savefig(saida, dpi=160, bbox_inches="tight", facecolor="white")
print(saida)
