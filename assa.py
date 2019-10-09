from io import StringIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

def graph_create(points, title, xlabel, ylabel):
    fig = Figure(facecolor = 'white', edgecolor = 'white')
    graph = fig.add_subplot(111)

    graph.set_title(title)
    graph.set_xlabel(xlabel)
    graph.set_ylabel(ylabel)

    graph.grid()
#    graph.legend(["hello"]) Выдает ошибку Division by Zero

    for x, y, f in points:
        graph.plot_date(x, y, f) #Если нужны даты по оси x, если обычные данные, используйте graph.plot(x, y, f)

    graph.xaxis.set_major_formatter(DateFormatter("%Y.%m.%d %H:%M")) #Опять же, если даты.
    fig.autofmt_xdate()
    output = StringIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(output)
    return output.getvalue()


def showimage(request, points, title, xlabel, ylabel):
    pic = graph_create(points, title, xlabel, ylabel)
    response = HttpResponse(pic, content_type = 'image/png')
    return response




def graph(request):
    x, y = [1, 2, 3], [2, 3, 4]
    u, v = [-1, -2, -3], [-2, -3, -5]
    title = u'Пробный график'
    xlabel = u'Время'
    ylabel = u'Энергия'
    points = [(x, y, 'g^'), (u, v, 'ro')]
    return showimage(request, points, title, xlabel, ylabel)

graph()