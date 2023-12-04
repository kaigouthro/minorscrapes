  + Authorization

* * *
# Authorization¶

_class_ `github.Authorization.`  `Authorization` ¶

This class represents Authorizations. The reference can be found here https://docs.github.com/en/enterprise-server@3.0/rest/reference/oauth-authorizations

`created_at` ¶

     Type:| datetime.datetime

---|---

`delete` () → None¶

     Calls:| DELETE /authorizations/{id}

---|---

`edit` ( _scopes: Opt[list[str]] = NotSet_ , _add_scopes: Opt[list[str]] = NotSet_ , _remove_scopes: Opt[list[str]] = NotSet_ , _note: Opt[str] = NotSet_ , _note_url: Opt[str] = NotSet_ ) → None¶

     Calls:|

PATCH /authorizations/{id}

---|---
Parameters:|

  + **scopes** – list of string
  + **add_scopes** – list of string
  + **remove_scopes** – list of string
  + **note** – string
  + **note_url** – string

Return type:|

None
