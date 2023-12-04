  + Project

* * *
# Project¶

_class_ `github.Project.`  `Project` ¶

This class represents Projects. The reference can be found here https://docs.github.com/en/rest/reference/projects

`delete` () → None¶

     Calls:| DELETE /projects/{project_id}

---|---

`edit` ( _name: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _body: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _state: Union[str_ , _github. GithubObject._NotSetType] =
NotSet_ , _organization_permission: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _private: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /projects/{project_id}

---|---

`get_columns` () → github. PaginatedList. PaginatedList[github. ProjectColumn. ProjectColumn][github. ProjectColumn. ProjectColumn]¶

     Calls:| GET /projects/{project_id}/columns

---|---

`create_column` ( _name: str_ ) → github. ProjectColumn. ProjectColumn¶

calls: POST /projects/{project_id}/columns
