  + RepositoryAdvisory

* * *
# RepositoryAdvisory¶

_class_ `github.RepositoryAdvisory.`  `RepositoryAdvisory` ¶

This class represents a RepositoryAdvisory. The reference can be found here https://docs.github.com/en/rest/security-advisories/repository-advisories

`add_vulnerability` ( _ecosystem: str_ , _package_name: str | None = None_ , _vulnerable_version_range: str | None = None_ , _patched_versions: str | None = None_ , _vulnerable_functions: list[str] |
None = None_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>

---|---

`add_vulnerabilities` ( _vulnerabilities: Iterable[Union[github. RepositoryAdvisoryVulnerability. SimpleAdvisoryVulnerability, RepositoryAdvisoryVulnerability]]_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>

---|---

`offer_credit` ( _login_or_user: str | github. NamedUser. NamedUser_ , _credit_type: str_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>

---|---

Offers credit to a user for a vulnerability in a repository. Unless you are giving credit to yourself, the user having credit offered will need to explicitly accept the credit.

`offer_credits` ( _credited: Iterable[Union[github. RepositoryAdvisoryCredit. SimpleCredit, RepositoryAdvisoryCredit]]_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>

---|---

Offers credit to a list of users for a vulnerability in a repository. Unless you are giving credit to yourself, the user having credit offered will need to explicitly accept the credit. :param
credited: iterable of dict with keys “login” and “type”

`revoke_credit` ( _login_or_user: str | github. NamedUser. NamedUser_ ) → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id

---|---

`clear_credits` () → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id

---|---

`edit` ( _summary: Union[str, github. GithubObject._NotSetType] = NotSet, description: Union[str, github. GithubObject._NotSetType] = NotSet, severity_or_cvss_vector_string: Union[str, 
github. GithubObject._NotSetType] = NotSet, cve_id: Union[str, github. GithubObject._NotSetType] = NotSet, vulnerabilities:
Union[Iterable[Union[github. RepositoryAdvisoryVulnerability. SimpleAdvisoryVulnerability, RepositoryAdvisoryVulnerability]], github. GithubObject._NotSetType] = NotSet, cwe_ids: Union[Iterable[str], 
github. GithubObject._NotSetType] = NotSet, credits: Union[Iterable[Union[github. RepositoryAdvisoryCredit. SimpleCredit, RepositoryAdvisoryCredit]], github. GithubObject._NotSetType] = NotSet, state:
Union[str, github. GithubObject._NotSetType] = NotSet_ ) → github. RepositoryAdvisory. RepositoryAdvisory¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id

---|---

`accept_report` () → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>

---|---

Accepts the advisory reported from an external reporter via private vulnerability reporting.

`publish` () → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>

---|---

Publishes the advisory.

`close` () → None¶

     Calls:| PATCH /repos/{owner}/{repo}/security-advisories/:advisory_id <https://docs.github.com/en/rest/security-advisories/repository-advisories>

---|---

Closes the advisory.
