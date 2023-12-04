  + PullRequest

* * *
# PullRequest¶

_class_ `github.PullRequest.`  `PullRequest` ¶

This class represents PullRequests. The reference can be found here https://docs.github.com/en/rest/reference/pulls

`as_issue` () → github. Issue. Issue¶

     Calls:| GET /repos/{owner}/{repo}/issues/{number}

---|---

`create_comment` ( _body: str_ , _commit: github. Commit. Commit_ , _path: str_ , _position: int_ ) → github. PullRequestComment. PullRequestComment¶

     Calls:| POST /repos/{owner}/{repo}/pulls/{number}/comments

---|---

`create_review_comment` ( _body: str_ , _commit: github. Commit. Commit_ , _path: str_ , _line: Union[int_ , _github. GithubObject._NotSetType] = NotSet_ , _side: Union[str_ , 
_github. GithubObject._NotSetType] = NotSet_ , _start_line: Union[int_ , _github. GithubObject._NotSetType] = NotSet_ , _start_side: Union[int_ , _github. GithubObject._NotSetType] = NotSet_ , 
_in_reply_to: Union[int_ , _github. GithubObject._NotSetType] = NotSet_ , _subject_type: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _as_suggestion: bool = False_ ) →
github. PullRequestComment. PullRequestComment¶

     Calls:| POST /repos/{owner}/{repo}/pulls/{number}/comments

---|---

`create_review_comment_reply` ( _comment_id: int_ , _body: str_ ) → github. PullRequestComment. PullRequestComment¶

     Calls:| POST /repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies

---|---

`create_issue_comment` ( _body: str_ ) → github. IssueComment. IssueComment¶

     Calls:| POST /repos/{owner}/{repo}/issues/{number}/comments

---|---

`create_review` ( _commit: Opt[github. Commit. Commit] = NotSet_ , _body: Opt[str] = NotSet_ , _event: Opt[str] = NotSet_ , _comments: Opt[list[ReviewComment]] = NotSet_ ) →
github. PullRequestReview. PullRequestReview¶

     Calls:| POST /repos/{owner}/{repo}/pulls/{number}/reviews

---|---

`create_review_request` ( _reviewers: Opt[list[str] | str] = NotSet_ , _team_reviewers: Opt[list[str] | str] = NotSet_ ) → None¶

     Calls:| POST /repos/{owner}/{repo}/pulls/{number}/requested_reviewers

---|---

`delete_review_request` ( _reviewers: Opt[list[str] | str] = NotSet_ , _team_reviewers: Opt[list[str] | str] = NotSet_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/pulls/{number}/requested_reviewers

---|---

`edit` ( _title: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _body: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _state: Union[str_ , _github. GithubObject._NotSetType] =
NotSet_ , _base: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _maintainer_can_modify: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/pulls/{number}

---|---

`get_comment` ( _id: int_ ) → github. PullRequestComment. PullRequestComment¶

     Calls:| GET /repos/{owner}/{repo}/pulls/comments/{number}

---|---

`get_review_comment` ( _id: int_ ) → github. PullRequestComment. PullRequestComment¶

     Calls:| GET /repos/{owner}/{repo}/pulls/comments/{number}

---|---

`get_comments` ( _sort: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _direction: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _since: Union[datetime.datetime_ , 
_github. GithubObject._NotSetType] = NotSet_ ) → github. PaginatedList. PaginatedList[github. PullRequestComment. PullRequestComment][github. PullRequestComment. PullRequestComment]¶

Warning: this only returns review comments. For normal conversation comments, use get_issue_comments.

Calls:|

GET /repos/{owner}/{repo}/pulls/{number}/comments

---|---
Parameters:|

  + **sort** – string ‘created’ or ‘updated’
  + **direction** – string ‘asc’ or ‘desc’
  + **since** – datetime

`get_review_comments` ( _*_ , _sort: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _direction: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _since: Union[datetime.datetime_ , 
_github. GithubObject._NotSetType] = NotSet_ ) → github. PaginatedList. PaginatedList[github. PullRequestComment. PullRequestComment][github. PullRequestComment. PullRequestComment]¶

     Calls:|

GET /repos/{owner}/{repo}/pulls/{number}/comments

---|---
Parameters:|

  + **sort** – string ‘created’ or ‘updated’
  + **direction** – string ‘asc’ or ‘desc’
  + **since** – datetime

`get_single_review_comments` ( _id: int_ ) → github. PaginatedList. PaginatedList[github. PullRequestComment. PullRequestComment][github. PullRequestComment. PullRequestComment]¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}/review/{id}/comments

---|---

`get_commits` () → github. PaginatedList. PaginatedList[github. Commit. Commit][github. Commit. Commit]¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}/commits

---|---

`get_files` () → github. PaginatedList. PaginatedList[github. File. File][github. File. File]¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}/files

---|---

`get_issue_comment` ( _id: int_ ) → github. IssueComment. IssueComment¶

     Calls:| GET /repos/{owner}/{repo}/issues/comments/{id}

---|---

`get_issue_comments` () → github. PaginatedList. PaginatedList[github. IssueComment. IssueComment][github. IssueComment. IssueComment]¶

     Calls:| GET /repos/{owner}/{repo}/issues/{number}/comments

---|---

`get_issue_events` () → github. PaginatedList. PaginatedList[github. IssueEvent. IssueEvent][github. IssueEvent. IssueEvent]¶

     Calls:| GET /repos/{owner}/{repo}/issues/{issue_number}/events

---|---
Return type:| `github.PaginatedList.PaginatedList` of `github.IssueEvent.IssueEvent`

`get_review` ( _id: int_ ) → github. PullRequestReview. PullRequestReview¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}/reviews/{id}

---|---
Parameters:|  **id** – integer
Return type:| `github.PullRequestReview.PullRequestReview`

`get_reviews` () → github. PaginatedList. PaginatedList[github. PullRequestReview. PullRequestReview][github. PullRequestReview. PullRequestReview]¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}/reviews

---|---
Return type:| `github.PaginatedList.PaginatedList` of `github.PullRequestReview.PullRequestReview`

`get_review_requests` () → tuple[PaginatedList[NamedUser], PaginatedList[github. Team. Team]]¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}/requested_reviewers

---|---
Return type:| tuple of `github.PaginatedList.PaginatedList` of `github.NamedUser.NamedUser` and of `github.PaginatedList.PaginatedList` of `github.Team.Team`

`get_labels` () → github. PaginatedList. PaginatedList[github. Label. Label][github. Label. Label]¶

     Calls:| GET /repos/{owner}/{repo}/issues/{number}/labels

---|---

`add_to_labels` ( _*labels_ ) → None¶

     Calls:| POST /repos/{owner}/{repo}/issues/{number}/labels

---|---

`delete_labels` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/{number}/labels

---|---

`remove_from_labels` ( _label: github. Label. Label | str_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/{number}/labels/{name}

---|---

`set_labels` ( _*labels_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/issues/{number}/labels

---|---

`is_merged` () → bool¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}/merge

---|---

`merge` ( _commit_message: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _commit_title: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _merge_method: Union[str_ , 
_github. GithubObject._NotSetType] = NotSet_ , _sha: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ ) → github. PullRequestMergeStatus. PullRequestMergeStatus¶

     Calls:| PUT /repos/{owner}/{repo}/pulls/{number}/merge

---|---

`add_to_assignees` ( _*assignees_ ) → None¶

     Calls:| POST /repos/{owner}/{repo}/issues/{number}/assignees

---|---

`remove_from_assignees` ( _*assignees_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/{number}/assignees

---|---

`update_branch` ( _expected_head_sha: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ ) → bool¶

:calls PUT /repos/{owner}/{repo}/pulls/{pull_number}/update-branch
