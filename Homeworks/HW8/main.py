import fileIO
import view
import UI

data = fileIO.read_data('data.csv')
UI.menu(data)