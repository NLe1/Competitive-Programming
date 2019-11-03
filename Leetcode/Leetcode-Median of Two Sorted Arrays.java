class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] i = new int[nums1.length + nums2.length];
        System.arraycopy(nums1, 0, i, 0, nums1.length);
		System.arraycopy(nums2, 0, i, nums1.length, nums2.length);
        Arrays.sort(i);
        if(i.length %2==1)
            return i[i.length/2]*1.00;
        else
            return (i[i.length/2-1]+i[i.length/2])/2.00;
    }

}