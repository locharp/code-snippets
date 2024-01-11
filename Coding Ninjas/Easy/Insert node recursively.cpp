Node* InsertNode( Node *head, int pos, Node* newNode )
{
    if ( pos < 1 )
    {
	    newNode->next = head;
	    return newNode;
    }

    Node *curr = head;

	while ( pos-- > 1 )
	{
		curr = curr->next;
	}

	newNode->next = curr->next;
	curr->next = newNode;

	return head;
}
