class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        match = 0
        p, t = 0, 0

        while p<len(players) and t<len(trainers):
            if players[p] <= trainers[t]:
                match += 1
                p += 1
                t += 1
            else:
                t += 1
        return match