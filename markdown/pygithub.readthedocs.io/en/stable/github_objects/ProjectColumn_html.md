

  * Docs »
  * Reference »
  * Github objects »
  * ProjectColumn
  * Edit on GitHub

* * *

# ProjectColumn¶

_class_`github.ProjectColumn.``ProjectColumn`¶

    

This class represents Project Columns. The reference can be found here https://docs.github.com/en/rest/reference/projects#columns

`get_cards`( _archived_state: Union[str_ , _github.GithubObject._NotSetType] = NotSet_ ) → github.PaginatedList.PaginatedList[github.ProjectCard.ProjectCard][github.ProjectCard.ProjectCard]¶

     Calls:| GET /projects/columns/{column_id}/cards  
---|---  
  
`create_card`( _note: Union[str_ , _github.GithubObject._NotSetType] = NotSet_ , _content_id: Union[int_ , _github.GithubObject._NotSetType] = NotSet_ , _content_type: Union[str_ ,
_github.GithubObject._NotSetType] = NotSet_ ) → github.ProjectCard.ProjectCard¶

     Calls:| POST /projects/columns/{column_id}/cards  
---|---  
  
`move`( _position: str_ ) → bool¶

     Calls:| POST POST /projects/columns/{column_id}/moves  
---|---  
  
`delete`() → bool¶

     Calls:| DELETE /projects/columns/{column_id}  
---|---  
  
`edit`( _name: str_ ) → None¶

     Calls:| PATCH /projects/columns/{column_id}  
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

