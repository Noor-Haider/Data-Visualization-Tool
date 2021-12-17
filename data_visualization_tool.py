import pandas as pd
import matplotlib.pyplot as pyplot


class FileHandling:
    def __init__(self, file):
        self.file = file

    def getSep(self):   # Detects which separator is being used in the csv file
        file = self.file

        with open(file) as file:
            lines = file.readlines()

        if "," in lines[0]:
            return ","
        elif ";" in lines[0]:
            return ";"

    def getCategories(self):    # Extracts column headers
        file = self.file

        with open(file) as file:
            lines = file.read().split('\n')

        categories = lines[0].split(self.getSep())

        return categories

    def getData(self):      # Extracts data set associated with each column header
        data = pd.read_csv(self.file, sep=self.getSep())
        data = data[self.getCategories()]

        return data


class Visualize:
    def __init__(self, data, graphType, xLabel, yLabel, xData, yData, title, style):
        self.data = data
        self.graphType = graphType
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.xData = data[xData]
        self.yData = data[yData]
        self.title = title
        self.style = style

    def checkStyle(self):   # Checks which style has been selected and returns the matplotlib's equivalent
        style = self.style

        if style == "default":
            return "ggplot"
        elif style == "plain":
            return "default"
        elif style == "grayscale":
            return "grayscale"
        elif style == "bold":
            return "fivethirtyeight"
        elif style == "outline grid":
            return "classic"

    def design(self):   # Adds style, labels and title elements to the graph
        pyplot.style.use(self.checkStyle())
        pyplot.xlabel(self.xLabel)
        pyplot.ylabel(self.yLabel)
        pyplot.title(self.title)

    # Functions to generate various graph types
    def scatterPlot(self):
        self.design()
        pyplot.scatter(self.xData, self.yData)
        pyplot.show()

    def horizontalBar(self):
        self.design()
        pyplot.barh(self.xData, self.yData)
        pyplot.show()

    def verticalBar(self):
        self.design()
        pyplot.bar(self.xData, self.yData)
        pyplot.show()

    def histogram(self):
        self.design()
        pyplot.hist2d(self.xData, self.yData)
        pyplot.show()

    def stem(self):
        self.design()
        pyplot.stem(self.xData, self.yData)
        pyplot.show()

    def create(self):   # Checks which graph type has been selected and generates graph accordingly
        graphType = self.graphType

        if graphType == "scatter plot":
            self.scatterPlot()
        elif graphType == "stem plot":
            self.stem()
        elif graphType == "vertical bar":
            self.verticalBar()
        elif graphType == "horizontal bar":
            self.horizontalBar()
        elif graphType == "2D histogram":
            self.histogram()

