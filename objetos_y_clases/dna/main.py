class DNA:
    ADENINE = 'A'
    CYTOSINE = 'C'
    THYMINE = 'T'
    GUANINE = 'G'

    def __init__(self, sequence: str):
        self.sequence = sequence

    def __len__(self) -> int:
        return len(self.sequence)
    
    def __str__(self) -> str:
        return self.sequence
    
    @property
    def adenines(self) -> int:
        num_adenines = self.sequence.count(self.ADENINE)
        return num_adenines
    
    @property
    def cytosines(self) -> int:
        num_cystosines = self.sequence.count(self.CYTOSINE)
        return num_cystosines
    
    @property
    def guanines(self) -> int:
        num_guanines = self.sequence.count(self.GUANINE)
        return num_guanines
    
    @property
    def thymines(self) -> int:
        num_thymines = self.sequence.count(self.THYMINE)
        return num_thymines
    
    def __add__(self, other:DNA) -> DNA:
        min_len = min(len(self.sequence), len(other.sequence))
        if isinstance(other, DNA):
           new_sequence = ''
           for base_one, base_two in zip(self.sequence, other.sequence):
               if base_one > base_two:
                   new_sequence += base_one
               elif base_two > base_one:
                   new_sequence += base_two
               else:
                   new_sequence += base_one
        if len(self.sequence) > len(other.sequence):
            new_sequence += self.sequence[min_len:]
        else:
            new_sequence += other.sequence[min_len:]        
        return DNA(new_sequence)