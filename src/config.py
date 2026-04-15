class Config:
    def __init__(self):
        self.clip = \
            {
                "lines": [],
                "poly": []
            }

    def clear_clip(self):
        self.clip["lines"].clear()
        self.clip["poly"].clear()

    def add_clip_line(self, line):
        self.clip["lines"].append(line)

    def del_clip_line(self, line):
        self.clip["lines"].remove(line)

    def add_clip_poly(self, poly):
        self.clip["poly"].append(poly)

    def del_clip_poly(self, poly):
        self.clip["poly"].remove(poly)
