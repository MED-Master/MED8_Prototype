import os
import glob


class figure:
    Piclist = None  # instantiation of the list of images
    currentPlot = None

    def __init__(self):
        self.Piclist = glob.glob('logs/images/*')  # instantiation of the list of images
        print("THIS IS IN INIT, INNIT?", len(self.Piclist))
        self.currentPlot = 0

    def newestFigure(self, button_pressed=None):
        list_of_files = glob.glob('logs/images/*')  # * means all if need specific format then *.csv
        print("PICLIST:", len(self.Piclist), "LIST:", len(list_of_files))
        if len(self.Piclist) != len(list_of_files):
            self.Piclist = list_of_files
            filename = max(self.Piclist, key=os.path.getctime)
            self.currentPlot += 1
            print("THIS IS THE NEW  IMAGE", len(self.Piclist))
            return filename
        print("THIS IS THE LENGTH OF FILE:", len(self.Piclist))
        print("THIS IS THE FUNCTION:", self.Piclist)
        if button_pressed == "Forward":
            try:
                self.currentPlot += 1
                filename = self.Piclist[self.currentPlot]
                return filename
            except:
                print("Bad boi")
        if button_pressed == "Backward":
            try:
                self.currentPlot -= 1
                filename = self.Piclist[self.currentPlot]
                print(filename)
                return filename
            except:
                print("nope")



    # def CurrentPlot(filename): #returns the index of the input image
    #     list_of_files = glob.glob('logs/images/*')  # * means all if need specific format then *.csv
    #     return list_of_files.index(filename)


    # print('current plot', CurrentPlot())