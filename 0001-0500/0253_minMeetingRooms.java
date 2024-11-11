class Solution {
    public int minMeetingRooms(int[][] intervals) {
        List<int[]> allPoints = new ArrayList<>();

        for (int i = 0; i < intervals.length; i++) {
            allPoints.add(new int[] {intervals[i][0], 1});
            allPoints.add(new int[] {intervals[i][1], 0});
        }

        Collections.sort(allPoints, Comparator.comparingInt((int[] a) -> a[0]).thenComparingInt(a -> a[1])); 
        int numberOfMeetingRooms = 0;
        int currentRoom = 0;
        
        for (int i = 0; i < allPoints.size(); i++) {
            if (allPoints.get(i)[1] == 1) {
                currentRoom++;  
            } else {
                currentRoom--;
            }
            numberOfMeetingRooms = Math.max(numberOfMeetingRooms, currentRoom);
        }
        
        return numberOfMeetingRooms;
    }
}
