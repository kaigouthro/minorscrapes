  + ProjectCard

* * *
# ProjectCard¶

_class_ `github.ProjectCard.`  `ProjectCard` ¶

This class represents Project Cards. The reference can be found here https://docs.github.com/en/rest/reference/projects#cards

`get_content` ( _content_type: Opt[str] = NotSet_ ) → github. PullRequest. PullRequest | github. Issue. Issue | None¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}

---|---

`move` ( _position: str_ , _column: github. ProjectColumn. ProjectColumn | int_ ) → bool¶

     Calls:| POST /projects/columns/cards/{card_id}/moves

---|---

`delete` () → bool¶

     Calls:| DELETE /projects/columns/cards/{card_id}

---|---

`edit` ( _note: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _archived: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /projects/columns/cards/{card_id}

---|---
