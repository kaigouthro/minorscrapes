  + Variable

* * *
# Variable¶

_class_ `github.Variable.`  `Variable` ¶

This class represents a GitHub variable. The reference can be found here https://docs.github.com/en/rest/actions/variables

`name` ¶

     Type:| string

---|---

`value` ¶

     Type:| string

---|---

`created_at` ¶

     Type:| datetime.datetime

---|---

`updated_at` ¶

     Type:| datetime.datetime

---|---

`url` ¶

     Type:| string

---|---

`edit` ( _value: str_ ) → bool¶

     Calls:|

PATCH /repos/{owner}/{repo}/actions/variables/{variable_name}

---|---
Parameters:|

  + **variable_name** – string
  + **value** – string

Return type:|

bool

`delete` () → None¶

     Calls:| DELETE {variable_url}

---|---
Return type:| None
