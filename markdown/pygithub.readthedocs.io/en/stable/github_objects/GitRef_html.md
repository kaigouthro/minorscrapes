  + GitRef

* * *
# GitRef¶

_class_ `github.GitRef.`  `GitRef` ¶

This class represents GitRefs. The reference can be found here https://docs.github.com/en/rest/reference/git#references

`delete` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/git/refs/{ref}

---|---

`edit` ( _sha: str_ , _force: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/git/refs/{ref}

---|---
