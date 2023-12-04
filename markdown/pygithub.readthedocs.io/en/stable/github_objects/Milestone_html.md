  + Milestone

* * *
# Milestone¶

_class_ `github.Milestone.`  `Milestone` ¶

This class represents Milestones. The reference can be found here https://docs.github.com/en/rest/reference/issues#milestones

`delete` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/milestones/{number}

---|---

`edit` ( _title: str_ , _state: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _description: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _due_on: Union[datetime.date_ , 
_github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/milestones/{number}

---|---

`get_labels` () → github. PaginatedList. PaginatedList[github. Label. Label][github. Label. Label]¶

     Calls:| GET /repos/{owner}/{repo}/milestones/{number}/labels

---|---
