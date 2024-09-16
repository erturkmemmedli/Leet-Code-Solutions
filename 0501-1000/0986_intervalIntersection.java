class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int i = 0;
        int j = 0;
        List<int[]> result = new ArrayList<>();

        while (i < firstList.length && j < secondList.length) {
            if (firstList[i][1] < secondList[j][1]) {
                if (firstList[i][1] >= secondList[j][0]) {
                    result.add(new int[] {Math.max(firstList[i][0], secondList[j][0]), firstList[i][1]});
                }
                i++;
            } else if (firstList[i][1] > secondList[j][1]) {
                if (secondList[j][1] >= firstList[i][0]) {
                    result.add(new int[] {Math.max(firstList[i][0], secondList[j][0]), secondList[j][1]});
                }
                j++;
            } else {
                result.add(new int[] {Math.max(firstList[i][0], secondList[j][0]), secondList[j][1]});
                i++;
                j++; 
            }
        }

        return result.toArray(new int[result.size()][2]);
    }
}
