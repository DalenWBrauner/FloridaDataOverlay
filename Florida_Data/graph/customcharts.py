from graphos.renderers import gchart, flot


class CustomGchart(gchart.LineChart):
    def get_template(self):
        return "demo/gchart_line.html"
