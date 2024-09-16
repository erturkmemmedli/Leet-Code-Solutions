class Solution {
    public int maxScore(int[] cardPoints, int k) {
        List<Integer> points = new ArrayList<>();
        for (int i=cardPoints.length-k; i<cardPoints.length; i++) points.add(cardPoints[i]);
        for (int i=0; i<k; i++) points.add(cardPoints[i]);
        int windowSum = 0;
        for (int i=0; i<k; i++) windowSum += points.get(i);
        int maxPoint = windowSum;
        for (int i=k; i<points.size(); i++) {
            windowSum += points.get(i) - points.get(i-k);
            maxPoint = Math.max(maxPoint, windowSum);
        }
        return maxPoint;
    }
}

// Alternative solution

class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        int windowSum = 0;
        for (int i=n-k; i<n; i++) windowSum += cardPoints[i];
        int maxPoint = windowSum;
        for (int i=n; i<n+k; i++) {
            windowSum += cardPoints[i%n] - cardPoints[(i-k)%n];
            maxPoint = Math.max(maxPoint, windowSum);
        }
        return maxPoint;
    }
}
