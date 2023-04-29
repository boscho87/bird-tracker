from src.tracker.entity.sequence import Sequence


class Match:
    species_name: str
    species_id: int
    sequence: Sequence

    def __init__(self, species_name: str, species_id: int, sequence: Sequence):
        print("Match init")
        self.sequence = sequence
        self.species_name = species_name
        self.species_id = species_id

    def get_sequence(self):
        return self.sequence
