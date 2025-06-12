class Solution {
public:
    string dayOfTheWeek(int day, int month, int year) {
        int days[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int start = day + 4;

        if (year % 4 == 0 && year != 2100) {
            days[1]++;
        }

        for (int i = 1971; i < year; i++) {
            if (i % 4 == 0) {
                start += 366;
            } else {
                start += 365;
            }
        }

        for (int i = 0; i < month - 1; i++) {
            start += days[i];            
        }

        std::unordered_map<int, std::string> weekMap;

        weekMap[0] = "Sunday";
        weekMap[1] = "Monday";
        weekMap[2] = "Tuesday";
        weekMap[3] = "Wednesday";
        weekMap[4] = "Thursday";
        weekMap[5] = "Friday";
        weekMap[6] = "Saturday";

        return weekMap[start % 7];
    }
};
