class Solution {
public:
    int dayOfYear(string date) {
        int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        std::string yearStr = date.substr(0, 4);
        int year = std::stoi(yearStr);
        std::string monthStr = date.substr(5, 7);
        int month = std::stoi(monthStr);
        std::string dayStr = date.substr(8, 10);
        int day = std::stoi(dayStr);
        
        if (year % 4 == 0 and year != 1900) {
            days[1] = 29;
        }
        
        for (int i = 0; i < month - 1; i++) {
            day += days[i];
        }

        return day; 
    }
};
