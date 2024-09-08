from matplotlib.lines import Line2D


# Отрисовка графика.
def show(ax, stickPos, qPos, forceVec):
    ax.add_line(Line2D((stickPos[0][0], stickPos[1][0]), (stickPos[0][1], stickPos[1][1]), color='r'))
    ax.plot(qPos[0], qPos[1], '.', markersize=15)

    x1 = min(stickPos[0][0], qPos[0])
    x2 = max(stickPos[1][0], qPos[0])
    y1 = min(stickPos[0][1], qPos[1])
    y2 = max(stickPos[0][1], qPos[1])
    ax.plot(x1-2, y1-2, ' w', markersize=5)
    ax.plot(x2+2, y1-2, ' w', markersize=5)
    ax.plot(x1-2, y2+2, ' w', markersize=5)
    ax.plot(x2+2, y2+2, ' w', markersize=5)

    if list(forceVec) != [0, 0]:
        ax.arrow(qPos[0], qPos[1], forceVec[0], forceVec[1], head_width=0.2, head_length=0.2)

