  + OrganizationVariable

* * *
# OrganizationVariable¶

_class_ `github.OrganizationVariable.`  `OrganizationVariable` ¶

This class represents a org level GitHub variable. The reference can be found here https://docs.github.com/en/rest/actions/variables

`visibility` ¶

     Type:| string

---|---

`edit` ( _value: str_ , _visibility: str = 'all'_ ) → bool¶

     Calls:|

PATCH /orgs/{org}/actions/variables/{variable_name}

---|---
Parameters:|

  + **variable_name** – string
  + **value** – string
  + **visibility** – string

Return type:|

bool

`add_repo` ( _repo: github. Repository. Repository_ ) → bool¶

     Calls:| ‘PUT {org_url}/actions/variables/{variable_name} <https://docs.github.com/en/rest/actions/variables#add-selected-repository-to-an-organization-secret>`_

---|---
Parameters:|  **repo** – github. Repository. Repository
Return type:| bool

`remove_repo` ( _repo: github. Repository. Repository_ ) → bool¶

     Calls:| ‘DELETE {org_url}/actions/variables/{variable_name} <https://docs.github.com/en/rest/actions/variables#add-selected-repository-to-an-organization-secret>`_

---|---
Parameters:|  **repo** – github. Repository. Repository
Return type:| bool
