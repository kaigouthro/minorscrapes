  + PullRequestComment

* * *
# PullRequestComment¶

_class_ `github.PullRequestComment.`  `PullRequestComment` ¶

This class represents PullRequestComments. The reference can be found here https://docs.github.com/en/rest/reference/pulls#review-comments

`delete` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/pulls/comments/{number}

---|---
Return type:| None

`edit` ( _body: str_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/pulls/comments/{number}

---|---
Parameters:|  **body** – string
Return type:| None

`get_reactions` () → github. PaginatedList. PaginatedList[github. Reaction. Reaction][github. Reaction. Reaction]¶

     Calls:| GET /repos/{owner}/{repo}/pulls/comments/{number}/reactions

---|---
Returns:|  | class:| `github.PaginatedList.PaginatedList` of `github.Reaction.Reaction`

---|---

`create_reaction` ( _reaction_type: str_ ) → github. Reaction. Reaction¶

     Calls:| POST /repos/{owner}/{repo}/pulls/comments/{number}/reactions

---|---
Parameters:|  **reaction_type** – string
Return type:| `github.Reaction.Reaction`

`delete_reaction` ( _reaction_id: int_ ) → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}

---|---
Parameters:|  **reaction_id** – integer
Return type:| bool
