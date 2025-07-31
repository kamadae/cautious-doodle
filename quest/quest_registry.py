class QuestRegistry:
    def __init__(self):
        self.quests = {}

    def register(self, quest):
        self.quests[quest.name] = quest
