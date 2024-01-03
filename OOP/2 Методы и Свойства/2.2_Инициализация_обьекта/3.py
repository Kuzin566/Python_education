class SoccerPlayer:
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assists = assists

    def score(self, goals=1):
        self.goals = self.goals + goals

    def make_assist(self, assists=1):
        self.assists = self.assists + assists

    def statistics(self):
        print(f"{self.surname} " + f"{self.name} - " + f"голы: {self.goals}, " + f"передачи: {self.assists}")



