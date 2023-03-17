import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def configAndPlotData(plotSetup, data, os):

    # figure properties
    width = plotSetup['output']['config']['figure']['size']['width']*0.393701
    heigth = plotSetup['output']['config']['figure']['size']['heigth']*0.393701
    visible = plotSetup['output']['config']['figure']['visible']
    fontName = plotSetup['output']['config']['figure']['font']
    
    fig = plt.figure(figsize = [width, heigth])

    # default of math text (format as LaTeX)
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["mathtext.default"] = "it"
    plt.rcParams["mathtext.fontset"] = "cm"

    # configure axis settings
    bottomStickMin = plotSetup['output']['config']['axis']['limits']['bottom']['min']
    bottomStickMax = plotSetup['output']['config']['axis']['limits']['bottom']['max']
    bottomStickStep = plotSetup['output']['config']['axis']['stick']['bottom']
    bottomAxisColor = plotSetup['output']['config']['axis']['color']['bottom']
    bottomLabel = plotSetup['output']['config']['axis']['label']['bottom']
    bottomExponent = plotSetup['output']['config']['axis']['exponent']['bottom']
    bottomLabelFormat = plotSetup['output']['config']['axis']['format']['bottom']
    bottomLabelFlag = plotSetup['output']['config']['axis']['active']['bottom']
    bottomMinorStickStep = plotSetup['output']['config']['axis']['minorStick']['bottom']

    leftStickMin = plotSetup['output']['config']['axis']['limits']['left']['min']
    leftStickMax = plotSetup['output']['config']['axis']['limits']['left']['max']
    leftStickStep = plotSetup['output']['config']['axis']['stick']['left']
    leftAxisColor = plotSetup['output']['config']['axis']['color']['left']
    leftLabel = plotSetup['output']['config']['axis']['label']['left']
    leftExponent = plotSetup['output']['config']['axis']['exponent']['left']
    leftLabelFormat = plotSetup['output']['config']['axis']['format']['left']
    leftLabelFlag = plotSetup['output']['config']['axis']['active']['left']
    leftMinorStickStep = plotSetup['output']['config']['axis']['minorStick']['left']

    rightStickMin = plotSetup['output']['config']['axis']['limits']['right']['min']
    rightStickMax = plotSetup['output']['config']['axis']['limits']['right']['max']
    rightStickStep = plotSetup['output']['config']['axis']['stick']['right']
    rightAxisColor = plotSetup['output']['config']['axis']['color']['right']
    rightLabel = plotSetup['output']['config']['axis']['label']['right']
    rightExponent = plotSetup['output']['config']['axis']['exponent']['right']
    rightLabelFormat = plotSetup['output']['config']['axis']['format']['right']
    rightLabelFlag = plotSetup['output']['config']['axis']['active']['right']

    labelFontSize = plotSetup['output']['config']['axis']['labelFontSize']

    plt.rc('axes', labelsize = labelFontSize)
    plt.rc('xtick', labelsize = labelFontSize)    # fontsize of the tick labels
    plt.rc('ytick', labelsize = labelFontSize)    # fontsize of the tick labels
    
    ax = plt.gca()
    if (rightLabelFlag):
        ax1 = ax.twinx()
    ax.set_xticks(np.arange(bottomStickMin,bottomStickMax+bottomStickStep,bottomStickStep))
    ax.set_yticks(np.arange(leftStickMin,leftStickMax+leftStickStep,leftStickStep))
    ax.set_xlim([bottomStickMin, bottomStickMax])
    ax.set_ylim([leftStickMin, leftStickMax])
    
    # Set the axis properties
    ax.set_xlabel(xlabel = bottomLabel, fontname = fontName, fontsize = labelFontSize)
    ax.set_ylabel(ylabel = leftLabel, fontname = fontName, fontsize = labelFontSize)
    ax.spines['bottom'].set_color(bottomAxisColor)
    ax.spines['left'].set_color(leftAxisColor) 
    ax.tick_params(axis = 'x', colors = bottomAxisColor)
    ax.tick_params(axis = 'y', colors = leftAxisColor)
    ax.xaxis.label.set_color(bottomAxisColor)
    ax.yaxis.label.set_color(leftAxisColor)
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(bottomLabelFormat))
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(leftLabelFormat))
    ax.tick_params(direction = 'inout', length = 10, width = 1.0)
    ax.tick_params(axis = 'both', which = 'minor', length = 0)

    # Set the right or top axes (if needed)
    if (rightLabelFlag):
        ax1.set_ylim([rightStickMin, rightStickMax])
        ax1.set_yticks(np.arange(rightStickMin,rightStickMax+rightStickStep,rightStickStep))
        ax1.set_ylabel(ylabel = rightLabel, fontname = fontName, fontsize = labelFontSize)
        ax1.spines['right'].set_color(rightAxisColor) 
        ax1.tick_params(axis = 'y', colors = rightAxisColor)
        ax1.yaxis.label.set_color(rightAxisColor)
        ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter(rightLabelFormat))
        ax1.tick_params(direction = 'inout', length = 10, width = 1.0)
        ax1.tick_params(axis = 'both', which = 'minor', length = 0)
    
    # Set the font name for axis tick labels to be Serif
    for tick in ax.get_xticklabels():
        tick.set_fontname("serif")
    for tick in ax.get_yticklabels():
        tick.set_fontname("serif")

    # Grid configurations
    xGrid = plotSetup['output']['config']['axis']['grid']['x']
    yGrid = plotSetup['output']['config']['axis']['grid']['y']
    gridLineStyle = plotSetup['output']['config']['axis']['grid']['lineStyle']
    gridAlpha = plotSetup['output']['config']['axis']['grid']['alpha']
    outSideBox = plotSetup['output']['config']['figure']['outsideBox']
    rightMinorStickStep = plotSetup['output']['config']['axis']['minorStick']['left']

    # Turn off the outside boc
    if (outSideBox):
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)  
        if (rightLabelFlag):
            ax1.spines.left.set_visible(False)
            ax1.spines.bottom.set_visible(False)
            ax1.spines.top.set_visible(False)  

    # Set the ticks positions
    ax.set_xticks(np.arange(bottomStickMin,bottomStickMax+bottomMinorStickStep,bottomMinorStickStep), minor=True)
    ax.set_yticks(np.arange(leftStickMin,leftStickMax+leftMinorStickStep,leftMinorStickStep), minor=True)

    # Set the grid spacing
    if (xGrid):
        ax.grid(axis = 'x', which = 'minor', linestyle = '--', alpha = gridAlpha*0.5)
        ax.grid(axis = 'x', which = 'major', linestyle = gridLineStyle, alpha = gridAlpha)
    if (yGrid):
        ax.grid(axis = 'y', which = 'major', linestyle = gridLineStyle, alpha = gridAlpha)
        ax.grid(axis = 'y', which = 'minor', linestyle = '--', alpha = gridAlpha*0.5)

    handles = []
    nPlots = len(data)
    for i in range(nPlots):
        # data setting for each plot
        lineSpec = plotSetup['input'][i]['config']['lineSpec']
        lineWidth = plotSetup['input'][i]['config']['lineWidth']
        lineColor = plotSetup['input'][i]['config']['lineColor']
        markerSize = plotSetup['input'][i]['config']['markerSize']
        markerSample = plotSetup['input'][i]['config']['markerSample']
        markerEdgeColor = plotSetup['input'][i]['config']['markerEdgeColor']
        markerFaceColor = plotSetup['input'][i]['config']['markerFaceColor']
        legendName = plotSetup['input'][i]['config']['legendName']
        try:
            xScale = plotSetup['input'][i]['config']['xScale']
        except:
            xScale = 1.0
        try:
            yScale = plotSetup['input'][i]['config']['scaleFactor']
        except:
            yScale = 1.0
        try:
            yScale = plotSetup['input'][i]['config']['yScale']
        except:
            yScale = 1.0
        try:
            xShift = plotSetup['input'][i]['config']['xShift']
        except:
            xShift = 0.0
        try:
            yShift = plotSetup['input'][i]['config']['yShift']
        except:
            yShift = 0.0
        try:
            xAxis = plotSetup['input'][i]['config']['axis']['x']
            yAxis = plotSetup['input'][i]['config']['axis']['y']
        except:
            xAxis = "bottom"
            yAxis = "left"
        if (xAxis == "bottom" and yAxis == "left"):
            axis = 0
        elif (xAxis == "bottom" and yAxis == "right"):
            axis = 1
        try:
            plotType = plotSetup['input'][i]['config']['plotType']
        except:
            plotType = "line"
       
        # edit the data (shift and scale)
        x = data[i][0]
        y = data[i][1]
        for j in range(len(x)):
            x[j] = x[j]*xScale+xShift
        for j in range(len(y)):
            y[j] = y[j]*yScale+yShift

        # plot of each data series
        if (axis == 0):
            if (plotType == "line"):
                handle = ax.plot(x, y, lineSpec, figure = fig, linewidth = lineWidth, color = lineColor, markersize = markerSize,
                markevery = markerSample, markeredgecolor = markerEdgeColor, markerfacecolor = markerFaceColor, 
                markeredgewidth = lineWidth, label = legendName)
            elif (plotType == "bar"):
                barWidth = plotSetup['input'][i]['config']['barWidth']
                ax.bar(x, y, figure = fig, linewidth = lineWidth, width = barWidth, 
                edgecolor = markerEdgeColor, color = markerFaceColor, label = legendName)

        if (axis == 1):
            if (plotType == "line"):
                handle = ax1.plot(x, y, lineSpec, figure = fig, linewidth = lineWidth, color = lineColor, markersize = markerSize,
                markevery = markerSample, markeredgecolor = markerEdgeColor, markerfacecolor = markerFaceColor, 
                markeredgewidth = lineWidth, label = legendName)
            elif (plotType == "bar"):
                barWidth = plotSetup['input'][i]['config']['barWidth']
                ax.bar(x, y, figure = fig, linewidth = lineWidth, width = barWidth, 
                edgecolor = markerEdgeColor, color = markerFaceColor, label = legendName)

        if (legendName != ""):
            handles = handles + handle

    # legend settings
    location = plotSetup['output']['config']['legend']['location']
    orientation = plotSetup['output']['config']['legend']['orientation']
    boxFlag = plotSetup['output']['config']['legend']['box']
    legendFontSize = plotSetup['output']['config']['legend']['fontSize']
    nColumns = plotSetup['output']['config']['legend']['columns']
    active = plotSetup['output']['config']['legend']['active']

    labels = [label.get_label() for label in handles]
    leg = plt.legend(handles, labels, loc = location, ncol = nColumns, fontsize = legendFontSize,
    fancybox = boxFlag, framealpha = 1.0, borderpad = 0.05, columnspacing = 0.3, 
    handletextpad = 0.3, handlelength = 1.5, labelspacing = 0.2)
    leg.get_frame().set_edgecolor('k')
    leg.get_frame().set_boxstyle('Square')
    plt.setp(leg.texts, family='Times New Roman')
    if (active == "off"):
        leg.remove()
    
    # output file name and folder
    fig.tight_layout()
    folder = plotSetup['output']['data']['folder']
    fileName = plotSetup['output']['data']['filename']
    if (os == "ubuntu"):
        fullFileName = folder+"/"+fileName+".jpg"
    elif (os == "windows"):
        fullFileName = folder+"\\"+fileName+".jpg"
   
    plt.savefig(fullFileName)

    if (visible):
        plt.show()