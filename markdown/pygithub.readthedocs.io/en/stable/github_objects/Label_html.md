  + Label

* * *
# Label¶

_class_ `github.Label.`  `Label` ¶

This class represents Labels. The reference can be found here https://docs.github.com/en/rest/reference/issues#labels

`delete` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/labels/{name}

---|---

`edit` ( _name: str_ , _color: str_ , _description: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/labels/{name}

---|---
