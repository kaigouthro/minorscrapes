  + Gist

* * *
# Gist¶

_class_ `github.Gist.`  `Gist` ¶

This class represents Gists. The reference can be found here https://docs.github.com/en/rest/reference/gists

`create_comment` ( _body: str_ ) → GistComment¶

     Calls:| POST /gists/{gist_id}/comments

---|---

`create_fork` () → github. Gist. Gist¶

     Calls:| POST /gists/{id}/forks

---|---

`delete` () → None¶

     Calls:| DELETE /gists/{id}

---|---

`edit` ( _description: Opt[str] = NotSet_ , _files: Opt[dict[str_ , _InputFileContent | None]] = NotSet_ ) → None¶

     Calls:| PATCH /gists/{id}

---|---

`get_comment` ( _id: int_ ) → GistComment¶

     Calls:| GET /gists/{gist_id}/comments/{id}

---|---

`get_comments` () → PaginatedList[GistComment]¶

     Calls:| GET /gists/{gist_id}/comments

---|---

`is_starred` () → bool¶

     Calls:| GET /gists/{id}/star

---|---

`reset_starred` () → None¶

     Calls:| DELETE /gists/{id}/star

---|---

`set_starred` () → None¶

     Calls:| PUT /gists/{id}/star

---|---
