

  * Docs »
  * Reference »
  * Github objects »
  * IssueComment
  * Edit on GitHub

* * *

# IssueComment¶

_class_`github.IssueComment.``IssueComment`¶

    

This class represents IssueComments. The reference can be found here https://docs.github.com/en/rest/reference/issues#comments

`delete`() → None¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/comments/{id}  
---|---  
  
`edit`( _body: str_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/issues/comments/{id}  
---|---  
  
`get_reactions`() → PaginatedList[Reaction]¶

     Calls:| GET /repos/{owner}/{repo}/issues/comments/{id}/reactions  
---|---  
  
`create_reaction`( _reaction_type: str_ ) → Reaction¶

     Calls:| POST /repos/{owner}/{repo}/issues/comments/{id}/reactions  
---|---  
  
`delete_reaction`( _reaction_id: int_ ) → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}  
---|---  
  
Read the Docs v: stable

Versions

     latest
     stable
     v2.1.1
     v2.1.0.post0
     v2.1.0
     v2.0.1-preview
     v2.0.0-preview.1
     v2.0.0-preview
     v1.59.1
     v1.59.0
     v1.58.2
     v1.58.1
     v1.58.0
     v1.57

On Read the Docs

     Project Home
     Builds
     Downloads

On GitHub

     View

Search

    

* * *

Hosted by Read the Docs ·  Privacy Policy

