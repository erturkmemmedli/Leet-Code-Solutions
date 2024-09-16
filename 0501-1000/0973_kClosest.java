class Tuple implements Comparator<Tuple> {
    private int xCoordinate;
    private int yCoordinate;
    private double distance;

    public Tuple(int xCoordinate, int yCoordinate, double distance) {
        this.xCoordinate = xCoordinate;
        this.yCoordinate = yCoordinate;
        this.distance = distance;
    }

    public int getX() {
        return this.xCoordinate;
    }

    public int getY() {
        return this.yCoordinate;
    }

    public double getDistance() {
        return this.distance;
    }

    @Override
    public int compare(Tuple o1, Tuple o2) {
        return Double.compare(o1.distance, o2.distance);
    }
}

class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Tuple> pQueue = new PriorityQueue<>(new Tuple(0, 0, 0.0));
        int[][] result = new int[k][2];

        for(int[] coordinate: points) {
            int x = coordinate[0];
            int y = coordinate[1];
            double distance = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));

            if (pQueue.size() < k) {
                pQueue.add(new Tuple(x, y, -distance));
                continue;
                
            }

            if (-pQueue.peek().getDistance() > distance) {
                pQueue.poll();
                pQueue.add(new Tuple(x, y, -distance));
            }
        }

        int i = 0;
        
        while (!pQueue.isEmpty()) {
            Tuple tuple = pQueue.poll();
            result[i][0] = tuple.getX();
            result[i][1] = tuple.getY();
            i++;
        }

        return result;
    }
}
