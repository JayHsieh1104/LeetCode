class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.split(' ', 2)
        
        year = date[2]
        
        month_dict = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        month = month_dict[date[1]]
        
        day = date[0]
        if len(day) == 4:
            day = day[0:2]
        else:
            day = "0" + day[0]
            
        return year + "-" + month + "-" + day