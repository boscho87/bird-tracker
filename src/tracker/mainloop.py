from src.tracker.capturer import Capturer
from src.tracker.entity.match import Match
from src.tracker.predictor import Predictor


class MainLoop:
    predictor: Predictor
    capturer: Capturer

    def __init__(self):
        self.predictor = Predictor()
        self.capturer = Capturer()
        print("MainLoop init")

    def execute(self):
        print("MainLoop execute")
        # Video Sequenz in mp4 format aufnehmen
        sequence = self.capturer.capture()
        # prüfen ob es sich um einen Vogel handelt
        match = self.predictor.predict(sequence)

        if isinstance(match, Match):
            #Sequence abspeichern
            #counter in der Datenbank erhöhen (file link in db speichern)
            #Von Zeit zu Zeit notification senden, dass neue Videos gibt
            print("Match found")
            return

        print("No match found")
        # wenn es keinen match gibt, sequence/bilder für späteres training speichern
        # counter in der DB erhöhen
        # Von Zeit zu Zeit notification senden, dass es bilder fürs training gibt
