class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        double[][] workerInfo = new double[quality.length][2];
        PriorityQueue<Double> heap = new PriorityQueue<>();
        double minWage = Double.MAX_VALUE;
        double currQuality = 0;

        for (int i = 0; i < quality.length; i++) {
            workerInfo[i][0] = (double)wage[i]/(double)quality[i];
            workerInfo[i][1] = (double)quality[i];
        }
        
        Arrays.sort(workerInfo, (a, b) -> Double.compare(a[0], b[0]));

        for (int i = 0; i < quality.length; i++) {
            heap.offer(-workerInfo[i][1]);
            currQuality += workerInfo[i][1];

            if (heap.size() == k) {
                minWage = Math.min(minWage, currQuality * workerInfo[i][0]);
                currQuality += heap.poll();
            }
        }

        return minWage;
    }
}
