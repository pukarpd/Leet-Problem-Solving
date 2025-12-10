class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n = nums.length;

    // Handle small cases
    if (n == 1) {
        return nums[0];
    }
    if (n == 2) {
        return (nums[0] + nums[1]) / 2.0;
    }

    // Sliding window setup
    int i = 0, j = k - 1;
    double val = Double.NEGATIVE_INFINITY;

    while (j < n) {
        // Compute sum of current window
        int sum = 0;
        for (int idx = i; idx <= j; idx++) {
            sum += nums[idx];
        }

        double avgVal = (double) sum / k;
        val = Math.max(val, avgVal);

        i++;
        j++;
    }

    return val;
    }
}