import PySimpleGUI as sg
import csv

sg.theme('Topanga')

# defining layout of gui
layout = [
    [sg.Text('Please enter the url, name(code), and buy below price:')],
    [sg.Text('URL', size=(15, 1)), sg.InputText()],
    [sg.Text('Code', size=(15, 1)), sg.InputText()],
    [sg.Text('Buy Below Price', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

# calling window with label
window = sg.Window('Add Product to Tracker', layout)
event, values = window.read()
window.close()

# assigning variable to input and appending it to csv
vals = values[0],values[1],values[2]
with open('PRODUCT_TRACKER.csv', mode='a') as tracker_file:
    tracker_writer = csv.writer(tracker_file, lineterminator='\n', delimiter=',')
    tracker_writer.writerow(vals)
