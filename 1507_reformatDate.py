class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":'-01-', "Feb":'-02-', "Mar":'-03-',
                 "Apr":'-04-', "May":'-05-', "Jun":'-06-',
                 "Jul":'-07-', "Aug":'-08-', "Sep":'-09-',
                 "Oct":'-10-', "Nov":'-11-', "Dec":'-12-'}
        date = date.split()
        if len(date[0]) == 4:
            day = date[0][:2]
        else:
            day = "0" + date[0][0]
        return date[2] + month[date[1]] + day

# Alternative solution

class Solution1:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":'-01-', "Feb":'-02-', "Mar":'-03-',
                 "Apr":'-04-', "May":'-05-', "Jun":'-06-',
                 "Jul":'-07-', "Aug":'-08-', "Sep":'-09-',
                 "Oct":'-10-', "Nov":'-11-', "Dec":'-12-'}
        if date[4] == ' ':
            return date[9:] + month[date[5:8]] + date[:2]
        else:
            return date[8:] + month[date[4:7]] + "0" + date[0][0]
