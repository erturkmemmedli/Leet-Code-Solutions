/*
// Definition for an Interval.
class Interval {
    public int start;
    public int end;

    public Interval() {}

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> finalWorkInterval = schedule.get(0);
        List<Interval> result = new ArrayList<>();
        
        for(int i = 1; i < schedule.size(); i++) {
            finalWorkInterval = mergeIntervals(finalWorkInterval, schedule.get(i));
        }
        
        for (int i = 1; i < finalWorkInterval.size(); i++) {
            result.add(new Interval(finalWorkInterval.get(i - 1).end, finalWorkInterval.get(i).start));
        }
        
        return result;
    }
    
    public List<Interval> mergeIntervals(List<Interval> baseInterval, List<Interval> interval) {
        List<Interval> finalInterval = new ArrayList<>(baseInterval);
        finalInterval.addAll(interval);
        
        Collections.sort(finalInterval, (a, b) -> Integer.compare(a.start, b.start));
        List<Interval> result = new ArrayList<>();
        result.add(finalInterval.get(0));
        
        for (int i = 1; i < finalInterval.size(); i++) {
            if (finalInterval.get(i).start <= result.get(result.size() - 1).end) {
                Interval currInterval = new Interval(
                    result.get(result.size() - 1).start, 
                    Math.max(result.get(result.size() - 1).end, finalInterval.get(i).end)
                );
                result.set(result.size() - 1, currInterval);
            } else {
                result.add(finalInterval.get(i));
            }
        }
        
        return result;
    }
}
