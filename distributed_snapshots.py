import threading
import time
import socket

class ChandyLamportSnapshot(trheading.Thread):
    server_port = 4242
    balance = 1000
    server_map = {"marvin": 0, "blender":1, "hal":2}
    server_list = ['marvin', 'blender', 'hal']
    marker = 0
    state_recorded = False
    marker_list = set()
    attached_channels = dict()
    temp = 0
    acknowledgement = dict()
    send_now = False

    def __init__(self, operation = None):
        threading.Thread.__init__(self)
        self.operation = operation
        self.process1 = ""
        self.process2 = ""
        self.marker_receipt = 0

    def run(self):
        server_socket = socket.socket()

    def initialize_map()
        return {"marvin": 0, "blender":1, "hal":2}
