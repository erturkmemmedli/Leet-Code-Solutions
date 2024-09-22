class MedianFinder {
    PriorityQueue<Double> maxHeap;
    PriorityQueue<Double> minHeap;

    public MedianFinder() {
        maxHeap = new PriorityQueue<>();
        minHeap = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        if (maxHeap.isEmpty() || num < -maxHeap.peek()) {
            maxHeap.offer((double)-num);
        } else {
            minHeap.offer((double)num);
        }

        if (maxHeap.size() == minHeap.size() + 2) {
            minHeap.offer(-maxHeap.poll());
        }

        if (maxHeap.size() + 1 == minHeap.size()) {
            maxHeap.offer(-minHeap.poll());
        }
    }
    
    public double findMedian() {
        if (minHeap.size() == maxHeap.size()) {
            return (minHeap.peek() - maxHeap.peek()) / 2;
        } else {
            return -maxHeap.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
