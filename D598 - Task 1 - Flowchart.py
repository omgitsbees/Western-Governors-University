from graphviz import Digraph

# Create flowchart
flowchart = Digraph(format='png', engine='dot')
flowchart.attr(rankdir='TB', size='8,10')

# Define nodes
flowchart.node('Start', 'START', shape='oval', style='filled', color='lightgreen')
flowchart.node('Import', 'Import Data\nLoad Dataset into DataFrame', shape='parallelogram', style='filled', color='lightblue')
flowchart.node('Duplicates', 'Identify Duplicates\nCheck for duplicate rows', shape='rectangle', style='filled', color='lightyellow')
flowchart.node('Group', 'Group by State\nCalculate statistics', shape='rectangle', style='filled', color='lightyellow')
flowchart.node('Filter', 'Filter Negative Debt-to-Equity\nIdentify rows', shape='diamond', style='filled', color='lightpink')
flowchart.node('Calculate', 'Create Debt-to-Income Ratio\nCalculate Ratio', shape='rectangle', style='filled', color='lightyellow')
flowchart.node('Concatenate', 'Concatenate DataFrames\nMerge all data', shape='rectangle', style='filled', color='lightyellow')
flowchart.node('Output', 'Output Results\nSave or Display', shape='parallelogram', style='filled', color='lightblue')
flowchart.node('End', 'END', shape='oval', style='filled', color='lightgreen')

# Define edges
flowchart.edge('Start', 'Import')
flowchart.edge('Import', 'Duplicates')
flowchart.edge('Duplicates', 'Group')
flowchart.edge('Group', 'Filter')
flowchart.edge('Filter', 'Calculate')
flowchart.edge('Calculate', 'Concatenate')
flowchart.edge('Concatenate', 'Output')
flowchart.edge('Output', 'End')

# Render the flowchart
flowchart.render('flowchart_equity_analysis_corrected', cleanup=True, format='png')

print("Flowchart generated successfully.")
