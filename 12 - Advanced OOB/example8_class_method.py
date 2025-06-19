class Fashion:
    
    def __init__(self, style):
        self.style = style
    
    @classmethod
    def casual(cls):
        return cls(["tshirt", "jeans", "sneakers"])
    def formal(cls):
        return cls(["tuxedo","celana bahan","pantofel"])
    
ricko_formal = Fashion.casual()

print(ricko_formal.style)
        