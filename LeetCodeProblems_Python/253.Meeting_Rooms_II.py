class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for m in intervals:
            start.append(m[0])
            end.append(m[1])
        
        start.sort()
        end.sort()
        s, e =0, 0
        rooms = 0
        maxRooms = 0
        while s < len(intervals):
            if start[s] < end[e]:
                rooms +=1
                s+=1
            else:
                rooms -= 1
                e+=1
            maxRooms = max(maxRooms, rooms)
        return maxRooms