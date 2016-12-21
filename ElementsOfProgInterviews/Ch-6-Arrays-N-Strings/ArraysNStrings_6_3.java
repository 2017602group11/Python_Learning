
public class ArraysNStrings_6_3 {
	
	/*
	 * Problem: 6.3 Design an algorithm that takes a sequence of n three-dimensional
coordinates to be traversed, and returns the minimum battery capacity needed to complete
thejourney. The robot begins with a fully charged battery.
	 */

	public static int find_max_batt(int[] A){
		if(A.length<1)
			return 0;
		int maxdiff =0;
		int minHeight=A[0];
		for (int j=1; j< A.length; ++j){
			maxdiff= Math.max(maxdiff, A[j]-minHeight);
			minHeight=Math.min(minHeight, A[j]);
		}
		return maxdiff;
	}
	
	public static void main(String[] args){
		int[] arr = {7,2,3,1,2,5,6,9,2,2,0};
		System.out.println(find_max_batt(arr));
	}
	
}

