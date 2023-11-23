class player:
    def __init__(self, screen, font, char, x, y, own, amount = 3, move = False): #char = (image,size)
        self.screen = screen
        self.font = font
        self.image = char[0]
        self.orix = x
        self.oriy = y
        self.x = x
        self.y = y
        self.size = char[1]
        self.own = own
        self.amount = amount
        self.move = move

    def back(self):
            self.x = self.orix
            self.y = self.oriy

    def update(self, x, y):
        if not self.move and self.amount > 0:
            self.x = x
            self.y = y

    def draw(self):
        if self.amount > 0:
            self.screen.blit(self.image, (self.x, self.y))
            self.area = self.image.get_rect()
            self.area.topleft = (self.x, self.y)

    def stop(self, move):
        self.move = move
    
    def use(self):
        self.amount -= 1

    def text(self):
        message = f"{self.amount}"
        text = self.font.render(message, True, "BLACK")
        text_rect = text.get_rect(center=(self.orix, self.oriy))
        self.screen.blit(text, text_rect)