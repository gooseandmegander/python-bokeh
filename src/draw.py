import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()

# N sets number of vertices and node_indices creates list with N capacity
N = 8
node_indices = list(range(N))

# Creating the graph plot's title, x-axis range, y-axis range, and tool features (none)
plot = figure(title='Python-Bokeh Demonstration', x_range=(0, 750), y_range=(600, 0),
              tools='', toolbar_location=None)

# graph variable pointing to GraphRenderer class instance
# has node_renderer, edge_renderer, layout_provider
graph = GraphRenderer()

## TODO: Give glyphs labels

# looks like this is adding the list of vertices to a key 'index'
graph.node_renderer.data_source.add(node_indices, 'index')
# looks like this is adding a color palette to node_renderer to use below
graph.node_renderer.data_source.add(Spectral8, 'color')
# oval also takes x, y as arguments before height...
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

# looks like this is adding a dict object holding start and end values of the edges
# here all 7 vertices connect to 1 central vertex (start)
graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

### start of layout code
# creating a circle, x-coordinate, and y-coordinate for each vertex
circ = [i*2*math.pi/N for i in node_indices]
x = [math.cos(i) for i in circ]
y = [math.sin(i) for i in circ]

# creating dict object holding tuples of node and coordinate pairs
# serving it to the graph class' layout
graph_layout = dict(zip(node_indices, zip(x, y))) # [(node_index, (x, y)) * N]
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# adds graph instance of GraphRenderer to graph plot
plot.renderers.append(graph)

output_file('graph.html')
show(plot)