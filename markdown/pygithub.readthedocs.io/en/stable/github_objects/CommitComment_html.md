  + CommitComment

* * *
# CommitComment¶

_class_ `github.CommitComment.`  `CommitComment` ¶

This class represents CommitComments. The reference can be found here https://docs.github.com/en/rest/reference/repos#comments

`delete` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/comments/{id}

---|---
Return type:| None

`edit` ( _body: str_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/comments/{id}

---|---

`get_reactions` () → PaginatedList[Reaction]¶

     Calls:| GET /repos/{owner}/{repo}/comments/{id}/reactions

---|---
Returns:|  | class:| `github.PaginatedList.PaginatedList` of `github.Reaction.Reaction`

---|---

`create_reaction` ( _reaction_type: str_ ) → Reaction¶

     Calls:| POST /repos/{owner}/{repo}/comments/{id}/reactions

---|---

`delete_reaction` ( _reaction_id: int_ ) → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}

---|---
Parameters:|  **reaction_id** – integer
Return type:| bool
