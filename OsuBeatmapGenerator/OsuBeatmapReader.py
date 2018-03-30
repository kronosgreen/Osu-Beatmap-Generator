#
#   Osu Beatmap Generator Project
#
#       by Christopher Medrano
#
#   Osu Beatmap Reader File
#
#   Info: This file is meant to create instances of an Osu Beatmap from a '.osu' file, parsing
#           the file as text, retrieving all of the info needed (i.e. beat location, tempo, length,
#           note type, etc.)
#

import os, sys

class OsuMap:
    def __init__(self, osuFile):

        self.fileFormat = ""
        self.general = []
        self.editor = []
        self.metadata = []
        self.difficulty = []
        self.events = []
        self.timingPoints = []
        self.hitPoints = []
        self.colour = []
        self.parsing = "file format"

        with open(osuFile, 'r') as myFile:
            for line in myFile:
                if line == "[General]":
                    parsing = "general"
                    continue
                elif line == "[Editor]":
                    parsing = "editor"
                    continue
                elif line == "[Metadata]":
                    parsing = "metadata"
                    continue
                elif line == "[Difficulty]":
                    parsing = "difficulty"
                    continue
                elif line == "[Events]":
                    parsing = "events"
                    continue
                elif line == "[Timing Points]":
                    parsing = "timing points"
                    continue
                elif line == "[Hit Points]":
                    parsing = "hit points"
                    continue
                elif line == "[Colour]":
                    parsing = "colour"
                    continue


                if parsing == "file format":
                    self.fileFormat = line
                    parser = "null"
                elif parsing == "general":
                    self.general.append(line)
                elif parsing == "editor":
                    self.editor.append(line)
                elif parsing == "metadata":
                    self.metadata.append(line)
                elif parsing == "difficulty":
                    self.difficulty.append(line)
                elif parsing == "events":
                    self.events.append(line)
                elif parsing == "timing points":
                    timings = line.split(',')
                    self.timingPoints.append(timings)
                elif parsing == "hit points":
                    hits = line.split(',')
                    self.hitPoints.append(hits)
                elif parsing == "colour":
                    self.colour.append(line)




class OsuFolderReader:
    def __init__(self, folderAddress):
        addr = "./" + folderAddress
        for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
            base_file, ext = os.path.splitext(filename)
            if ext == ".osu":
                os.rename(filename, base_file + ".text")
            osuFile = OsuMap(filename)