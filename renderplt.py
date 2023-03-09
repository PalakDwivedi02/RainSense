import matplotlib.pyplot as plt
import mpld3

def renderplt():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
    return mpld3.fig_to_html(fig)

if __name__ == '__main__':
    html_str = renderplt()
    Html_file= open("plots.html","w")
    Html_file.write(html_str)
    Html_file.close()