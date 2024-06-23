import graphviz

# Context Level DFD (Level 0)
context_level_dfd = graphviz.Digraph('Context_Level_DFD', format='png')
context_level_dfd.attr(rankdir='LR')

# External Entities
context_level_dfd.node('User', shape='rectangle')
context_level_dfd.node('ExternalStorage', 'External Storage', shape='rectangle')

# Process
context_level_dfd.node('ConvertPDF', 'Convert PDF', shape='circle')

# Data Flows
context_level_dfd.edge('User', 'ConvertPDF', label='Uploads PDF')
context_level_dfd.edge('ConvertPDF', 'User', label='Converted file')
context_level_dfd.edge('ConvertPDF', 'ExternalStorage', label='Stored converted file')

context_level_dfd.render('Context_Level_DFD')

# Level 1 DFD
level_1_dfd = graphviz.Digraph('Level_1_DFD', format='png')
level_1_dfd.attr(rankdir='LR')

# External Entities
level_1_dfd.node('User', shape='rectangle')
level_1_dfd.node('ExternalStorage', 'External Storage', shape='rectangle')

# Processes
level_1_dfd.node('ValidatePDF', '1.1 Validate PDF', shape='circle')
level_1_dfd.node('ConvertPDF', '1.2 Convert PDF to Desired Format', shape='circle')
level_1_dfd.node('StoreFile', '1.3 Store Converted File', shape='circle')

# Data Stores
level_1_dfd.node('ConvertedFiles', 'D1: Converted Files', shape='database')

# Data Flows
level_1_dfd.edge('User', 'ValidatePDF', label='Uploads PDF')
level_1_dfd.edge('ValidatePDF', 'ConvertPDF', label='Valid PDF')
level_1_dfd.edge('ConvertPDF', 'StoreFile', label='Converted file')
level_1_dfd.edge('StoreFile', 'ConvertedFiles')
level_1_dfd.edge('StoreFile', 'User', label='Converted file')
level_1_dfd.edge('ConvertedFiles', 'ExternalStorage', label='Stored converted file')

level_1_dfd.render('Level_1_DFD')
