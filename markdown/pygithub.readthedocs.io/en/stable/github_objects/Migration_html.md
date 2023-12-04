  + Migration

* * *
# Migration¶

_class_ `github.Migration.`  `Migration` ¶

This class represents Migrations. The reference can be found here https://docs.github.com/en/rest/reference/migrations

`get_status` () → str¶

     Calls:| GET /user/migrations/{migration_id}

---|---

`get_archive_url` () → str¶

     Calls:| GET /user/migrations/{migration_id}/archive

---|---

`delete` () → None¶

     Calls:| DELETE /user/migrations/{migration_id}/archive

---|---

`unlock_repo` ( _repo_name: str_ ) → None¶

     Calls:| DELETE /user/migrations/{migration_id}/repos/{repo_name}/lock

---|---
