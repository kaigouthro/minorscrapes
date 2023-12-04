  + PullRequestReview

* * *
# PullRequestReview¶

_class_ `github.PullRequestReview.`  `PullRequestReview` ¶

This class represents PullRequestReviews. The reference can be found here https://docs.github.com/en/rest/reference/pulls#reviews

`dismiss` ( _message: str_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/pulls/{number}/reviews/{review_id}/dismissals

---|---

`delete` () → None¶

     Calls:| DELETE /repos/:owner/:repo/pulls/:number/reviews/:review_id

---|---
