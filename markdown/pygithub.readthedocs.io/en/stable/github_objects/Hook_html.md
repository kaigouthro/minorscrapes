  + Hook

* * *
# Hook¶

_class_ `github.Hook.`  `Hook` ¶

This class represents Hooks. The reference can be found here https://docs.github.com/en/rest/reference/repos#webhooks

`delete` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/hooks/{id}

---|---

`edit` ( _name: str_ , _config: dict_ , _events: Opt[list[str]] = NotSet_ , _add_events: Opt[list[str]] = NotSet_ , _remove_events: Opt[list[str]] = NotSet_ , _active: Opt[bool] = NotSet_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/hooks/{id}

---|---

`test` () → None¶

     Calls:| POST /repos/{owner}/{repo}/hooks/{id}/tests

---|---

`ping` () → None¶

     Calls:| POST /repos/{owner}/{repo}/hooks/{id}/pings

---|---
