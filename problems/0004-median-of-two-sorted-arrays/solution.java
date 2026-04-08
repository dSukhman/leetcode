class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int len1 = nums1.length;
        int len2 = nums2.length;

        int left = 0;
        int right = len1;

        while (left <= right) {

            int x = (left + right) / 2;
            int y = (len1 + len2 + 1) / 2 - x;

            int left1  = (x == 0)    ? Integer.MIN_VALUE : nums1[x - 1];
            int right1 = (x == len1) ? Integer.MAX_VALUE : nums1[x];

            int left2  = (y == 0)    ? Integer.MIN_VALUE : nums2[y - 1];
            int right2 = (y == len2) ? Integer.MAX_VALUE : nums2[y];

            if (left1 <= right2 && left2 <= right1) {
                if ((len1 + len2) % 2 == 0) {
                    return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
                } else {
                    return Math.max(left1, left2);
                }

            } else if (left1 > right2) {
                right = x - 1;
            } else {
                left = x + 1;
            }
        }

        throw new IllegalArgumentException();
    }
}