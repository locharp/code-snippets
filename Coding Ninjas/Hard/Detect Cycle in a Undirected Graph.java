import java.util.*;
/*
 * class Graph {
	int V; // No. of vertices
	ArrayList<Integer> adj[]; // Pointer to an array containing adjacency lists
 */
public class solution
{

	static boolean f
	( Graph g, HashSet< Integer > set, int curr, Integer last )
	{
		boolean t = false;
		set.add( curr );
		
		
		for ( Integer i : g.adj[ curr ] )
		{
			if ( set.contains( i ) )
			{
				if ( i.equals( last ) )
				{
					if ( t )
					{
						return t;
					}
					else
					{
						t = true;
					}
				}
				else
				{
					return true;
				}
			}
			else
			{
				if ( f( g, set, i, curr ) )
				{
					return true;
				}
			}
		}


		return false;
	}

	

	static boolean isCyclic
	( Graph g )
	{
		for ( int i = 0; i < g.V; i++ )
		{
			HashSet< Integer > set = new HashSet<>();


			if ( f( g, set, i, null ) )
			{
				return true;
			}
		}
		return false;
	}

}
