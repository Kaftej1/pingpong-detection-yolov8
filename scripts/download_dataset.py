from roboflow import Roboflow
rf = Roboflow(api_key="xO4tLrRweYuKAVsWK5Df")
project = rf.workspace("vertex-dl0xb").project("table-tennis-53jaz")
version = project.version(11)
dataset = version.download("yolov8")
                