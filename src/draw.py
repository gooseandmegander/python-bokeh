import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, ColumnDataSource, Range1d, Label, LabelSet
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
# graph_data.debug_create_test_data()
graph_data.randomize(4, 5, 0.5)
graph_data.bfs(graph_data.vertexes[0])

N = len(graph_data.vertexes)
node_indices = list(range(N))


color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

plot = figure(title='Python-Bokeh Demonstration', plot_width=750, plot_height=600, x_range=(0, 750), y_range=(600, 0),
              tools='', toolbar_location=None)

# graph variable pointing to GraphRenderer class instance
# has node_renderer, edge_renderer, layout_provider
graph = GraphRenderer()

## TODO: Give glyphs labels
# Label

label_x_values = []
label_y_values = []
label_vertex_indices = []

for i, vertex in enumerate(graph_data.vertexes):
    label_x_values.append(vertex.pos['y'])
    label_y_values.append(vertex.pos['x'])
    label_vertex_indices.append(i)

source = ColumnDataSource(data=dict(y_axis=label_x_values,
                                    x_axis=label_y_values,
                                    labels=label_vertex_indices))

plot.scatter(x='x_axis', y='y_axis', size=8, source=source)
plot.xaxis[0].axis_label = 'X-Axis'
plot.yaxis[0].axis_label = 'Y-Axis'

labels = LabelSet(x='x_axis', y='y_axis', text='labels', level='overlay',
              x_offset=0, y_offset=0, source=source, render_mode='canvas')



# looks like this is adding the list of vertices to a key 'index'
graph.node_renderer.data_source.add(node_indices, 'index')
# looks like this is adding a color palette to node_renderer to use below
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=30, width=30, fill_color='color')

start_indices = []
end_indices = []

for start_index, vertex in enumerate(graph_data.vertexes):
    for edge in vertex.edges:
        start_indices.append(start_index)
        end_indices.append(graph_data.vertexes.index(edge.destination))

graph.edge_renderer.data_source.data = dict(
    start= start_indices,
    end= end_indices)

### start of layout code
# Makes a list of x-coordinate values and list of y-coordinate values
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

# creating dict object holding tuples of node and coordinate pairs
# serving it to the graph class' layout
graph_layout = dict(zip(node_indices, zip(x, y))) # [(node_index, (x, y)) * N]
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

# adds graph instance of GraphRenderer to graph plot
plot.renderers.append(graph)
plot.add_layout(labels)

output_file('graph.html')
show(plot)