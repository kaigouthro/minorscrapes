  + Issue

* * *
# Issue¶

_class_ `github.Issue.`  `Issue` ¶

This class represents Issues. The reference can be found here https://docs.github.com/en/rest/reference/issues

`as_pull_request` () → PullRequest¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}

---|---

`add_to_assignees` ( _*assignees_ ) → None¶

     Calls:| POST /repos/{owner}/{repo}/issues/{number}/assignees

---|---

`add_to_labels` ( _*labels_ ) → None¶

     Calls:| POST /repos/{owner}/{repo}/issues/{number}/labels

---|---

`create_comment` ( _body: str_ ) → IssueComment¶

     Calls:| POST /repos/{owner}/{repo}/issues/{number}/comments

---|---

`delete_labels` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/{number}/labels

---|---

`edit` ( _title: Opt[str] = NotSet_ , _body: Opt[str] = NotSet_ , _assignee: Opt[str | NamedUser | None] = NotSet_ , _state: Opt[str] = NotSet_ , _milestone: Opt[Milestone | None] = NotSet_ , _labels:
Opt[list[str]] = NotSet_ , _assignees: Opt[list[NamedUser | str]] = NotSet_ , _state_reason: Opt[str] = NotSet_ ) → None¶

     Calls:|

PATCH /repos/{owner}/{repo}/issues/{number}

---|---
Parameters:|

  + **assignee** – deprecated, use assignees instead. assignee=None means to remove current assignee.
  + **milestone** – milestone=None means to remove current milestone.

`lock` ( _lock_reason: str_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/issues/{issue_number}/lock

---|---

`unlock` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/{issue_number}/lock

---|---

`get_comment` ( _id: int_ ) → IssueComment¶

     Calls:| GET /repos/{owner}/{repo}/issues/comments/{id}

---|---

`get_comments` ( _since: Opt[datetime] = NotSet_ ) → PaginatedList[IssueComment]¶

     Calls:| GET /repos/{owner}/{repo}/issues/{number}/comments

---|---

`get_events` () → PaginatedList[IssueEvent]¶

     Calls:| GET /repos/{owner}/{repo}/issues/{issue_number}/events

---|---

`get_labels` () → PaginatedList[Label]¶

     Calls:| GET /repos/{owner}/{repo}/issues/{number}/labels

---|---

`remove_from_assignees` ( _*assignees_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/{number}/assignees

---|---

`remove_from_labels` ( _label: Label | str_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/{number}/labels/{name}

---|---

`set_labels` ( _*labels_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/issues/{number}/labels

---|---

`get_reactions` () → PaginatedList[Reaction]¶

     Calls:| GET /repos/{owner}/{repo}/issues/{number}/reactions

---|---

`create_reaction` ( _reaction_type: str_ ) → Reaction¶

     Calls:| POST /repos/{owner}/{repo}/issues/{number}/reactions

---|---

`delete_reaction` ( _reaction_id: int_ ) → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}

---|---

`get_timeline` () → PaginatedList[TimelineEvent]¶

     Calls:| GET /repos/{owner}/{repo}/issues/{number}/timeline

---|---
