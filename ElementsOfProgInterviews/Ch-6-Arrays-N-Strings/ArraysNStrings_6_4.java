
// Problem 6.4
// For each of the following, A is an integer array of length n
// (1) Compute the maximum value of ( A[j0] - A[i0] ) + ( A[j1] - A[i1] ),
//     subject to i0 < j0 < i1 < j1.
// (2) Compute the maximum value of ( A[j0] - A[i0] ) + ( A[j1] - A[i1] ) + ...
//     + ( A[jk-1] - A[ik-1] ), subject to i0 < j0 < i1 < j1 < ... < jk-1 < ik-1
// (3) Repeat (2) when k can be chosen to be any value from 0 to n/2

public class ArraysNStrings_6_4 {
	
	public static int max_2_pairs_profits(int[] A){
		int min=A[0];
		int[] left = new int[A.length];
		int[] right = new int[A.length];
		left[0]=0;
		right[A.length-1]=0;
		
		min=A[0];
		for(int i=1;i<A.length;++i){
			left[i]=Math.max( left[i-1], A[i]-min);
			min=Math.min(min, A[i]);
		}
		
		int max=A[A.length -1];
		for(int j=A.length-2;j>0;--j){
			right[j]=Math.max( right[j+1], max - A[j]);
			max=Math.max(max, A[j]);
		}
		
		int maxprofit=0;
		for (int k=0;k<=A.length; k++){
			maxprofit = Math.max( maxprofit, left[k]+right[k]);
		}
		System.out.println(min+' '+max);
		
		return maxprofit;	
	}
	
	public static void main(String[] args){
		int[] arr = {7,2,3,1,2,5,6,9,2,2,0};
		System.out.println(max_2_pairs_profits(arr));
	}

}
