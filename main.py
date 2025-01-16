import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Load the InkML file
inkml_file = "mathwriting-2024/mathwriting-2024/test/0baddebeb93d38ba.inkml"  # Update path
tree = ET.parse(inkml_file)
root = tree.getroot()

# Define the namespace and register it
namespace = {"ink": "http://www.w3.org/2003/InkML"}
ET.register_namespace("ink", "http://www.w3.org/2003/InkML")

# Extract annotations
annotations = {
    ann.attrib["type"]: ann.text for ann in root.findall(".//ink:annotation", namespace)
}

print("Annotations:", annotations)

# extract trace format
trace_format = [channel.attrib['name'] for channel in root.find('ink:traceFormat', namespace)]

#extract trace data
traces = []
all_strokes = []

for trace in root.findall('ink:trace', namespace):
    trace_id = trace.attrib['id']
    trace_data = trace.text.strip()
    raw_points = trace_data.split(",")

    points = []

    for raw_point in raw_points:
        x_y_t = raw_point.split()

        x = float(x_y_t[0])
        y = float(x_y_t[1])
        t = float(x_y_t[2])

        points.append([x, y ,t])

    all_strokes.append(points)

x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Plot the points
plt.figure(figsize=(6, 6))

for stroke in all_strokes:
    x_coords = [point[0] for point in stroke]  # Extract X coordinates for the stroke
    y_coords = [point[1] for point in stroke]  # Extract Y coordinates for the stroke
    plt.plot(x_coords, y_coords, marker='o', linestyle='-', label=f"Stroke {all_strokes.index(stroke) + 1}")

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Handwriting Trace Visualization')
plt.legend()
plt.grid(True)
plt.gca().invert_yaxis()  # Invert Y-axis to match typical handwriting visualization
plt.show()
