import pickle
import csv
import os

class Database():   
    def __init__(self, filename, provider):
        self.provider = provider
        self.contents = []
        self.filename = filename
        if self.provider == "pickle":
            self.filename = self.filename + ".dat"
        elif self.provider == "csv":
            self.filename = self.filename + ".csv"
        
        self.load()

    def load(self):
        if self.provider == "pickle":
            if os.path.isfile(self.filename):
                in_file = open(self.filename, "rb")
                self.contents = pickle.load(in_file)
                in_file.close()
        elif self.provider == "csv":
            if os.path.isfile(self.filename):
                with open(self.filename) as csvfile:
                    reader = csv.DictReader(csvfile)
                    self.contents = list(reader)

    def save(self):
        if self.provider == "pickle":
            out_file = open(self.filename, "wb")
            pickle.dump(self.contents, out_file)
            out_file.close()
        elif self.provider == "csv":
            data = []
            line = []
            for key in self.contents[0].keys():
                line.append(key)
            data.append(line)
            line = []

            for entry in self.contents:
                for key in entry.keys():
                    line.append(entry[key])
                data.append(line)
                line = []
            
            with open(self.filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                for line in data:
                    writer.writerow(line)
            
    def add(self, obj):
        self.contents.append(obj)
        self.save()

    def getall(self):
        return self.contents

    def getwhere(self, key, value):
        self.load()
        
        outputlist = []
        
        for entry in self.contents:
            if entry[key] == value:
                outputlist.append(entry)

        return outputlist

    def purge(self):
        self.contents = []
        self.save()
